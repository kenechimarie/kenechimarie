from bs4 import BeautifulSoup
import requests
import datetime
#from bs4 import BeautifulSoup
today = datetime.date.today()
monday = today + datetime.timedelta((0-today.weekday()) % 7)
tuesday = today + datetime.timedelta((1-today.weekday()) % 7)
wednesday = today + datetime.timedelta((2-today.weekday()) % 7)
thursday = today + datetime.timedelta((3-today.weekday()) % 7)
friday = today + datetime.timedelta((4-today.weekday()) % 7)
saturday = today + datetime.timedelta((5-today.weekday()) % 7)
sunday = today + datetime.timedelta((6-today.weekday()) % 7)
weekdays = {
    "Monday " + monday.strftime('%Y-%m-%d'): monday,
    "Tuesday " + tuesday.strftime('%Y-%m-%d'): tuesday,
    "Wednesday " + wednesday.strftime('%Y-%m-%d'): wednesday,
    "Thursday " + thursday.strftime('%Y-%m-%d'): thursday,
    "Friday " + friday.strftime('%Y-%m-%d'): friday,
    "Saturday " + saturday.strftime('%Y-%m-%d'): saturday,
    "Sunday " + sunday.strftime('%Y-%m-%d'): sunday
}
urls = {
    "Ausstellungen": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=9315&keys=&date_between%5Bmin%5D=&date_between%5Bmin%5D=2022-12-16&date_between%5Bmin%5D{0}&date_between%5Bmax%5D={1}&district=All&items_per_page=21",
    "Comedy": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=9320&keys=&date_between%5Bmin%5D=&date_between%5Bmin%5D{0}&date_between%5Bmax%5D={1}&district=All&items_per_page=21",
    "Konzerte": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=29169&keys=&date_between%5Bmin%5D=&date_between%5Bmin%5D{0}&date_between%5Bmax%5D={1}&district=All&items_per_page=21",
    "Nachtleben": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=9330&keys=&date_between%5Bmin%5D=&date_between%5Bmin%5D{0}&date_between%5Bmax%5D={1}&district=All&items_per_page=21",
    "Food": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=16379&keys=&date_between%5Bmin%5D=&date_between%5Bmin%5D{0}&date_between%5Bmax%5D={1}&district=All&items_per_page=21",
    "Theater": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=6&keys=&date_between%5Bmin%5D=&date_between%5Bmin%5D{0}&date_between%5Bmax%5D={1}&district=All&items_per_page=21",
    "Sport": "https://www.visitberlin.de/de/veranstaltungskalender-berlin?cat%5B%5D=9316&keys=&date_between%5Bmin%5D=&date_between%5Bmin%5D{0}&date_between%5Bmax%5D={1}&district=All&items_per_page=21"
    }
list_of_urls = list(urls)
list_of_weekdays = list(weekdays)
def find_events(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    for event in soup.select('.teaser-search__content'):
        title = event.find('h2').get_text()
        time = event.find('time').get_text()
        address = event.find_next('span', class_='teaser-search__print-address teaser-search__print-info').get_text()
        link = event.find_next('p', class_="teaser-search__print-link teaser-search__print-info").get_text()
        description = event.find_next('div', class_='teaser-search__text').get_text()
        print(title,time,address,description,link)
if __name__ == '__main__':
    for key, value in urls.items():
        print(f'{list(urls).index(key)}. {key}')
    category = input("Choose a category: ")
    keyForUrl = list_of_urls[int(category)]
    for key in weekdays:
        print(f'{list(weekdays).index(key)}. {key}')
    date = input('Choose a date: ')
    weekday = list_of_weekdays[int(date)].split()[1]
    formatted_url = urls[keyForUrl].format(weekday, weekday)
    find_events(formatted_url)