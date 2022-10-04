from riotwatcher import LolWatcher
import argparse

lol_watcher = LolWatcher(' ')

def get_champion_name():
    parser = argparse.ArgumentParser(description = 'Display champion information.')
    parser.add_argument('champion_name', type = str, help = 'Name of champion')
    arguments = parser.parse_args()

    return arguments.champion_name.capitalize()
    
def validate_arguments(argument_champion_name, champion_names):
    return argument_champion_name in champion_names

def get_latest_version(region = 'na1'): # default region is North America
    region = region                     # other regions are available as well
    version = lol_watcher.data_dragon.versions_for_region(region)
    
    return version

def get_champion_data():
    version = get_latest_version()
    champion_version = version['n']['champion']
    champion_data = lol_watcher.data_dragon.champions(champion_version)['data']
    
    return champion_data

def get_champion_names():
    champion_data = get_champion_data()
    champion_names = list()

    for champion in champion_data:
        champion_names.append(champion)
    
    return champion_names

def get_data(champion_name):
    return get_champion_data()[champion_name]

def get_champion_title(champion_name):
    return (get_data(champion_name))['title']

def get_champion_blurb(champion_name):
    return (get_data(champion_name))['blurb']

def get_champion_info(champion_name):
    return (get_data(champion_name))['info']

def get_champion_tags(champion_name):
    return (get_data(champion_name))['tags']

def print_champion_info(champion_name):
    title = get_champion_title(champion_name)
    blurb = get_champion_blurb(champion_name)
    info = get_champion_info(champion_name)
    attack = info['attack']
    defense = info['defense']
    magic = info['magic']
    difficulty = info['difficulty']
    tags = get_champion_tags(champion_name)
    print(champion_name + ', ' + title)
    print(blurb)
    print('ATK: ', attack)
    print('DEF: ', defense)
    print('INT: ', magic)
    print('DIF: ', difficulty)

import urllib.request

def get_champion_image(champion_name):
    url = 'https://ddragon.leagueoflegends.com/cdn/12.18.1/img/champion/' + champion_name + '.png'
    directory = 'temp.png'
    urllib.request.urlretrieve(url, directory)


from colors import color
from PIL import Image
import numpy as np
import os

def get_image_pixel(col):
    return color('  ', bg=f'rgb({int(col[0])}, {int(col[1])}, {int(col[2])})')

def render_image(pixels, scale = 20):
    image_size = pixels.shape[:2]
    block_size = (image_size[0] / scale[0], image_size[1] / scale[1])
    blocks = []
    y = 0
    while y < image_size[0]:
        x = 0
        block_col = []
        while x < image_size[1]:
            block_col.append(pixels[int(y):int(y+block_size[0]), int(x):int(x+block_size[1])].reshape(-1, 3).mean(axis=0))
            x += block_size[1]
        blocks.append(block_col)
        y += block_size[0]
    output = [[get_image_pixel(block) for block in row] for row in blocks]
    
    return output

def print_image():
    image = np.asarray(Image.open('temp.png'))
    output = render_image(image, (20, 20))
    rows = ('\n'.join([''.join(row) for row in output]))
    print(rows)

def print_combined(champion_name):
    image = np.asarray(Image.open('temp.png'))
    output = render_image(image, (20, 20))
    rows = [''.join(row) for row in output]
    
    title = get_champion_title(champion_name)
    blurb = get_champion_blurb(champion_name)
    info = get_champion_info(champion_name)
    attack = info['attack']
    defense = info['defense']
    magic = info['magic']
    difficulty = info['difficulty']
    tags = get_champion_tags(champion_name)
    
    i = 0
    for i in range(20):
        if i == 8:
            print(rows[i], end = '\t')
            print(champion_name + ', ' + title, end = '\n')
        elif i == 9:
            print(rows[i], end = '\t  ')
            print('ATK: ', attack, end = '\n')
        elif i == 10:
            print(rows[i], end = '\t  ')
            print('DEF: ', defense, end = '\n')
        elif i == 11:
            print(rows[i], end = '\t  ')
            print('INT: ', magic, end = '\n')
        elif i == 12:
            print(rows[i], end = '\t  ')
            print('DIF: ', difficulty, end = '\n')
        else:
            print(rows[i])
    
def remove_image():
    os.remove('temp.png')