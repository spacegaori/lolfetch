# from colors import color
# from PIL import Image, ImageFilter
# import numpy as np
# from riotwatcher import LolWatcher, ApiError
# import lolfetch.get_champion_icon as get_champion_icon
import os

import helper_functions


# def get_pixel(col):
#     return color('  ', bg=f'rgb({int(col[0])}, {int(col[1])}, {int(col[2])})')

# def render_image(pixels, scale):
#     # first of all scale the image to the scale 'tuple'
#     image_size = pixels.shape[:2]
#     block_size = (image_size[0]/scale[0], image_size[1]/scale[1])
#     blocks = []
#     y = 0
#     while y < image_size[0]:
#         x = 0
#         block_col = []
#         while x < image_size[1]:
#             # get a block, reshape in into an Nx3 matrix and then get average of each column
#             block_col.append(pixels[int(y):int(y+block_size[0]), int(x):int(x+block_size[1])].reshape(-1, 3).mean(axis=0))
#             x += block_size[1]
#         blocks.append(block_col)
#         y += block_size[0]
#     output = [[get_pixel(block) for block in row] for row in blocks]
#     return output

# def find_dominant_color(filename):
#     #Resizing parameters
#     width, height = 150,150
#     image = Image.open(filename)
#     image = image.resize((width, height),resample = 0)
#     #Get colors from image object
#     pixels = image.getcolors(width * height)
#     #Sort them by count number(first element of tuple)
#     sorted_pixels = sorted(pixels, key=lambda t: t[0])
#     #Get the most frequent color
#     dominant_color = sorted_pixels[-1][1]
#     return dominant_color

champion_name = helper_functions.get_champion_name()

# version = helper_functions.get_latest_version()
# champions = helper_functions.get_champion_data()
champion_names = helper_functions.get_champion_names()

if(not helper_functions.validate_arguments(champion_name, champion_names)):
    print('Incorrect argument.')
    quit()

helper_functions.get_champion_image(champion_name)
helper_functions.print_image(champion_name)
helper_functions.print_champion_info(champion_name)

# champion_name = input('Name of the champion?\n')
# get_champion_icon.get_image(champion_name)
# get_champion          
# champion = current_champ_list[champion_name]

# version = champion['version']
# id = champion['id']
# key = champion['key']
# name = champion['name']
# title = champion['title']
# blurb = champion['blurb']
# info = champion['info']
# image = champion['image']
# tags = champion['tags']
# partype = champion['partype']
# stats = champion['stats']

# for champ in current_champ_list:
#     print(champ)

# # print(version + "\n" + id + "\n" + key + "\n" + name + ", " + title + "\n" + blurb + "\n" + info + "\n" + image + "\n" + tags + "\n" + partype + "\n" + stats + "\n")
# print(name + ", " + title + "\n" + blurb + "\n" + stats + "\n")

# domcol = find_dominant_color(champion_name + '.png')
# print(domcol)
# image = np.asarray(Image.open(champion_name + '.png'))
# output = render_image(image, (20, 20))
# print('\n'.join([''.join(row) for row in output]))

# os.remove(champion_name + '.png') 