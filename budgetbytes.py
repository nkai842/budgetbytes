import requests
from bs4 import BeautifulSoup

url = 'https://www.budgetbytes.com/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

for recipe in soup.find_all('a'):
##    print(recipe.get_text())
    if 'title' in recipe.attrs and 'rel' in recipe.attrs and not 'target' in recipe.attrs:
        print(recipe.get('title'))
        print(recipe.get('href'))
        print("\n")
         

input("Press Enter to Exit. . .")
