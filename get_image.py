import urllib.request

def get_image(champion_name):
    url = 'https://ddragon.leagueoflegends.com/cdn/12.18.1/img/champion/' + champion_name + '.png'
    dir = champion_name + '.png'
    urllib.request.urlretrieve(url, dir)