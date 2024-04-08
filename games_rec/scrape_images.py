from bs4 import BeautifulSoup
import requests

def scrape_first_image(game_name):
    search_url = f'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q=${game_name}'  
    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        first_image = soup.find('img')
        if first_image:
            return first_image['src']
    
    return None
