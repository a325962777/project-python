from girl import Girl
from boy import Boy
import itertools as it
import playsound

class Create_Shiduch:
    # def __init__(self):
    #     pass

    def match(self, boy, girl):
        """"Compatibility Test"""
        a=int(boy.age)
        b=int(girl.age)
        if abs(a-b) > 2:
            return False
        elif int(girl.financiallyParticipation)< int(boy.financiallyrequirement):
            return False
        elif int(girl.height) - int(boy.height) > 5 or int(boy.height) - int(girl.height) > 15:
            return False
        elif girl.sector != boy.sector:
            return False
        return True

    def sucsses(self,nameBoy, nameGirl):
        """"If the boy and girl matched and the SHIDUCH succeeded"""
        print(f"{nameBoy} & {nameGirl}, mazal-tov!!")
        playsound.playsound('music/02 בשעה טובה.mp3')

