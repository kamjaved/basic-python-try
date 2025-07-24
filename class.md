## Understanding Classes

Classes serve as blueprints for creating objects. They help organize code by grouping related data (attributes) and functions (methods) into a single, logical unit. For instance, in a game, you could have a `Mage` class with attributes like `health` and `mana`, and methods like `cast_magic`[1].

### Creating a Basic Class and Instances

A class is defined using the `class` keyword, followed by the class name, which conventionally uses PascalCase (e.g., `TestClass`). You can create multiple, independent instances of a class, each with its own set of attribute values[1].

```python
# A simple class with two attributes
class TestClass:
    test_var = [1, 2, 3]
    another_var = 'something'

# Create the first instance
test = TestClass()
# Update an attribute for the 'test' instance
test.another_var = 'a new value'
print(test.another_var) # Output: a new value

# Create a second, independent instance
test2 = TestClass()
# This instance retains the original attribute value
print(test2.another_var) # Output: something
```

### Class Methods and the `self` Parameter

Functions defined within a class are called methods. The first parameter of any method must be a reference to the current instance of the class, conventionally named `self`. This parameter allows you to access and modify the instance's attributes from within the method[1].

```python
class TestClass:
    test_var = [1, 2, 3]

    # A method that uses 'self' to access an attribute
    def test_function(self):
        print('Function in a class')
        print(self.test_var)

# Create an instance
test_instance = TestClass()
# Call the method on the instance
test_instance.test_function()
# Output:
# Function in a class
# [1, 2, 3]
```

### Special Dunder Methods

Python classes include special methods, known as "dunder" (double underscore) methods, which are automatically called in specific situations.

-  **`__init__`**: This method is the class constructor, executed when a new instance is created. It's commonly used to initialize attributes with values passed during instantiation[1].
-  **`__len__`**: This method is called when the built-in `len()` function is used on an object of the class[1].
-  **`__repr__`**: This method returns a developer-friendly string representation of the object, which is useful for debugging. It is called when `print()` is used on an instance[1].

```python
class Mage:
    # __init__ is called when a Mage object is created
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        print('The Mage class was created')

    # __repr__ is called when the object is printed
    def __repr__(self):
        return f'A monster with {self.health} HP'

# Creating an instance triggers __init__
mage = Mage(100, 200)

# Printing the instance triggers __repr__
print(mage)
# Output:
# The Mage class was created
# A monster with 100 HP
```

### Class Interaction

Objects can interact with each other. For example, an instance of a `Mage` class can have an `attack` method that modifies the attributes of a `Monster` instance[1].

```python
class Mage:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def attack(self, target):
        target.health -= 10

class Monster:
    health = 40

# Create instances
mage = Mage(100, 200)
monster = Monster()

print(f'Monster health before attack: {monster.health}') # Output: 40
mage.attack(monster)
print(f'Monster health after attack: {monster.health}')  # Output: 30
```

### Inheritance

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reuse by defining common functionality in a single base class[1].

The `super()` function is used within a child class to call methods from its parent class. This is particularly useful for extending the parent's `__init__` method without overriding it completely[1].

```python
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
```

### Final Exercise: Combining Concepts

The tutorial concludes with an exercise that combines these concepts. The goal is to create a `Monster` class that inherits an `attack` method from an `Entity` parent class and uses the `__repr__` method for a custom print output[1].

```python
# Parent class
class Entity:
    def attack(self):
        # 'self' here will refer to the instance of the child class (Monster)
        print(f'Attack with {self.damage} damage')

# Child class inheriting from Entity
class Monster(Entity):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def __repr__(self):
        return f'A monster with {self.health} HP'

# Create an instance of Monster
monster = Monster(100, 10)

# Call the inherited attack method
monster.attack() # Output: Attack with 10 damage

# Print the instance to see the custom __repr__ output
print(monster)   # Output: A monster with 100 HP
```

[1] https://www.youtube.com/watch?v=OHT0wGUz5GI&list=PPSV&ab_channel=NetNinja
