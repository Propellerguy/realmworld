import datetime
import random
import sys

def greetz():
    date = datetime.datetime.now()

    if (date.year > 2032) and (not random.randint(0,999)):
        return 'Holy cow, people still PLAY this game?!'
    if (random.randint(1,1000000) == 75586):
        return 'OH MY GOSH - a ninja outside the window!\n - Oh - he\'s gone.'
    if (sys.platform == 'riscos') and (random.randint(1,10000) == 36):
        return 'The same sort of strange person who uses RISC OS would play this game.\nYou are that strange person.\nCongratulations.'
    if (sys.platform.startswith('win')) and (random.randint(1,100000) == 8):
        return 'Please throw your computer out the window.\nThank you.'
    if random.randint(1,10000000) == random.randint(1,10000000):
        return 'The odds of getting this message are so low that you should have spent that\nluck playing the lottery. Ooops.'
    if (date.month == 12) and (date.day == 25):
        return 'Merry Christmas!'
    if (date.month == 1) and (date.day == 1):
        return 'Happy New Year.'
    if (date.month == 4) and (date.day == 1):
        return [
            'ALL UR BASE R BELONG 2 US - APRLFLZ',
            'Your computer has been hacked by someone. Please\nplace head against keyboard and cry.\nThank you.',
            'Happy April Fools. That is, if YOU are happy.'
        ][date.year%3]
    if (date.month == 7) and (date.day == 13):
        return 'It is Propellerguy\'s birthday today!'
    if (date.hour >= 18):
        return 'Good evening.'
    if (date.hour < 11):
        return 'Good morning.'
    if (date.hour == 0) and (date.minute == 0) and (date.second == 0):
        return 'It is the stroke of midnight. I hope this computer wasn\'t a present\nfrom a fairy godmother.'
    return 'Hello!'