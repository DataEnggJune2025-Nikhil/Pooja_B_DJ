# Global Healthcare Data ETL & Analysis CLI 🌍💉

## Overview

This project is a command-line tool that extracts healthcare data from a public API or CSV, transforms it into a clean format, loads it into PostgreSQL, and allows analytical queries via CLI. It demonstrates data engineering skills such as data ingestion, cleaning, storage, and reporting.

---

## Features

* Connects to public API (e.g. WHO) or CSV source.
* Extracts data based on country and indicator.
* Cleans data (handles missing values, converts types, standardizes names, removes duplicates).
* Loads data into PostgreSQL using batch inserts with incremental load logic.
* Automatically generates `id` and `etl_timestamp` on insert.
* Provides CLI commands for ETL, queries, export, and DB management.
* Supports extended analytical queries.
* Displays results in tables using `tabulate`.
* Includes robust error handling and logging.

---

## File Structure

```
healthcare_etl_cli/
├── main.py                # CLI entry point
├── api_client.py          # API handler
├── data_transformer.py    # Data cleaning logic
├── pgsql_handler.py       # DB operations
├── config.ini             # DB/API config
├── requirements.txt       # Dependencies
├── health.csv             # exported data file
├── sql/
│   └── create_tables.sql  # DB schema DDL
├── screenshots/           # CLI output screenshots
│   ├── Screenshot 2025-07-01 110629.png
│   ├── Screenshot 2025-07-01 110809.png
│   ├── Screenshot 2025-07-01 113506.png
│   ├── Screenshot 2025-07-01 113647.png
│   └── Screenshot 2025-07-01 113753.png
└── README.md              # Project documentation
```

---

## Installation

```bash
pip install -r requirements.txt
```

Set up your PostgreSQL DB using:

```bash
psql -d <dbname> -f sql/create_tables.sql
```

Update `config.ini` with DB credentials and API keys.

---

## CLI Usage

### Fetch data

```bash
python main.py fetch-data --indicator WHOSIS_000001 --country IND
```

### Queries

```bash
python main.py query-data total_cases India
python main.py query-data daily_trends WHOSIS_000001
python main.py query-data daily_trends India WHOSIS_000001
python main.py query-data top_n_countries_by_metric 3 WHOSIS_000001
python main.py query-data avg_metric_by_country WHOSIS_000001
python main.py query-data latest_value_by_country WHOSIS_000001
python main.py query-data country_rank_by_indicator WHOSIS_000001
```

### Manage DB

```bash
python main.py list-tables
python main.py drop-tables
```

### Export

```bash
python main.py export-full-dataset --export-csv output.csv
```

---

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS gho_data (
  id SERIAL PRIMARY KEY,
  report_date DATE NOT NULL,
  country_name VARCHAR(50) NOT NULL,
  indicator_code VARCHAR(50) NOT NULL,
  value NUMERIC,
  etl_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (country_name, indicator_code, report_date)
);
```

---

## ETL Process

* **Extract:** API/CSV fetch.
* **Transform:** Clean, standardize, deduplicate.
* **Load:** Batch insert, incremental load.

---

## Extended Queries

* `avg_metric_by_country`: Average value per country for indicator.
* `latest_value_by_country`: Latest value per country for indicator.
* `country_rank_by_indicator`: Rank countries by total metric value.

---

## Future Enhancements

* Multi-API support.
* CLI visualizations.
* HTML/CSV report generation.
* Airflow/Prefect orchestration.

---

## Author

Pooja Bavisetti 

## Data Source

Data used in this project was obtained from the WHO Global Health Observatory API: [https://www.who.int/data/gho](https://www.who.int/data/gho)

## License

MIT License
