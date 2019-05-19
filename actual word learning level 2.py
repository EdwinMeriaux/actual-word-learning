#import nltk
#nltk not being used yet

import pynput
import random
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller

variable = 1
previouskey = -1
previousvariable = 0

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters0 = [['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z']]
letters1 = [['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z']]
letters2 = [['a',letters0],['b',letters0],['c',letters0],['d',letters0],['e',letters0],['f',letters0],['g',letters0],['h',letters0],['i',letters0],['j',letters0],['k',letters0],['l',letters0],['m',letters0],['n',letters0],['o',letters0],['p',letters0],['q',letters0],['r',letters0],['s',letters0],['t',letters0],['u',letters0],['v',letters0],['w',letters0],['x',letters0],['y',letters0],['z',letters0]]

def number_of_letters():
    global objects
    objects = -1
    for i in letters1:
        objects = objects + 1
        a = i[0]
        b = len(letters1[objects])-1
        print(a)
        print(b)
        
def appender(variable1):
    letters1[variable1].append(letters[variable1])

def appender1(previousvariable,variable1):
    letters2[previousvariable][1][variable1].append(letters[variable1])
    print(previousvariable)
    
def on_press(key):
    global variable
    global variable1
    global previouskey
    global previousvariable
    variable1 = 0
    variable = -1
    
    print("{0} pressed".format(key))
    for i in letters1:
        variable = variable + 1
        a = i[0]
        if key == keyboard.KeyCode.from_char(a):
            variable1 = variable
            appender(variable1)
            if previouskey != -1:
                appender1(previousvariable,variable1)
            if key == keyboard.KeyCode.from_char(a):
                previouskey = key
    previousvariable = variable1
    
def on_release(key):
    global answer
    answer = 0
    if key == Key.esc:
        number_of_letters()
        answer = int(input('do you want to see any of the number of letters in any of the letters2 file? Y = 0 N = 1: '))
        while answer == 0:
            localvariable = int(input('letter number of first letter: '))
            localvariable2 = int(input('letter number of second letter: '))
            print('variable 1 is', localvariable)
            print('variable 2 is', localvariable2)
            print('letter section entered:', letters2[localvariable][1][localvariable2][0], 'values in section', letters2[localvariable][1][localvariable2][1:])
            answer = int(input('go again? Y = 0 N = 1: '))
        print("terminating program")
        return False
    elif key == Key.enter:
        #print('hello')
        if previouskey != -1:
            #print('hello1')
            pass

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
    
#print(letters1[1][1][0])