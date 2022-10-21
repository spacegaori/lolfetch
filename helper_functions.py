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

def get_champion_icon(champion_name):
    url = 'https://ddragon.leagueoflegends.com/cdn/12.18.1/img/champion/' + champion_name + '.png'
    directory = 'icon.png'
    urllib.request.urlretrieve(url, directory)

def get_champion_splash(champion_name):
    url = 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/' + champion_name + '_0.jpg'
    directory = 'splash.jpg'
    urllib.request.urlretrieve(url, directory)


from colors import color
from PIL import Image
import numpy as np
from colorthief import ColorThief
from sty import fg, bg, ef, rs, Style, RgbFg
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

def get_dominant_color(champion_name):
    get_champion_splash(champion_name)
    color_thief = ColorThief('splash.jpg')
    (r, g, b) = color_thief.get_color(quality=1)
    os.remove('splash.jpg')
    
    return (r, g, b)

def colored_text(r, g, b):
    fg.dominant_color = Style(RgbFg(r, g, b))
    return fg.dominant_color

def reset_text():
    return fg.rs

def print_image():
    image = np.asarray(Image.open('icon.png'))
    output = render_image(image, (20, 20))
    rows = ('\n'.join([''.join(row) for row in output]))
    print(rows)

def print_combined(champion_name, r, g, b):
    image = np.asarray(Image.open('icon.png'))
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
        if i == 7:
            print(rows[i], end = '\t')
            print(colored_text(r, g, b) + champion_name + ', ' + title + reset_text(), end = '\n')
        elif i == 8:
            print(rows[i], end = '\t')
            for i in range(len(champion_name)+len(title) + 2):
                print('-', end='')
        elif i == 9:
            print('\n' + rows[i], end = '\t')
            print(colored_text(r, g, b) + '  ATK: ' + reset_text(), attack, end = '\n')
        elif i == 10:
            print(rows[i], end = '\t')
            print(colored_text(r, g, b) + '  DEF: ' + reset_text(), defense, end = '\n')
        elif i == 11:
            print(rows[i], end = '\t')
            print(colored_text(r, g, b) + '  INT: ' + reset_text(), magic, end = '\n')
        elif i == 12:
            print(rows[i], end = '\t')
            print(colored_text(r, g, b) + '  DIF: ' + reset_text(), difficulty, end = '\n')
        else:
            print(rows[i])
    print(blurb)
    
def remove_image():
    os.remove('icon.png')
