import time
from webbrowser import open as op

from pyautogui import hotkey, locateOnScreen, useImageNotFoundException

import os
from dotenv import load_dotenv
from colors import bcolors

print(f'{bcolors.HEADER}STARTING WHATSAPP NUMBER CHECKER...')

load_dotenv()

useImageNotFoundException()
country_code = os.getenv('COUNTRY_CODE')

def change_country_code(country_code:str):
    os.environ['COUNTRY_CODE']   = country_code
    print(f'{bcolors.BOLD}Country Code updated Succesfully')

def check(country_code):

    file = input(f'{bcolors.OKGREEN}Enter path of TXT File : ')

    with open(file, 'r') as f:
        nos = f.readlines()

    available = []

    total = len(nos)
    print(f"{bcolors.OKBLUE}Total numbers to check : ", total)

    # count = 0

    for num in nos:

        op(f'https://web.whatsapp.com/send?phone={int(country_code + num)}&text&app_absent=0')
        time.sleep(10)


        try:
            a=locateOnScreen('valid.png')
            available.append(num)
            # print("Available")
        except Exception:
            try:
                locateOnScreen('invalid.png')
                # print("Unvailble")
            except Exception:
                # print("Coundn't Verify")
                pass

        hotkey('Ctrl', 'w')
        # count = count + 1
        # print(f'{bcolors.ENDC}PROGRESS : {count}/{total}', end='\r')

    with open('output.txt', 'w') as f:
        f.writelines(available)

check(country_code)

print(f'{bcolors.BOLD}Successfully completed checking')
os.system('output.txt')