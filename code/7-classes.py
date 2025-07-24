# Below are Basic Example for more detailed explanantion see class.md

# Basic Class
class TestClass:
  a_list=[1,2,3,4,5,6,7]
  a_string='Hello World'
  # you have to pass self as first argument when you declare method inside class
  # otherwise it will throw error  "takes 0 positional arguments but 1 was given"
  def a_method(self):
    print('Hello')
    print(self.a_string)


test=TestClass()
test.a_method()

# lets create another instance of same class
test_two= TestClass()
test_two.a_string='Hello Guys!'
# it will not mutate class a_string varibale instead it create seprate one for specific instance
# whihc is very useful 

print(test_two.a_string)

# CLASS INTERACTION AND DUNDER METHOD

class Mage:
  def __init__(self, hea, mana):
    self.health=hea
    self.mana=mana
  
  def attack(self, target):
    target.health-=10

class Monster:
    health=40

mage=Mage(60,200)
monster=Monster()

print(f'Monster health before attack: {monster.health}') # Output: 40
mage.attack(monster)
print(f'Monster health after attack: {monster.health}')  # Output: 30


# Parent class with a shared method

class Human:
    def __init__(self, health):
        self.health = health

    def attack(self):
        print('Attack')

# Child class inheriting from Human
class Warrior(Human):
    def __init__(self, health, defense):
        # Call the parent's __init__ method
        super().__init__(health)
        # Add a new attribute specific to Warrior
        self.defense = defense

# Child class inheriting from Human
class Barbarian(Human):
    def __init__(self, health, damage):
        # Call the parent's __init__ method
        super().__init__(health)
        # Add a new attribute specific to Barbarian
        self.damage = damage

warrior = Warrior(50, 5.5)
barbarian = Barbarian(100, 8.1)

# Both instances can use the attack method from the Human class
warrior.attack()    # Output: Attack
barbarian.attack()  # Output: Attack

# Accessing the health attribute initialized via super()
print(warrior.health) # Output: 50


########################################################
## EXERCISE:
# Create a Monster class where you can set a health and damage attribute on creation
# It should also inherit from a entity class to get an attack method (that prints 'attack' & the damage amount)
# Do some research so that when an instance of the class is printed it returns 'a monster with {health} hp'
########################################################

class MonsterParent:
   def attack(self):
      print(f"Attack From Monster Parent with {self.damage} damage")
      

class MonsterRawan(MonsterParent):
  def __init__(self, health, damage):
      self.health=health
      self.damage=damage
      
  def __repr__(self):
     return f'a monster with {self.health} HP'
  

monsterRawan= MonsterRawan(200, 400)
monsterRawan.attack()
print(monsterRawan)