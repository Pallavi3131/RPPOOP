class Animal:
    def __init__(self,species,color,nickname):
        self.species = self.species
        self.color = color
        self.nickname = nickname

class Dog(Animal):
    def sound(self):
        print("He Bhows")

    def fav_food(self):
        print("He loves to eat bones")

class Cat(Animal):
    def sound(self):
        print("She does Meow Meow")

    def fav_food(self):
        print("She eats catfood")
dog_Name= input("Enter the Name of your dog: ")
dog_color= input("Enter the color of your dog: ")
dog_species = input("Enter the breed of your dog: ")
dog1 = Dog(dog_Name, dog_color, dog_species)

print(f"Species of Dog is: {dog1.species}")
print(f"Name of Dog is: {dog1.nickname}")
print(f"Color of Dog is: {dog1.color}")
dog1.fav_food()
dog1.sound()
print("------------------------------------------------------")

cat_name = input("Enter the name of your Cat: ")
cat_color = input("Enter the color of your Cat: ")
cat_species = input("Enter the breed of your Cat: ")
cat1 = Cat(cat_name, cat_color, cat_species)

print(f"Species of Cat is: {cat1.species}")
print(f"Name of Cat is: {cat1.nickname}")
print(f"Color of Cat is: {cat1.color}")
cat1.fav_food()
cat1.sound()

