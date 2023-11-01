#class
#syntax:  class className:
              #def_init____(self):
                    #logic
              # //variables
              # //functions

class employee:
    firstName:str="Navya"
    lastName:str="Kolakani"
    def fullName(self):
        return self.firstName+" "+self.lastName
emp=employee()
print(emp.fullName())


#fibonocii

class fibseries:
    def fibex(selfself):
        n=10
        a=1
        b=0
        i=1
        lst=[]
        while i<=n:
            lst.append(b)
            a=a+b
            b=a-b
            i+=1
        print(lst)
fib=fibseries()
fib.fibex()