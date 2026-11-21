def odd_even(a) :
    if(a % 2 == 0 ):
        return "Even number"
    else :
        return "Odd number"

myNum = 11

print(odd_even(myNum))

def largeNum (a , b) :
    if(a > b) :
        return a 
    else :
        return b 

x = 100
y = 200

print(largeNum(x , y))


class Student :
    name = "rahul" 
    age = 22

s1 = Student()  # object
print(s1.name)
print(s1.age)

class CarModel :

    def Tata(self , model , price) :
        print("Model is " , model , " and price is " , price)

    def Maruti(self , model , price) :
        print("Model is " , model , " and price is " , price)

s1 = CarModel()

s1.Tata("TATA SAFARI" , 3500000)
s1.Maruti("Swift Dezire" , 800000)
