import requests
from bs4 import BeautifulSoup
urls = {
  "Ausstellungen": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=9315&keys=&date_between%5Bmin%5D=&date_between%5Bmax%5D=&district=All&items_per_page=21",
  "Comedy": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=9320&keys=&date_between%5Bmin%5D=&date_between%5Bmax%5D=&district=All&items_per_page=21",
  "Konzerte": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=29169&keys=&date_between%5Bmin%5D=&date_between%5Bmax%5D=&district=All&items_per_page=21"
}
list_of_urls = list(urls)
def find_events(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    
    for event in soup.select('.teaser-search__content'):
        title = event.find("h2").get_text()
        print(title)

        
if __name__ == '__main__':
    for key, value in urls.items():
        print(f"{list(urls).index(key)}. {key}")
    category = input("Choose a category: ")
    listElement = list_of_urls[int(category)]
    
    find_events(urls[listElement])