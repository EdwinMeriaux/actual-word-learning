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

#error in the code is that they are all pasting into the letters0 (possibly fixed with the many diferent leters00)
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

letters00 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters01 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters02 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters03 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters04 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters05 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters06 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters07 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters08 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters09 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters10 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters11 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters12 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters13 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters14 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters15 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters16 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters17 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters18 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters19 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters20 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters21 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters22 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters23 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters24 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters25 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]


letters1 = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
letters2 = [['a',letters00],['b',letters01],['c',letters02],['d',letters03],['e',letters04],['f',letters05],['g',letters06],['h',letters07],['i',letters08],['j',letters09],['k',letters10],['l',letters11],['m',letters12],['n',letters13],['o',letters14],['p',letters15],['q',letters16],['r',letters17],['s',letters18],['t',letters19],['u',letters20],['v',letters21],['w',letters22],['x',letters23],['y',letters24],['z',letters25]]

order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
maxmin = []
maxmin2 = []
order2 = []

def most_used():
    global previousvariable
    print('previousvariable')
    print(previousvariable)
    #previousvariable = 1
    global order2
    global maxmin2
    order2 = order
    maxmin2 = maxmin
    while len(maxmin2) < 26:
        x = 0
        y = x + 1
        x1 = order2[x]
        y1 = order2[y]
        while y <= len(order2)-1:
            x1 = order2[x]
            y1 = order2[y]
            if letters2[previousvariable][1][x1][1] < letters2[previousvariable][1][y1][1]:
                x = y
                y = y + 1
            elif letters2[previousvariable][1][x1][1] >= letters2[previousvariable][1][y1][1]:
                y = y + 1
            else:
                print('aaaaaah')
            '''print(x)
            print(y)'''
        print(x1)
        maxmin2.append(order2[x])
        order2.pop(x)
        
        if len(maxmin2) == 25:
            maxmin2.append(order2[0])
            order.pop(0)

def generated_letter():
    most_used()
    Controller().press(keyboard.KeyCode.from_char(letters2[previousvariable][1][maxmin2[0]][0]))

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
                generated_letter()
                print('accomplished')
            else:
                print('moving on...')

        elif previouskey == -1:
            print('there is nothing to be done so far')
            
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
    
#print(letters1[1][1][0])