import json
import sys

from helpers import *


def main():
    data = read_file("data/frienfs_list_Obama.json")
    while True:
        if isinstance(data, dict):
            data = print_obj_keys(data)

        elif isinstance(data, list):
            data = list_content_handle(data)
        
        else:
            print(data)
            break


def print_obj_keys(obj: dict):

    print('Here are all the awalible keys:')
    for key in obj.keys():
        print(key, flush=True)
    print('---------------')
    
    while True:
        try:
            answer = input('Choose a key: ')
            if isinstance(obj[answer], (list, dict)):
                return obj[answer]
            else:
                print(obj[answer])

        except KeyError:
            print('Wrong key, try again')
    # Exit or continue choosing keys?
        exit_answer = input('Exit? (y/n) ')
        if exit_answer == 'y':
            sys.exit()
        else:
            pass




def list_content_handle(lst: list):

    while True:
        answer = input(f'This is a list. Print all the {len(lst)} options? (y/n)')
        try:
            # Yes options
            if answer == 'y':
                for i, option in enumerate(lst):
                    print(f'{option} [{i}]', flush=True)

                yes_answer = input('Choose an option index: ')
                if isinstance(int(yes_answer), int):
                    return lst[int(yes_answer)]

            # No option
            elif answer == 'n':
                no_answer = input(f'What is the index of the wanted item? (int)')
                # if isinstance(answer_2, int):
                #     for i in range(answer_2):
                #         print(f'{lst[i]} [{i}]', flush=True)
                # no_answer = input('Choose an option index: ')
                if isinstance(int(no_answer), int):
                    return lst[int(no_answer)]
            else:
                pass
        except:
            print('Wrong input, try again')


main()