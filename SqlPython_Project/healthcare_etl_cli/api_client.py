import requests
import logging

class APIClient:
    def __init__(self, base_url="https://ghoapi.azureedge.net/api/"):
        self.base_url = base_url

    def fetch_data(self, indicator_code, country_code=None):
        url = f"{self.base_url}{indicator_code}"
        if country_code:
            url += f"?$filter=SpatialDim eq '{country_code}'"
        try:
            logging.info(f"Fetching data from: {url}")
            response = requests.get(url)
            response.raise_for_status()
            return response.json().get('value', [])
        except requests.RequestException as e:
            logging.error(f"API request failed: {e}")
            return []

