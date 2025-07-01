import psycopg2
import configparser
import logging

class PGSQLHandler:
    def __init__(self, config_file="config.ini"):
        config = configparser.ConfigParser()
        config.read(config_file)
        pg_conf = config['postgresql']
        self.conn = psycopg2.connect(
            host=pg_conf['host'],
            user=pg_conf['user'],
            password=pg_conf['password'],
            dbname=pg_conf['database']
        )
        self.cursor = self.conn.cursor()

    def create_tables(self, ddl_file):
        with open(ddl_file, 'r') as f:
            ddl = f.read()
        self.cursor.execute(ddl)
        self.conn.commit()

    def insert_data(self, df):
        if df.empty:
            logging.info("No data to insert.")
            return
        sql = """
        INSERT INTO gho_data (report_date, country_name, indicator_code, value)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (country_name, indicator_code, report_date) DO NOTHING;
        """
        records = [tuple(map(lambda x: x.item() if hasattr(x, 'item') else x, r)) for r in df.to_records(index=False)]

        self.cursor.executemany(sql, records)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
