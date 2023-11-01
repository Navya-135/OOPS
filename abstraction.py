class Employee:
    firstName:str="Navya"
    lastName:str="Kolakani"
    def fullName(self):
        return self.firstName+" "+self.lastName
emp=Employee()
emp.firstName="134"
print(emp.fullName())


class Employee:
    __firstName:str="Navya"
    __lastName:str="Kolakani"
    def fullName(self):
        return self.__firstName+" "+self.__lastName
emp=Employee()
emp.firstName="134"
print(emp.fullName())
