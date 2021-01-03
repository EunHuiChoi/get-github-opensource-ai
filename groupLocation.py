import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def usa_city_list(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    city_table = soup.find("table", {"class": "wikitable sortable"})

    city_print = []
    # print(soup.find("table", {"class": "wikitable sortable"}).find_all("th"))
    for a in city_table.find_all('td'):
        infolist = []
        for b in a.find_all('a'):
            info = b.get_text()
            no_num = re.compile('[^0-9]')
            this = "".join(no_num.findall(info))
            str(this)
            infolist.append(info)
        city_print.append(infolist)
        city_print = list(filter(None, city_print))
    usa_city = sum(city_print, [])
    usa_city = list(filter(None, usa_city))
    final = list(filter(lambda a: a!= '[]', usa_city))
    return usa_city


df = pd.read_csv("inprogress_data_2019.csv")

df = df.astype({'owner_location': 'str'})
print(df.shape)

city_list = usa_city_list('https://en.wikipedia.org/wiki/List_of_cities_in_Canada#British_Columbia')
print(city_list)

temp = df['owner_location'].str.contains('|'.join(city_list))
filter_df = df[temp]

print(filter_df)

filter_df.to_csv("3_canada_filter.csv", index=False)

