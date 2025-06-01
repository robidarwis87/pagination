import pandas as pd
import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.scrapethissite.com/pages/forms/?page_num=1')

BASE_URL = 'https://www.scrapethissite.com/pages/forms/'
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('table', class_='table')
rows = soup.find_all('tr', class_='team')

result = []
for row in rows:
    team_name = row.find('td', class_='name').get_text(strip=True)
    year = row.find('td', class_='year').get_text(strip=True)
    winprcent = row.find('td', class_='pct').get_text(strip=True)
    
    result.append({
        'Team_name': team_name,
        'Year': year,
        'Win_precent': winprcent
    })
# for item in result:
#     print(f"{item['Team_name']}, {item['Year']}, {item['Win_precent']}")
    
    
# df = pd.DataFrame(result)
# df.to_csv('teams.csv')