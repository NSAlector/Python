
from city.person import Person
from city.city import  City
from city.city_list import CityList

def person_test():
    p = Person('a', 'b', 'c')
    #help(p)

    #print(dir(p))
    print(p)


def city_test():
    c1 = City("City1", 10)
    #print(c1)
    c2 = City("City2", 50)
    #print(c2)

    #for i in range(15):
    #    c1.add_person()

    #for i in range(5):
    #    c1.remove_person()
    #    c2.remove_person()

    #print(c1)

    c2.tmp1 = 10
    c2.tmp2 = 20

    # print(c1.__dict__)
    # print(c2.__dict__)

    # print(dir(c1))
    #print(dir(c2))

    #print(hasattr(c2, 'tmp3' ))

    #for att in dir(c2):
    #    print(att, getattr(c2, att))

def city_list_test():

    c3 = CityList("City_with_named_persons", 10)

    for i in range(15):
        s = str(i)
        c3.add_person(Person(s,s+s, s+s+s))

    #print(c3)

    for i in range(2,10,2):
        c3.remove_person(i)

    print(c3)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Program is started")

    #person_test()
    city_test()
    city_list_test()

    print("Program is finished")


