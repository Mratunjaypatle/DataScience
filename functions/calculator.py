class calculator :

    def addition (self , first , second) :
        return first + second 

    def substraction (self , first , second) :
        return first - second 

    def multiplication (self , first , second) :
        return first * second 

    def division (self , first , second) :
        return first / second 

    def modulas (self , first , second) :
        return first % second 

c1 = calculator()

print("Addition is " , c1.addition(100 , 200))
print("Substraction is " , c1.substraction(100 , 50))
print("Multiplication is " , c1.multiplication(100 , 6))
print("Division is " , c1.division(100 , 5))
print("Reminder is " , c1.modulas(79 , 3))


    