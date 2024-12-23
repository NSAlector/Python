from exception_city.city import City

class CityList(City):

    def __init__(self, name, count):
        super(CityList, self).__init__(name, count)
        self.__person_list = []


    def add_person(self, p):
        try:
            super(CityList,self).add_person()
            self.__person_list.append(p)
        except Exception as e:
            raise e
        else:
            print("The resident was added successfully")
        finally:
            print("Total count of residents in the city {} is {} ".format(self._name, len(self.__person_list)))

    def remove_person(self, i):
        try:
            super(CityList,self).remove_person()
            assert i < len(self.__person_list), "There is no resident {} in the city {}".format(i, super(CityList,self)._name)
            del self.__person_list[i]
        except Exception as e:
            raise e
        else:
            print("The resident was removed successfully")
        finally:
            print(e)

    def __str__(self):
        s1 = super(CityList, self).__str__()

        s = []
        s.append(s1)

        s.append("List of residents \n")
        for (i,v) in enumerate(self.__person_list):
            s.append(" - {} - {} \n".format(i,v))

        return ''.join(s)
