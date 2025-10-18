import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta
import os
import pandas as pd
from datetime import timedelta

try:
    url = "https://earthquake.phivolcs.dost.gov.ph/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    if not table:
        raise ValueError("No earthquake table found on the page.")

    rows = table.find_all('tr')[1:]
    data = []
    for row in rows:
        cols = row.find_all('td')
        data.append([col.text.strip() for col in cols])

    columns = ['Date', 'Time', 'Latitude', 'Longitude', 'Depth', 'Magnitude', 'Location']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('phivolcs_earthquakes.csv', index=False)
    print("Scraping successful.")

except Exception as e:
    print(f"Error occurred: {e}")
    exit(1)
