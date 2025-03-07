# class PlayerCharacter():
#     def __init__(self,name,age): # Same as constructor in java, its like basic intro
#         self.name=name  # self refers to current class like 'this' in java
#         self.age=age


#     def shout(self,name,year):
#         age=2024-year
#         return (f'hi {name}. you are {age} years old now')


# player1= PlayerCharacter('teddy',17) 
# print(player1.shout('John', 2007))
# print(player1.age)


# Encapsulation - binding of data and function in a class to manipulate data

# Abstraction - hiding the info and provide necessary one nad  python don't have 'private' variables use convection name instead

#  Inheritance - new obj take on the property of existing one 

class User():
    def __init__(self,email):
        self.email=email
    def sign_in(self): # "__init__" doesn't require when we don't have attirbute to access
        return ("logeed in...")
    
class Wizard(User): #providing parent class inside parrenthesis of child class way of defining its inherits
    def __init__(self, name, power):
        # super().__init__(email)
        self.name=name
        self.power=power
    def attack(self):
        return (f'{self.power} power is left')
    
class Archer(User):
        def __init__(self, name, bullet):
            # super().__init__(email)
            self.name=name
            self.bullet=bullet
        def attack(self):
            return (f'{self.bullet} attack is left')


# wizard1=Wizard("Yami","Dark Magic","blackbulls@mail.com")
# print(wizard1.sign_in())
# print(wizard1.attack())

# archer1=Archer("Ben Beckmann","haki in bullet","akagami@gmail.com")
# print(archer1.sign_in())
# print(archer1.attack())

# Polymorphism - many forms 

# def player_role(char):
#     print(char.attack()) #calls the method which having same name but approaches different obj 

# player_role(wizard1)
# print(wizard1.email)
# player_role(archer1)
# print(archer1.email)

# By using super method to call a parent cls from child 

# Multiple inheritance 

class Hybrid(Wizard,Archer):
    def __init__(self,name,power,bullet):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, bullet)

hb=Hybrid("Aizen",100,"infinite")
# print(hb.attack())
print(hb.bullet)