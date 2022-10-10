from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://jiji.ng/lagos/houses-apartments-for-rent?utm_source=google_adw&utm_medium=4040486029&utm_campaign=11825087745&utm_content=118839766921&utm_term=486441484478&gclid=Cj0KCQjwhY-aBhCUARIsALNIC05S24tzNsfJx9UMaEqVLojCN3-GcykoDOuoNqHL3x6DaeTaVcl4oQUaAhpDEALw_wcB'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

apartments = soup.find_all("div")
title = soup.find_all('h4', class_="qa-advert-title b-list-advert__item-title")
price = soup.find_all("p", class_="b-list-advert__item-price")

with open("houses.csv", "w", encoding="utf8", newline="") as f:
    my_writer = writer(f)
    header = ["Location", "Price"]
    my_writer.writerow(header)
    for name, cost in zip(title, price):
        info = [name.text.replace("\n", ""), cost.text.replace("\n", "")]
        my_writer.writerow(info)



