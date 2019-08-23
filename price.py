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
engine.setProperty('rate', rate - 20)

class shirts:
    class T_shirts:
        def polo(self):
            engine.say("the price of the polo is five thousand naira")
            engine.runAndWait()
    class shirt:
        def short(self):
            engine.say("the price of the short sleeve is seven thousand, five hundred naira")
            engine.runAndWait()
        def long(self):
            engine.say("the price of the long sleeve is ten thousand naira")
            engine.runAndWait()
class trousers:
    class jeans:
        def shorts(self):
            engine.say("the price of the jeans short is eight thousand naira")
            engine.runAndWait()
        def long(self):
            engine.say("the price of the jeans trouser is ten thousand naira")
            engine.runAndWait()
        def crazy(self):
            engine.say("the price of the crazy jeans is seven thousand naira")
            engine.runAndWait()
        def skirt(self):
            engine.say("the price of the jeans skirt is nine thousand naira")
            engine.runAndWait()
    class trouser:
        def black(self):
            engine.say("the price of the black trouser is six thousand naira")
            engine.runAndWait()
        def blue(self):
            engine.say("the price of the blue trouser is eight thousand naira")
            engine.runAndWait()
        def sweat(self):
            engine.say("the price of the sweat pants is nine thousand naira")
            engine.runAndWait()
        def skirt(self):
            engine.say("the price of the skirt is five thousand naira")
            engine.runAndWait()
class suit:
    class male:
        def blue(self):
            engine.say("the price of the blue suit is thirty thousand naira")
            engine.runAndWait()
        def black(self):
            engine.say("the price of the black suit is twenty seven thousand naira")
            engine.runAndWait()
        def white(self):
            engine.say("the price of the white suit is thirty four thousand naira")
            engine.runAndWait()
        def grey(self):
            engine.say("the price of the grey suit is thirty two thousand naira")
            engine.runAndWait()

    class female:
        def blue(self):
            engine.say("the price of the blue suit is 27000 naira")
            engine.runAndWait()

        def black(self):
            engine.say("the price of the black suit is 28000 naira")
            engine.runAndWait()

        def white(self):
            engine.say("the price of the white suit is 32000 naira")
            engine.runAndWait()
        def grey(self):
            engine.say("the price of the grey suit is 29000 naira")
            engine.runAndWait()
