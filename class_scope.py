#global scope
class Employee:
    firstName:str="Navya"
    lastName:str="Kolakani"

emp=Employee()
print(emp.firstName)

#partially private scope
class Employee:
    _firstName:str="Navya"
    _lastName:str="Kolakani"

emp=Employee()
print(emp._firstName)

#strictly private scope
class Employee:
    __firstName:str="Navya"
    __lastName:str="Kolakani"

emp=Employee()
print(emp.__firstName)