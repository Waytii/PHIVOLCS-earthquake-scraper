import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.phivolcs.dost.gov.ph/index.php/earthquake/latest-earthquakes"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')[1:]

data = []
for row in rows:
    cols = row.find_all('td')
    data.append([col.text.strip() for col in cols])

columns = ['Date', 'Time', 'Latitude', 'Longitude', 'Depth', 'Magnitude', 'Location']
df = pd.DataFrame(data, columns=columns)
df.to_csv('phivolcs_earthquakes.csv', index=False)
