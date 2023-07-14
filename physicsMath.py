import math
class Maths:
    def add( num1,num2):
        
        return  num1+num2  
    def subtract(self, num1,num2):
        return num1-num2
    def mul(self, num1,num2):
        return num1*num2
    def modulos(self, num1,num2):
        return num1%num2
    def divide(self, num1,num2):
        return num1/num2
    
class Physics:
    def density(self, mass,velocity):
        return mass/velocity
    def power(self, work,time):
        return work/time
    def weight(self, mass,gravity):
        return mass*gravity
    def pressure(self, force,acceleration):
        return force/acceleration
    def  frequency(self, velocity,wavelength):
        return velocity/wavelength
    
    
selection = int(input("what subject do you want to calculate\n1 for Maths\n2 for Physics"))
if selection == 1:
    choice = int(input("Which formula do you want to run in maths\n1 for add\n2 for subtract"))
    if choice == 1:
        num1 = int(input("what is the first number:"))
        num2 = int(input("what is the first number:"))
        print(Maths.add(num1,num2))