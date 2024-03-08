from Person import Person


class Girl(Person):
    def __init__(self, firstName, lastName, age, height, sector, talentLevel,
                 strikingCharacterTrait, seminar, financiallyParticipation):
        super(Girl, self).__init__(firstName, lastName, age, height, sector, talentLevel, strikingCharacterTrait)
        self.seminar = seminar
        self.financiallyParticipation = financiallyParticipation

    def print(self):
        print(f"The name is: {self.firstName} {self.lastName}")
        print(f"age: {self.age}, hight: {self.height}, sector: {self.sector}")
        print(f"talent level: {self.talentLevel}, striking character trait: {self.strikingCharacterTrait}")
        print(f"seminar: {self.seminar},  financially participation: {self.financiallyParticipation}")

    result = lambda str1, str2: str1 == str2



