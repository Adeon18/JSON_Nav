'''
A main script that handles all the inputs
'''
import json
import sys

from helpers import *


def main():
    '''
    This is a main function. There's is a while loop that reads a file and
    gives you an option choice
    '''
    print('---------------')
    print('Starting...')
    answer = input('Give the .json file path: ')
    print('---------------')

    data = read_file(answer)
    while True:
        if isinstance(data, dict):
            data = handle_obj_keys(data)

        elif isinstance(data, list):
            data = list_content_handle(data)
        
        else:
            print(data)
            break


def handle_obj_keys(obj: dict):
    '''
    Responsible for the object data handling. And all the questions regarding
    that object.
    '''
    print('---------------')
    print('This is an object. Here are all the avalible keys:')
    for key in obj.keys():
        print(key, flush=True)
    print('---------------')
    # The while loop which allows you to access all the keys
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
    '''
    Responsible for the list data handling. And all the questions regarding
    that list.
    '''
    while True:
        answer = input(f'This is a list. Print all the {len(lst)} options?(y is usually a bad idea) (y/n) ')
        try:
            # Yes options
            if answer == 'y':
                for i, option in enumerate(lst):
                    print(f'{option}', flush=True, end=' ')
                    print(f'\033[1;32;40m [{i}] \033[0m')

                yes_answer = input('Choose an option index: ')
                if isinstance(int(yes_answer), int):
                    return lst[int(yes_answer)]

            # No option
            elif answer == 'n':
                no_answer = input(f'Choose an option index: ')
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