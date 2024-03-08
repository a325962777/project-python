from girl import Girl
from boy import Boy

class Manager:
    """"Manages the information database about the singles and its update"""

    def __init__(self):
        """"The function creates a complex dictionary that contains boys and girls by reading from a file"""
        self.dict = {'boys': {}, 'girls': {}}
        fullName = lambda firstName, lastName: firstName + " " + lastName
        fileGirls = open('girlsFile.txt', 'r')
        for girl in fileGirls.readlines():
            arr = girl.split(',')
            g = Girl(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
            fl = fullName(g.firstName, g.lastName)
            self.dict.get("girls").update({fl: g})
        fileBoys = open('boysFile.txt', 'r')
        for boy in fileBoys.readlines():
            arr = boy.split(',')
            b = Boy(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
            fl = fullName(b.firstName, b.lastName)
            self.dict.get("boys").update({fl: b})

    def add(self, person):
        """"Added boy or girl to the dictionary"""
        fullName = lambda firstName, lastName: firstName + " " + lastName
        fl = fullName(person.firstName, person.lastName)
        if isinstance(person, Boy):
            self.dict['boys'].update({fl: person})
        else:
            self.dict['girls'].update({fl: person})
        self.list()

    def delete(self, name):
        """"Deleted boy or girl from the dictionary"""
        try:
            if(name in self.dict['girls']):
                del self.dict['girls'][name]
            else:
                del self.dict['boys'][name]
            self.list()
        except:
            print("The requested boy or girl does not exist")

    def checkIsNumber(self, number, question):
        """"The function checks whether the input is of type number"""
        flag= False
        while flag!= True:
            try:
                x = int(number)
                flag= True
            except:
                print("The input is not correct")
                number= input(question)
        return number

    def createGirl(self):
        firstName = input("First name is: ")
        lastName = input("Last name is:")
        age = input("Age: ")
        age=self.checkIsNumber(age, "Age: ")
        height = input("Height: ")
        height=self.checkIsNumber(height, "Height: ")
        sector = input("sector: to litahi click-l, sfaradi click-s, chasidi click-c")
        talentLabel = input("Talent level rating from 1 to 10")
        strikingCharacterTrait = input("Insert a salient character trait")
        seminar = input("Place of study- seminar:")
        financial = input("Amount of financial participation by the parents:")
        financial=self.checkIsNumber(financial, "Amount of financial participation by the parents:")
        g= Girl(firstName, lastName, age, height, sector, talentLabel, strikingCharacterTrait, seminar, financial)
        return g

    def createBoy(self):
        firstName = input("First name is: ")
        lastName = input("Last name is:")
        age = input("Age: ")
        age=self.checkIsNumber(age, "Age: ")
        height = input("Height: ")
        height=self.checkIsNumber(height, "Height: ")
        sector = input("sector: to litahi click-l, sfaradi click-s, chasidi click-c")
        talentLabel = input("Talent level rating from 1 to 10")
        strikingCharacterTrait = input("Insert a salient character trait")
        yeshiva = input("Place of study- yeshiva:")
        financial = input("Financicial requirement:")
        financial=self.checkIsNumber(financial, "Financicial requirement:")
        b= Boy(firstName, lastName, age, height, sector, talentLabel, strikingCharacterTrait, yeshiva, financial)
        print(f"✔✔✔")
        return b

    def list(self):
        arr1=[i for i in self.dict['girls'].keys()]
        arr2=[i for i in self.dict['boys'].keys()]
        print(f"girls: {arr1}, boys: {arr2}")
