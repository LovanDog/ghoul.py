##1000-7
from time import sleep

ghoul = 1000

while True:
    wasghoul = ghoul
    ghoul = ghoul - 7

    print(f'{wasghoul} - 7 = {ghoul}')
    sleep(0.05)

    if ghoul < 0:
        print('I am... a ghoul')
        break
