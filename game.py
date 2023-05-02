ChooseEth = input('Choose ethnicity (White, Black, Chinese) or, type Controls to see the controls, or type Cheats to bring up the cheat menu!')
import random


White = False
Black = False
Chinese = False

if ChooseEth == 'White':
    SlaveW = input('You have enslaved a white guy named Earl! ')
    White = True
    if SlaveW == 'Beat':
        print('You have beat your slave to a pulp! He is badly injured.')
    if SlaveW == 'Work':
        print('You have commanded your slave to work!')
    if SlaveW == 'Feed':
        print('You have fed your slave!')
    if SlaveW == 'Shoot':
        print('You have shot your slave and he has died!')
    if SlaveW == 'Release':
        print('You have let your slave go into the wild!')

if ChooseEth == 'Black':
    SlaveB = input('You have enslaved a black guy named Tyrone! ')
    Black = True
    if SlaveB == 'Beat':
        print('You have beat your slave to a pulp! He is badly injured!')
    if SlaveB == 'Work':
        print('You have commanded your slave to work!')
    if SlaveB == 'Feed':
        print('You have fed your slave!')
    if SlaveB == 'Shoot':
        print('You have shot your slave and he has died!')
    if SlaveB == 'Release':
        print('You have let your slave go into the wild!')
if ChooseEth == 'Chinese':
    SlaveC = input('You have enslaved a chinese guy named Chong Bing Chow')
    Chinese = True
    if SlaveC == 'Beat':
        print('You have beat you slave to a pulp! He is badly injured!')
    if SlaveC == 'Work':
        print('you have commanded your slave to work!')
    if SlaveC == 'Feed':
        print('You have fed your slave!')
    if SlaveC == 'Shoot':
        print('You have shot your slave and he has died!')
    if SlaveC == 'Release':
        print('You have let your slave go into the wild!')
    
if ChooseEth == 'Controls':
    print('Here is a list of what you can do: Beat, Work, Feed, Shoot, Release')
    
if ChooseEth == 'Cheats':
    CheatMenu = input('Enter cheat:')
