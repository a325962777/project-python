from Person import Person

class Boy (Person):
    def __init__(self, firstName, lastName, age, height, sector, talentLevel,
                 strikingCharacterTrait, yeshiva, financiallyrequirement):
        super(Boy, self).__init__(firstName, lastName, age, height, sector, talentLevel, strikingCharacterTrait)
        self.yeshiva = yeshiva
        self.financiallyrequirement = financiallyrequirement

    def print(self):
        print(f"The name is: {self.firstName} {self.lastName}")
        print(f"age: {self.age}, hight: {self.height}, sector: {self.sector}")
        print(f"talent level: {self.talentLevel}, striking character trait: {self.strikingCharacterTrait}")
        print(f"yeshiva: {self.yeshiva},  financially requirement: {self.financiallyrequirement}")