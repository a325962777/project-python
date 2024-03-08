from girl import Girl
from boy import Boy
from create_shiduch import Create_Shiduch
from manager import Manager
import pprint

def genderInput():
    try:
        gender = input("insert b to boy, or g to girl")
        if gender != 'b' and gender != 'g':
            raise TypeError('incorrect input')
    except Exception as e:
        print(e)
        gender = input("insert b to boy, or g to girl")
    return gender

manager = Manager()
createShiduch = Create_Shiduch()
choiceInput = ''
while choiceInput != 'stop':
    print("-----------------------------------")
    choiceInput = input(f"Welcome to SHIDUCHIM site!😏😜😁\nif you want to create a shiduch: click 1,\nto add boy or girl to database: click 2,\nto delete boy or from database: click 3,\nto exit: write stop")
    try:
        if choiceInput == '1':
            print("In this program, the data of the intended boy or girl will be defined by you and we will adjust "
                  "the most suitable match for them")
            flagFindShiduch = False
            gender = genderInput()
            if gender == 'g':
                girl = manager.createGirl()
                for b in manager.dict['boys'].values():
                    if createShiduch.match(b, girl):
                        print("The match boy is: ")
                        b.print()
                        print("------------")
                        create = input("if you want create shiduch- click yes, else- click no")
                        if create == "yes":
                            flagFindShiduch = True
                            fullName = lambda firstName, lastName: firstName + " " + lastName
                            fl = fullName(b.firstName, b.lastName)
                            fl2 = fullName(girl.firstName, girl.lastName)
                            createShiduch.sucsses(fl, fl2)
                            manager.delete(fl)
                            break
            else:
                boy = manager.createBoy()
                for girl in manager.dict['girls'].values():
                    if createShiduch.match(boy, girl) == True:
                        print("The match girl is: ")
                        girl.print()
                        print("------------")
                        create = input("if you want create shiduch- click yes, else- click no")
                        if (create == "yes"):
                            flagFindShiduch = True
                            fullName = lambda firstName, lastName: firstName + " " + lastName
                            fl = fullName(boy.firstName, boy.lastName)
                            fl2 = fullName(girl.firstName, girl.lastName)
                            createShiduch.sucsses(fl, fl2)
                            manager.delete(fl2)
                            break
            if flagFindShiduch == False:
                print("No match was found for the intended")
        elif choiceInput == '2':
            gender = genderInput()
            if gender == 'g':
                girl = manager.createGirl()
                manager.add(girl)
            else:
                boy = manager.createBoy()
                manager.add(boy)
            print("The data was successfully captured")
        elif choiceInput == '3':
            gender = genderInput()
            if gender == 'g':
                girl = manager.createGirl()
                manager.delete(girl.firstName + " " + girl.lastName)
            else:
                boy = manager.createBoy()
                manager.delete(boy.firstName + " " + boy.lastName)
    except:
        print("The click is incorrect")
