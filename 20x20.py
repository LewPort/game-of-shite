#!/usr/bin/env python3

import random
import time

env = {}

def resetenv(env):
    for y in range(0, 21):
        for x in range(0, 21):
            env[x, y] = ' '

def printenv(env):
    for x in range(0, 21):
        for y in range(0, 21):
            print('|' + str(env[x, y]), end='')
        print('|')
    print('\n')

def randomO(bot, env):
    x = (random.randint(0, 20))
    y = (random.randint(0, 20))
    env[x, y] = bot
    

def moveO(bot, bot2, env):
    for x, y in env:
        if env[x, y] == bot:                      
            
            #movement rules
            if x == 0:
                env[x, y] = ' '
                x += (random.randint(0, 1))
            elif y == 0:
                env[x, y] = ' '
                y += (random.randint(0, 1))
            elif x == 20:
                env[x, y] = ' '
                x += (random.randint(-1, 0))
            elif y == 20:
                env[x, y] = ' '
                y += (random.randint(-1, 0))
            else:
                env[x, y] = ' '
                x += (random.randint(-1, 1))
                y += (random.randint(-1, 1))
            env[x, y] = bot

            try:
                for xsearch in range(-1, 1):
                    for ysearch in range(-1, 1):
                        if env[(x+xsearch), (y+ysearch)] == bot2:
                            randomO((random.choice(['O', '0'])), env)
            except KeyError: continue
            break
        
    
            

resetenv(env)
randomO('O', env)
randomO('0', env)

frame = 1
while True:
    printenv(env)
    print('Frame: %d' % frame)
    frame += 1
    moveO('O', '0', env)
    moveO('0', 'O', env)
    time.sleep(0.1)
    
    
