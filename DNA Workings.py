__author__ = 'Matt Q'
import random

base = [1,2,3,4]
digits = 27

class Person:

    def __init__(self):
        self.__units = 27
        self.__sections = 3
        self.__count = 0

        self.name_vowels = []
        self.name_consonants = []
        self.num_syllables = 0

        self.__name = None
        self.__race = None
        self.__gender = None

        self.divisible_values = {"7 Divisible":5,
                                 "5 Divisible":4,
                                 "3 Divisible":3,
                                 "2 Divisible":2,
                                 "Prime Number":1}

        self.vowels = ["a","e","i","o","u","ea",'ae','ei','io','ie','ou','ia','eo','ee', 'oo']
        self.consonants = ["b","c","d",'f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
                           'tt','ch','rr','rl','nn','nd','th','ty','tr','ck','kn','bl','br','cl','cr','dr',
                           'fl','fr','gl','gr','pl', 'pr', 'sc','sh','sk','sl','sm','sn',
                           'sp','st','sw','tr','tw', 'wh','wr','sch', 'scr','shr', 'sph','spl','spr',
                            'squ','str','thr']


        self.number_groups = []
        self.groupings = []

        self.calc_total()
        self.determine_divisibility()

        self.determine_name()
        self.determine_race()
        self.determine_gender()

    def __str__(self):

        return "Hello, my name is "+str(self.get_name())+" from "+str(self.get_race())+ \
               " and I am a "+str(self.get_gender())+"."

    def talk(self):
        print("Hello, my name is "+str(self.get_name())+" from "+str(self.get_race())+
              " and I am a "+str(self.get_gender())+".")

    # Figures out the total for each section that defines each piece.
    def calc_total(self):
        for i in range(0, self.__sections):
            self.__count = 0
            for j in range(0, self.__units):
                x = base[random.randint(0,3)]
                #print(x, end = '')
                self.__count += x
            #print()
            self.number_groups.append(self.__count)

    def determine_divisibility(self):
        for i in self.number_groups:
            if i%7 == 0:
                self.groupings.append("7 Divisible")
            elif i%5 == 0:
                self.groupings.append("5 Divisible")
            elif i%3 == 0:
                self.groupings.append("3 Divisible")
            elif i%2 == 0:
                self.groupings.append("2 Divisible")
            else:
                self.groupings.append("Prime Number")


    #### Generating a name based on syllables
    def syllables(self):

        # Figures out which group we are using.
        self.num_syllables = self.divisible_values[self.groupings[0]]
        self.num_syllables %= 2
        self.num_syllables += 1

        # Go through each syllable and pick a certain number of vowels and consonants
        for i in range(0,self.num_syllables):
            self.name_vowels.append(self.vowels[random.randint(0,len(self.vowels)-1)])
            self.name_consonants.append(self.consonants[random.randint(0,len(self.consonants)-1)])

    def determine_name(self):

        self.syllables()
        #Choose if we want to start name with vowel or consonant
        name_start = random.randint(1,2)

        # Empty list to be used to place the order of consonants and vowels
        name_parts = []
        self.__name = ""

        # Begin with a vowel
        if name_start%2 == 0:
            for i in range(0, self.num_syllables):
                name_parts.append(str(self.name_vowels[i]))
                name_parts.append(str(self.name_consonants[i]))

        # Begin with a consonant
        else:
            for i in range(self.num_syllables):
                name_parts.append(str(self.name_consonants[i]))
                name_parts.append(str(self.name_vowels[i]))

        # Conjoin all of the letters together
        for i in name_parts:
            self.__name += i

    # Final piece that returns name
    def get_name(self):
        self.__name = str(self.__name).capitalize()
        return self.__name

    # Determine Race
    def determine_race(self):
        race = self.divisible_values[self.groupings[1]]
        self.__race = "Group "+str(race)

    def get_race(self):
        return self.__race

    # Determine Gender
    def determine_gender(self):
        if self.number_groups[2] %2 == 0:
            self.__gender = "female"
        else:
            self.__gender = "male"

    def get_gender(self):
        return self.__gender


    def compare_information(self, other_person):
        if str(other_person.get_race()) == str(self.get_race()):
            #print(self.get_name()+ " says: " +"Me and " + other_person.get_name()+" are in the same group.")
            return True
        else:
            #print(self.get_name()+ " says: "+"Me and "+ other_person.get_name()+ " are in different groups.")
            return False


class Population:

    def __init__(self, population):

        self.group = []
        self.race_groups = [[],[],[],[],[]]

        for i in range(0,population):
            i = Person()
            self.group.append(i)

        self.group_individuals()

    def group_individuals(self):
        for i in self.group:
            self.race_groups[i.divisible_values[i.groupings[1]]-1].append(i.get_name())
        return self.race_groups

    def display_groups(self):
        position = 0
        for i in self.race_groups:
            print("Group"+ str(position +1), end = ": ")
            for j in self.race_groups[position]:
                print(j, end = " ")

            position +=1
            print()


population = Population(10)
population.display_groups()

print()
a = Person()
b = Person()
a.talk()
b.talk()
#print("Hello, my name is "+p.get_name()+" from "+p.get_race()+ " and I am a "+p.get_gender()+".")

