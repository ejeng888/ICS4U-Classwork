class Dog:
    """
    Attributes:
        name (str): The name of the dog
        breed (str): The breed of the dog
        happiness (int)
    """
    def __init__(self, name: str, breed: str, happiness: int):
        self.name = name
        self.breed = breed
        self.happiness = happiness

    def __str__(self):
        return f"{self.name}, happiness: {self.happiness}"

    def eat(self):
        self.happiness = self.happiness + (self.happiness * 0.10)
        print(self.happiness)
    def bark(self):
        print("RUFF Ruff")


def main():
    dog = Dog("Mango", "Man", 200)
    dog.eat()

main()