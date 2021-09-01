class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self): 
        Pet.play(self.pet, self.pet.name)
        return self

    def feed(self, food_or_treat):
        if food_or_treat == "treat":
            self.treats-=1
        elif food_or_treat == "food":
            self.pet_food-=1
        Pet.eat(self.pet, food_or_treat)
        return self

    def bathe(self):
        Pet.noise(self.pet, self.pet.name)
        return self


class Pet:
    def __init__(self, name, type, tricks, health, energy, noise):
        self.name = name 
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.pet_noise = noise
    def sleep(self):
        self.energy += 25
        print(f"Badge takes a nap. Energy+25. (Energy= {self.energy})")
        return self
    def eat(self, food_or_treat):
        if food_or_treat == "food":
            self.energy += 5
            self.health += 10
            print(f"PLAIN FOOD?! {self.name} eats passive-aggressively. Energy+5 Health+10. (Energy= {self.energy} Health= {self.health})")
            return self
        elif food_or_treat == "treat":
            self.energy += 10
            self.health += 5
            print(f"TREATS! {self.name} purrs and chomps. Energy+10 Health+5. (Energy= {self.energy} Health= {self.health})")
            return self
    def play(self, pet_name):
        self.health += 5
        print(f"You take {pet_name} for a walk and now she has the zoomies! Health +5 (Health= {self.health})")
        return self
    def noise(self, pet_name):
        print(f"You give {pet_name} a bath and she says *{self.pet_noise}* to that.")
        return self

badge = Pet("Badge", "Cat", "Yell", 100, 50, "ROAR!")
todd = Ninja("Todd", "Aulwurm", 100, 5, badge)
todd.feed("food").walk().bathe().feed("treat")
badge.sleep()
