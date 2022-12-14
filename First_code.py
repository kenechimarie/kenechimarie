from bs4 import BeautifulSoup
import requests
import time
print('Enter your location')
where_are_you = input('>')
print(f"Looking for Events in: {where_are_you}")
def find_event():
    berlin_text = requests.get('https://www.gaesteliste030.de/#Y3IxOjE6MA==').text
    soup = BeautifulSoup(berlin_text, 'lxml')
    events = soup.find_all('div', class_ = 'xcard-body no-spacing')
    for event in events:
        Event_title = event.find('h4', class_ = 'title font-size-default').text.replace(' ','')
        organiser = event.find('span', class_ = 'location-link').text.replace(' ','')
        #venue = event.div.span.a['href']
        more_info = event.div.h4.a['href']
        category = event.find('span', class_ = 'tag badge-hashtag tag-secondary').text.replace(' ','')
        if where_are_you not in organiser:
            print(f"Event Name: {Event_title.strip()}")
            print(f"Organiser: {organiser.strip()}")
            print(f"More Info: {more_info}")
            print(f"Music Genre: {category}")
            #print(f"Address: {venue}")
            print('')
    
if __name__ == '__main__':
    while True:
        find_event()
        time_wait = 15
        print(f"waiting: {time_wait} seconds...")
        time.sleep(time_wait * 100)