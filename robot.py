from tkinter import*
from locate import*
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from price import*
import pyttsx3
porter = PorterStemmer()


#setting up the voice engine
engine = pyttsx3.init()

# voice type
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)

# rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)

#global variables
z = ""
maleShirt = menClothes()
femaleShirt = womenClothes()
bake = bakery()
wine = wines()
fv = fruitandveg()
dr = drinks()
ij = ijekuje()
pr = prov()
Tsh = shirts.T_shirts()
sh = shirts.shirt()
jean = trousers.jeans()
tr = trousers.trouser()
mst = suit.male()
fmt = suit.female()

#tokenize and stem human reply
def stemReply(x):
    token_word = word_tokenize(x)
    stem_x = []

    for word in token_word:
        stem_x.append(porter.stem(word))
        stem_x.append(" ")

    return "".join(stem_x)



def locate():
    engine.say("What do you want to buy?")
    engine.runAndWait()
    global x
    z = input()
    stemReply(z)
    x = z.lower()
    element = x.split(" ")
    inp = []
    for i in range(len(element)):
        inp.append(str(element[i].strip()))

    #class clothes
    if 'trousers' in inp or "trouser" in inp:
        if 'male' in inp:
            maleShirt.trousers()
        elif 'female' in inp:
            femaleShirt.trousers()
        else:
            engine.say("Do you mean male trousers or female trousers?")
            engine.runAndWait()
    elif 'suits' in inp:
        if 'male' in inp:
            maleShirt.suit()
        elif 'female' in inp:
            femaleShirt.suit()
        else:
            engine.say("Do you mean male suits or female suits?")
            engine.runAndWait()
    elif 'shirts' in inp or 'shirt' in inp:
        if 'female' in inp:
            femaleShirt.shirts()
        elif 'male' in inp:
            maleShirt.shirts()
        else:
            engine.say("Do you mean male shirts or female shirts?")
            engine.runAndWait()
    elif 'skirts' in inp:
        femaleShirt.skirt()


    #bakery
    elif 'bread' in inp:
        bake.bakery()

    #wines
    elif 'wine' in inp:
        if 'alcoholic' in inp:
            wine.alcoholic()
        elif 'fruit' in inp:
            wine.fruit()
        else:
            engine.say('Do you mean fruit wine or alcoholic wine?')
            engine.runAndWait()

    #fruits and vegetables
    elif 'fruits' in inp:
        fv.fruit()
    elif 'vegetables' in inp:
        fv.veg()

    #drinks
    elif 'drinks' in inp:
        if 'alcoholic' in inp:
            dr.alcoholic()
        elif 'energy' in inp:
            dr.energy()
        elif 'soft' in inp:
            dr.soft()
        else:
            engine.say('Do you mean soft drinks or energy drinks or alcoholic drinks')

    else:
        engine.say("Okay, I wasn't programmed to answer that.")
        engine.runAndWait()
        return
def price():
    engine.say("Which Item will you like to purchase")
    engine.runAndWait()
    global x
    z = input()
    stemReply(z)
    x = z.lower()
    element = x.split(" ")
    inp = []
    for i in range(len(element)):
        inp.append(str(element[i].strip()))

    #price of clothes
    if 'polo' in inp:
        Tsh.polo()
    elif 'short sleeve' in inp:
        sh.short()
    elif 'long sleeve' in inp:
        sh.long()



engine.say("Hi, I am the mall robot. Do you want to buy something")
engine.runAndWait()
y = input()

while y == "yes":
    locate()
    break

engine.say("Will you like to know the price of the item you want to purchase")
engine.runAndWait()
b = input()
while b == "yes":
    price()
    break


while b == 'yes':
    engine.say("Do you want to buy something else")
    engine.runAndWait()
    c = input()
    while c == 'yes':
        locate()
        engine.say("Will you like to know the price of the item you want to purchase")
        engine.runAndWait()
        b = input()
        while b == "yes":
            price()
            break
        break

