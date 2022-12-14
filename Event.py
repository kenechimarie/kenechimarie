from bs4 import BeautifulSoup
import datetime
import requests
import time

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
    "Sunday " + sunday.strftime('%Y-%m-%d'): sunday}

Events = {
  "Open Air": "https://www.gaesteliste030.de/de/berlin/events/open-air/14-12-22",
  "Electro": "https://www.gaesteliste030.de/de/berlin/events/electro/14-12-22",
  "Party": "https://www.gaesteliste030.de/de/berlin/events/party/14-12-22"
}
list_of_Events = list(Events)
list_of_weekdays = list(weekdays)
def find_event(url):
    berlin_text = requests.get(url)
    soup = BeautifulSoup(berlin_text.content, 'html.parser')
    events = soup.find_all('div', class_ = 'xcard-body no-spacing')
    for event in events:
        Event_title = event.find('h4', class_ = 'title font-size-default').text.replace(' ','')
        location = event.find('span', class_ = 'location-link').text.replace(' ','')
        more_info = event.div.h4.a['href']
        category = event.find('span', class_ = 'tag badge-hashtag tag-secondary').text.replace(' ','')
        
        print(f"Event Name: {Event_title.strip()}")
        print(f"Location: {location.strip()}")
        print(f"More Info: {more_info}")
        print(f"Music Genre: {category}")

        print('')
if __name__ == '__main__':
    for key, value in Events.items():
        print(f'{list(Events).index(key)}. {key}')
    category = input("Choose a category: ")
    keyForEvent = list_of_Events[int(category)]
    for key in weekdays:
        print(f'{list(weekdays).index(key)}. {key}')
    date = input('Choose a date: ')
    weekday = list_of_weekdays[int(date)].split()[1]
    formatted_url = Events[keyForEvent].format(weekday, weekday)
    find_event(formatted_url)