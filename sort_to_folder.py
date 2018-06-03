#!python3

import os
import re
from time import sleep
import shutil

bad_symbols = '#%&{}\\<>*&?/$!\'":@'


def single_out_files(path, keyword):
    regex = re.compile(keyword, re.IGNORECASE)
    files = os.listdir(path)
    matched_files = [x for x in files if re.search(regex, x)]
    return matched_files


def get_user_keyword():
    while True:
        keyword = input('Now enter a key word by which you want to single out files:\n')
        if re.match(bad_symbols, keyword):
            print('Sorry, but your input contains one of this forbidden characters: #%&{}\\<>*&?/$!\'":@')
            print('Try again without them.')
            continue
        print(f'Gotcha! Your keyword is >> {keyword} <<')
        return keyword


def copy(files, keyword):
    new_folder = os.path.join(path_to_work, keyword)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    for file in files:
        print(f'Copying {file}...')
        new_path_to_file = os.path.join(new_folder, file)
        if os.path.exists(new_path_to_file):
            print(f'File named {file} already exists in the folder {keyword}')
            print('Skip it and go to next file.')
            continue
        shutil.copy(os.path.join(path_to_work, file), new_path_to_file)
    print(f'Work is done. Your files in {new_folder}')
    exit()


def handle_results(files, keyword):
    if len(files) < 1:
        answ = input('Unfortunately there is 0 files that match you keyword. '
                     'Would you like to try another keyword? y/n: ')
        while True:
            if answ.lower() == 'y':
                keyword = get_user_keyword()
                files = single_out_files(path_to_work, keyword)
                handle_results(files)
            elif answ.lower() == 'n':
                print('Ciao!')
                exit()
            else:
                print('Wrong input. Try again.')
    else:
        print(f'There are {len(founded_files)} files that match your keyword:')
        for file in files:
            print(file)
        answ = input('Would you like to copy them to a new folder? y/n: ')
        while True:
            if answ == 'y':
                print(f'OK! Start copy to folder named {keyword}')
                copy(files, keyword)
                break
            elif answ == 'n':
                print('Good luck!')
                exit()
            else:
                print('Wrong input. Try again.')


print('Hi! This little scrip will help you to single out files by some key word and copy them in the separate folder.')
while True:
    path_to_work = input('Type in here path to folder to work:\n')
    if not os.path.exists(path_to_work):
        print('This path doesn\'t exist. Try another one.')
        continue
    break

user_keyword = get_user_keyword()

print('Start searching in 5...')
for i in range(4, 0, -1):
    sleep(1)
    print(f'{i}...')

sleep(1)
print('BANG!!!!')
sleep(2)
print('Just kidding :). Now really start searching...')
sleep(2)

founded_files = single_out_files(path_to_work, user_keyword)
handle_results(founded_files, user_keyword)








