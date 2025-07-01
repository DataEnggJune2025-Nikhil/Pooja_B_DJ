# Global Healthcare Data ETL & Analysis CLI 🌍💉

## Overview

This project is a command-line application that extracts healthcare data from a public API or CSV, transforms it into a clean and structured format, loads it into a PostgreSQL database, and allows users to perform analytical queries directly from the CLI. It demonstrates critical data engineering skills, including data ingestion, cleaning, storage, and reporting.

---

## Features

* Connects to a public healthcare API (e.g., WHO or similar) or reads from CSV files.
* Extracts data with user-defined parameters (country, indicator).
* Cleans and transforms data: handles missing values, standardizes formats, removes duplicates, applies business logic.
* Loads data into PostgreSQL using efficient batch inserts with incremental load support.
* Auto-generates `id` (SERIAL PRIMARY KEY) and sets `etl_timestamp` during data load.
* Provides a CLI with commands for data fetching, queries, exports, and database management.
* Supports extended query types for richer analysis.
* Displays results in clean tabular format using `tabulate`.
* Implements robust error handling and logging.

---

## CLI Usage Examples

### Fetch and load data

```bash
python main.py fetch-data --indicator WHOSIS_000001 --country IND
```

### Run queries (available query types)

```bash
python main.py query-data total_cases India
python main.py query-data daily_trends WHOSIS_000001
python main.py query-data daily_trends India WHOSIS_000001
python main.py query-data top_n_countries_by_metric 3 WHOSIS_000001
python main.py query-data avg_metric_by_country WHOSIS_000001
python main.py query-data latest_value_by_country WHOSIS_000001
python main.py query-data country_rank_by_indicator WHOSIS_000001
```

### Manage database

```bash
python main.py list-tables
python main.py drop-tables
```

### Export dataset

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

* **Extract:** Connect to API or read CSV, fetch data.
* **Transform:** Clean data using Pandas, standardize names, convert types, remove duplicates, apply business logic.
* **Load:** Insert into PostgreSQL using batch inserts, skip/update existing records (incremental load).

---

## Extended Query Types

* **avg\_metric\_by\_country** — Returns the average metric value per country for a given indicator.
* **latest\_value\_by\_country** — Returns the latest available value per country for a given indicator.
* **country\_rank\_by\_indicator** — Ranks countries by total metric value for a given indicator.

---

## Future Improvements

* Add support for multiple APIs.
* Integrate CLI visualizations (e.g., asciichartpy).
* Generate HTML/CSV reports from queries.
* Explore orchestration with Airflow/Prefect.

---

## Author

Pooja Bavisetti

---

## License

MIT License
