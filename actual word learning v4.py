#import nltk
#nltk not being used yet

#these files are the necessary imports
import pynput
import random
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller

#setting up key variables
variable = 1 #the number in the alphabet of the letter
previouskey = -1 #remembers what the previous key that was presssed
previousvariable = 0 #previous number of the letter in the alphabet
enter = 0 #will be used to recognize when the most probable letter will be used

#error in the code is that they are all pasting into the letters0
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters0 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters1 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters2 = [['a',letters0],['b',letters0],['c',letters0],['d',letters0],['e',letters0],['f',letters0],['g',letters0],['h',letters0],['i',letters0],['j',letters0],['k',letters0],['l',letters0],['m',letters0],['n',letters0],['o',letters0],['p',letters0],['q',letters0],['r',letters0],['s',letters0],['t',letters0],['u',letters0],['v',letters0],['w',letters0],['x',letters0],['y',letters0],['z',letters0]]

def most_used(previousvariable):
    x = 0
    y = 1
    while y <= 25:
        if letters2[previousvariable][1][x][1] < letters2[previousvariable][1][y][1]:
            x = y
            y = y + 1
        elif letters2[previousvariable][1][x][1] > letters2[previousvariable][1][y][1]:
            x = x
            y = y + 1
        else:
            x = x + 1
            y = y + 1
    return x

def generated_letter(previousvariable):
    letter_number = most_used(previousvariable)
    Controller().press(keyboard.KeyCode.from_char(letters2[previousvariable][1][letter_number][0]))

def number_of_letters(): #prints out all of the letters in the alphabet plus the total number of times they have been pressed
    global objects
    objects = -1
    for i in letters1:
        objects = objects + 1
        a = i[0]
        b = letters1[objects][1]
        print(a)
        print(b)
        
def appender(variable1): #increased the number of times 1 letter has been pressed by 1
    letters1[variable1][1] = letters1[variable1][1] + 1

def appender1(previousvariable,variable1): #increases the number of times 1 letter has been pressed after a certain letter
    letters2[previousvariable][1][variable1][1] = letters2[previousvariable][1][variable1][1] + 1
    print(previousvariable)
    
def on_press(key): #everything that happens after a key was pressed
    global enter
    global variable
    global variable1
    global previouskey
    global previousvariable
    variable1 = 0
    variable = -1
    
#this part is for use when after shift has been pressed meaning that the user want a generated letter this will eventually give that letter
    #TBF
    '''if enter == "was pressed":
        print('hello1')
        if key == Key.right:
            print('ye')'''
    
#this uses the pressed key and prints it out
    print("{0} pressed".format(key))

#this part recognizes if the key that was pressed is a letter in the alphabet 
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
    previousvariable = variable1 #resets previousvariable
    
    
    
def on_release(key): #everythin that happens once a key was released
    global enter
    global answer
    answer = 0
    '''if key == Key.right:
        print('yo')'''
    if key == Key.esc: #termination sequence and presentation of data
        number_of_letters()
        answer = int(input('do you want to see any of the number of letters in any of the letters2 file? Y = 0 N = 1: '))
        while answer == 0:
            localvariable = int(input('letter number of first letter: '))
            localvariable2 = int(input('letter number of second letter: '))
            print('variable 1 is', localvariable)
            print('variable 2 is', localvariable2)
            print('letter section entered:', letters2[localvariable][1][localvariable2][0],'\n''values in section:', letters2[localvariable][1][localvariable2][1])
            answer = int(input('go again? Y = 0 N = 1: '))
        print("terminating program")
        return False
    
    elif key == Key.shift: #start of proecess of the letter generation
        if key == Key.shift:
            enter = "was pressed"
            print('hello')
        if previouskey != -1:
            word = int(input('1/0 (Y/N) do you want autofil?'))
            if word == 1:
                print('starting')
                generated_letter(previousvariable)
                print('accomplished')
            else:
                print('moving on...')

        elif previouskey == -1:
            print('there is nothing to be done so far')
            
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
    
#print(letters1[1][1][0])
