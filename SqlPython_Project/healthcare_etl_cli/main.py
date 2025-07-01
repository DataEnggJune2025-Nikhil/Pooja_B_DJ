import click
import logging
from api_client import APIClient
from data_transformer import DataTransformer
from pgsql_handler import PGSQLHandler
from tabulate import tabulate


logging.basicConfig(level=logging.INFO)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--indicator', required=True, help='Indicator code (e.g. WHOSIS_000001)')
@click.option('--country', help='Country code (e.g. IND)')
def fetch_data(indicator, country):
    api = APIClient()
    transformer = DataTransformer()
    db = PGSQLHandler()

    db.create_tables('sql/create_tables.sql')
    raw_data = api.fetch_data(indicator, country)
    df = transformer.clean_and_transform(raw_data)
    db.insert_data(df)
    db.close()
    click.echo(f"Fetched, transformed, and loaded {len(df)} records.")

@cli.command()
def list_tables():
    db = PGSQLHandler()
    db.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = db.cursor.fetchall()
    for t in tables:
        click.echo(t[0])
    db.close()

@cli.command()
def drop_tables():
    db = PGSQLHandler()
    db.cursor.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
    db.conn.commit()
    db.close()
    click.echo("Dropped and recreated schema.")
    

import csv

def export_to_csv(path, headers, rows):
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    click.echo(f"Results exported to {path}")

@cli.command()
@click.argument('query_type')
@click.argument('args', nargs=-1)
def query_data(query_type, args):
    """Run predefined analytical queries and optionally export to CSV."""
    db = PGSQLHandler()

    if query_type == 'total_cases':
        if len(args) == 0:
            sql = """
            SELECT country_name, SUM(value)::numeric(10,2) AS total_value
            FROM gho_data
            WHERE value IS NOT NULL AND country_name IS NOT NULL
            GROUP BY country_name
            HAVING SUM(value) IS NOT NULL
            ORDER BY total_value DESC;
            """
            db.cursor.execute(sql)
            rows = db.cursor.fetchall()
            headers = ["Country", "Total Value"]
            if rows:
                click.echo(tabulate(rows, headers=headers, tablefmt="pretty"))
            
            else:
                click.echo("No data found.")

        elif len(args) == 1:
            country = args[0]
            sql = """
            SELECT country_name, SUM(value)::numeric(10,2) AS total_value
            FROM gho_data
            WHERE country_name = %s AND value IS NOT NULL
            GROUP BY country_name;
            """
            db.cursor.execute(sql, (country,))
            row = db.cursor.fetchone()
            headers = ["Country", "Total Value"]
            if row:
                click.echo(tabulate([row], headers=headers, tablefmt="pretty"))
            
            else:
                click.echo(f"No data found for country: {country}")

        else:
            click.echo("Usage: query-data total_cases [<country>]")

    elif query_type == 'daily_trends':
        if len(args) == 1:
            indicator = args[0]
            sql = """
            SELECT report_date, country_name, value
            FROM gho_data
            WHERE indicator_code = %s AND value IS NOT NULL
            ORDER BY country_name, report_date;
            """
            db.cursor.execute(sql, (indicator,))
            rows = db.cursor.fetchall()
            headers = ["Date", "Country", "Value"]
            if rows:
                click.echo(tabulate(rows, headers=headers, tablefmt="pretty"))
                
            else:
                click.echo(f"No data found for indicator: {indicator}")

        elif len(args) == 2:
            country, indicator = args
            sql = """
            SELECT report_date, value
            FROM gho_data
            WHERE country_name = %s AND indicator_code = %s AND value IS NOT NULL
            ORDER BY report_date;
            """
            db.cursor.execute(sql, (country, indicator))
            rows = db.cursor.fetchall()
            headers = ["Date", "Value"]
            if rows:
                click.echo(tabulate(rows, headers=headers, tablefmt="pretty"))
                
            else:
                click.echo(f"No data found for {country} and indicator {indicator}")

        else:
            click.echo("Usage: query-data daily_trends <indicator> [<country>]")
    elif query_type == 'avg_metric_by_country':
        if len(args) != 1:
            click.echo("Usage: query-data avg_metric_by_country <indicator>")
        else:
            indicator = args[0]
            sql = """
            SELECT country_name, AVG(value)::numeric(10,2) AS avg_value
            FROM gho_data
            WHERE indicator_code = %s AND value IS NOT NULL
            GROUP BY country_name
            ORDER BY avg_value DESC;
            """
            db.cursor.execute(sql, (indicator,))
            rows = db.cursor.fetchall()
            headers = ["Country", "Average Value"]
            click.echo(tabulate(rows, headers=headers, tablefmt="pretty"))
    elif query_type == 'latest_value_by_country':
        if len(args) != 1:
            click.echo("Usage: query-data latest_value_by_country <indicator>")
        else:
            indicator = args[0]
            sql = """
            SELECT DISTINCT ON (country_name) country_name, report_date, value
            FROM gho_data
            WHERE indicator_code = %s AND value IS NOT NULL
            ORDER BY country_name, report_date DESC;
            """
            db.cursor.execute(sql, (indicator,))
            rows = db.cursor.fetchall()
            headers = ["Country", "Latest Report Date", "Latest Value"]
            click.echo(tabulate(rows, headers=headers, tablefmt="pretty"))
            
    elif query_type == 'country_rank_by_indicator':
        if len(args) != 1:
            click.echo("Usage: query-data country_rank_by_indicator <indicator>")
        else:
            indicator = args[0]
            sql = """
            SELECT country_name, SUM(value)::numeric(10,2) AS total_value
            FROM gho_data
            WHERE indicator_code = %s AND value IS NOT NULL
            GROUP BY country_name
            ORDER BY total_value DESC;
            """
            db.cursor.execute(sql, (indicator,))
            rows = db.cursor.fetchall()
            headers = ["Rank", "Country", "Total Value"]
            ranked_rows = [(idx+1, r[0], r[1]) for idx, r in enumerate(rows)]
            click.echo(tabulate(ranked_rows, headers=headers, tablefmt="pretty"))        
        
    elif query_type == 'top_n_countries_by_metric':
        if len(args) != 2:
            click.echo("Usage: query-data top_n_countries_by_metric <n> <indicator>")
        else:
            n = int(args[0])
            indicator = args[1]
            sql = """
            SELECT country_name, SUM(value)::numeric(10,2) AS total_value
            FROM gho_data
            WHERE indicator_code = %s AND value IS NOT NULL
            GROUP BY country_name
            ORDER BY total_value DESC
            LIMIT %s;
            """
            db.cursor.execute(sql, (indicator, n))
            rows = db.cursor.fetchall()
            headers = ["Rank", "Country", "Total Value"]
            if rows:
                ranked_rows = [(idx+1, r[0], r[1]) for idx, r in enumerate(rows)]
                click.echo(tabulate(ranked_rows, headers=headers, tablefmt="pretty"))
                
            else:
                click.echo(f"No data found for indicator: {indicator}")

    else:
        click.echo("Invalid query type. Options: total_cases, daily_trends, top_n_countries_by_metric")

    db.close()

@cli.command()
@click.option('--export-csv', type=click.Path(), required=True, help='Path to export the entire dataset as CSV')
def export_full_dataset(export_csv):
    """Export the entire clean gho_data dataset to a CSV file."""
    db = PGSQLHandler()
    sql = """
    SELECT report_date, country_name, indicator_code, value
    FROM gho_data
    WHERE value IS NOT NULL AND country_name IS NOT NULL
    ORDER BY country_name, indicator_code, report_date;
    """
    db.cursor.execute(sql)
    rows = db.cursor.fetchall()
    headers = ["Report Date", "Country", "Indicator", "Value"]

    import csv
    with open(export_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    click.echo(f"✅ Complete dataset exported to {export_csv}")
    db.close()



if __name__ == '__main__':
    cli()
