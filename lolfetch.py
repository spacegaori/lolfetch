from riotwatcher import LolWatcher, ApiError
from imgrender import render
from PIL import Image
import get_image
import os


lol_watcher = LolWatcher('RGAPI-d79c0d9c-1e9c-4a84-abb8-1aff12c203cd')

my_region = 'na1'

versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version= versions['n']['champion']
current_champ_list = lol_watcher.data_dragon.champions(champions_version)['data']

champion_name = input('Name of the champion?\n')
get_image.get_image(champion_name)
                      
champion = current_champ_list[champion_name]
name = champion['name']
title = champion['title']
blurb = champion['blurb']

print(name + ", " + title + "\n" + blurb)

render(champion_name + '.png', scale = (25, 25))

os.remove(champion_name + '.png') 


