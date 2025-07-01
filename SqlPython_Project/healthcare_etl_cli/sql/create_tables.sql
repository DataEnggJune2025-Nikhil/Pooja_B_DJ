CREATE TABLE IF NOT EXISTS gho_data (
    id SERIAL PRIMARY KEY,
    report_date DATE NOT NULL,
    country_name VARCHAR(10) NOT NULL,
    indicator_code VARCHAR(50) NOT NULL,
    value NUMERIC,
    etl_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (country_name, indicator_code, report_date)
);
