import pandas as pd

class DataTransformer:
    def clean_and_transform(self, raw_data):
        df = pd.DataFrame(raw_data)
        if df.empty:
            return df

        df = df[df['SpatialDimType'] == 'COUNTRY']  # Keep only countries

        df = df.rename(columns={
            'SpatialDim': 'country_name',
            'IndicatorCode': 'indicator_code',
            'NumericValue': 'value',
            'TimeDim': 'report_year'
        })

        df['report_date'] = pd.to_datetime(df['report_year'], format='%Y', errors='coerce').dt.date
        df['value'] = pd.to_numeric(df['value'], errors='coerce').astype(float)
        df = df.drop_duplicates(subset=['country_name', 'indicator_code', 'report_date'])
        df = df[['report_date', 'country_name', 'indicator_code', 'value']]
        return df
