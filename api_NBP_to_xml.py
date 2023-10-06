

import requests as re
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'
url2 = 'http://api.nbp.pl/api/exchangerates/tables/B/?format=xml'

response = re.get(url2)
# print(response)
xml_data = response.content
# print(xml_data)

root = ET.fromstring(xml_data)
table_name = root.find(".//Table").text
# print(table_name) # A


date = root.find(".//EffectiveDate").text
# print(date) # 2023-10-06

no = root.find(".//No").text
# print(f"Numer tabeli: ",no) # Numer tabeli:  194/A/NBP/2023

rates = root.findall(".//Rate") # wyciagamy z tabeli tylko info o kursie walut
# print(rates)
#   [<Element 'Rate' at 0x000002B3E4BE1E40>, <Element 'Rate' at 0x000002B3E4BE1F80>, <Element 'Rate' at 0x000002B3E4BE20C0>, <Element 'Rate' at 0x000002B3E4BE2250>, <Element 'Rate' at 0x000002B3E4BE2390>, <Element 'Rate' at 0x000002B3E4BE2520>, <Element 'Rate' at 0x000002B3E4BE26B0>, <Element 'Rate' at 0x000002B3E4BE2840>, <Element 'Rate' at 0x000002B3E4BE2980>, <Element 'Rate' at 0x000002B3E4BE2AC0>, <Element 'Rate' at 0x000002B3E4BE2C50>, <Element 'Rate' at 0x000002B3E4BE2D90>, <Element 'Rate' at 0x000002B3E4BE2F20>, <Element 'Rate' at 0x000002B3E4BE3060>, <Element 'Rate' at 0x000002B3E4BE31A0>, <Element 'Rate' at 0x000002B3E4BE32E0>, <Element 'Rate' at 0x000002B3E4BE3470>, <Element 'Rate' at 0x000002B3E4BE35B0>, <Element 'Rate' at 0x000002B3E4BE36F0>, <Element 'Rate' at 0x000002B3E4BE3830>, <Element 'Rate' at 0x000002B3E4BE3970>, <Element 'Rate' at 0x000002B3E4BE3AB0>, <Element 'Rate' at 0x000002B3E4BE3C40>, <Element 'Rate' at 0x000002B3E4BE3D80>, <Element 'Rate' at 0x000002B3E4BE3EC0>, <Element 'Rate' at 0x000002B3E4BF0040>, <Element 'Rate' at 0x000002B3E4BF0180>, <Element 'Rate' at 0x000002B3E4BF02C0>, <Element 'Rate' at 0x000002B3E4BF0450>, <Element 'Rate' at 0x000002B3E4BF05E0>, <Element 'Rate' at 0x000002B3E4BF0720>, <Element 'Rate' at 0x000002B3E4BF0860>, <Element 'Rate' at 0x000002B3E4BF09F0>]

# wyciągay i wypisujemy kursy

for rate in rates:
    currency = rate.find('Currency').text # wyciąganie danych xml odtyczacych waluty
    code = rate.find('Code').text  # wyciąganie danych xml odtyczacych kodu waluty
    mid = rate.find('Mid').text  # # wyciąganie danych xml odtyczacych kodu kursu
    print(f"{code}: {currency} - {mid}")
