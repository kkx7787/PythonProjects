import requests
from bs4 import BeautifulSoup
import time
import schedule

def get_currency():
    url = 'https://www.kita.net/cmmrcInfo/ehgtGnrlzInfo/rltmEhgt.do'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    new_won_list = soup.select('td')
    for i in new_won_list:
        new_won = i.get_text()
        break

    new_won = new_won.replace(',', '')
    return new_won