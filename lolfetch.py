import helper_functions as hf

champion_name = hf.get_champion_name()
champion_names = hf.get_champion_names()

if(not hf.validate_arguments(champion_name, champion_names)):
    print('Incorrect argument.')
    quit()

hf.get_champion_image(champion_name)
# hf.print_image()
# hf.print_champion_info(champion_name)
hf.print_combined(champion_name)
hf.remove_image()

# TODO better image source
# TODO ideas to display champion infos and tags (emojis)
# TODO add functionality for random argument (-r)
