import pyttsx3

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
engine.setProperty('rate', rate - 18)

class menClothes:
    def shirts(self):
        engine.say("The Section for male shirts is at Stand 15")
        engine.runAndWait()

    def trousers(self):
        engine.say("The Section for male trousers is at Stand 16")
        engine.runAndWait()

    def suit(self):
        engine.say("The Section for male Suit is at Stand 17")
        engine.runAndWait()


class womenClothes:
    def shirts(self):
        engine.say("The Section for female shirts is at Stand 7")
        engine.runAndWait()

    def trousers(self):
        engine.say("The Section for female trousers is at Stand 9")
        engine.runAndWait()

    def suit(self):
        engine.say("The Section for female Suit is at Stand 8")
        engine.runAndWait()

    def skirt(self):
        engine.say("The section for skirts is at Stand 10")

class bakery:
    def bakery(self):
        engine.say("The section for the bakery is a Stand 20")

class wines:
    def alcoholic(self):
        engine.say("The Section for alcoholic wine is at stand 3")
        engine.runAndWait()

    def fruit(self):
        engine.say("The section for fruit wine is at stand 4")
        engine.runAndWait()

class fruitandveg:
    def fruit(self):
        engine.say("the section for fruits is at stand 12")
        engine.runAndWait()

    def veg(self):
        engine.say("the section for vegetables is at stand 13")
        engine.runAndWait()

class drinks:
    def alcoholic(self):
        engine.say("the section for alcoholic drinks is at stand 5")
        engine.runAndWait()

    def soft(self):
        engine.say("the section for soft drinks is at stand 2")
        engine.runAndWait()

    def energy(self):
        engine.say("the section for energy drinks is at stand 6")
        engine.runAndWait()

class ijekuje:
    def candy(self):
        engine.say("the section for candies is at stand 1")
        engine.runAndWait()

    def icecream(self):
        engine.say("the section for ice creams is at stand 11")
        engine.runAndWait()

    def pizza(self):
        engine.say("the section for pizza is at stand 19")
        engine.runAndWait()

class prov:
    def milk(self):
        engine.say("the section for milk is at stand 14")
        engine.runAndWait()

    def cereals(self):
        engine.say("the section for cereals is at stand 18")
