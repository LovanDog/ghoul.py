##1000-7
from time import sleep

ghoul = 1000

for x in range(143):
    wasghoul = ghoul
    ghoul = ghoul - 7
    print(f'{wasghoul} - 7 = {ghoul}')
    sleep(0.1)
    if ghoul == -1:
        print('I am... a ghoul')
