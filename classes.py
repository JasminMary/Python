class Dog:
    energy = "high"

    def speak(self):
        return("woof")


bilbo_waggins = Dog()

dogsay = bilbo_waggins.speak()

print(f" The dog says {dogsay}")
