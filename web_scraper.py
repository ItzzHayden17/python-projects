#pip install requests
#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)  #Make initial request to the url

soup = BeautifulSoup(page.content,"html.parser")

#id = soup.find(id = "ResultsContainer")
#string = soup.find("h2", string="React")  for specific job listings

card_elements = soup.find_all("div",class_= "card-content")

for card in card_elements:
    title = card.find("h2" , class_="title")
    subtitle = card.find("h3" , class_="subtitle")
    print("-"*100)
    print(title.text)
    print(subtitle.text)
    print("-"*100)