# Base class: Superhero
class Superhero:
    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Speed: {self.speed} mph")

    def move(self):
        print(f"{self.name} is moving...")

# Subclass: Flash inherits from Superhero
class Flash(Superhero):
    def __init__(self, name, power, speed, universe):
        super().__init__(name, power, speed)
        self.universe = universe

    def display_info(self):
        super().display_info()
        print(f"Universe: {self.universe}")

    def move(self):
        print(f"{self.name} runs at lightning speed! ⚡")

# Another class for Polymorphism example
class Superman(Superhero):
    def move(self):
        print(f"{self.name} flies through the sky! 🦸‍♂️")

# Create objects
flash = Flash("Barry Allen", "Super Speed", 670_616_629, "DC Universe")
superman = Superman("Clark Kent", "Super Strength & Flight", 200_000)

# Display details
print("=== Superhero Details ===")
flash.display_info()
print()
superman.display_info()

# Polymorphism demonstration
print("\n=== Movement Demonstration ===")
for hero in [flash, superman]:
    hero.move()
