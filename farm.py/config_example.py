# Define configurations for animals' behaviors
animal_configs = {
    "Duck": {
        "talk": "🦆 Quack",
        "walk": "🚶 Waddle",
        "raise_young": {
            "Duck": "🐤 ➡️ 💧 Lead to water",
            "default": "🐤😢 Abandon"
        }
    },
    "Swan": {
        "talk": "🦢 Hiss",
        "walk": "🚶 Waddle",
        "raise_young": {
            "Swan": "🐤 ↗️ 🦢 Carry on back",
            "default": "🐤😢 Abandon"
        }
    }
}

class Farm():
    def __init__(self, adult_animals, babies):
        self.adult_animals = adult_animals
        self.baby_animals = babies

    def simulate(self):
        print("Watch the animals walk and talk:")
        for animal_name in self.adult_animals:
            self.walk(animal_name)
            self.talk(animal_name)

        print("Raising the young:")
        parent = self.adult_animals[0]
        print("Parent says:")
        self.talk(parent)
        print("Watch the babies:")
        for child_name in self.baby_animals:
            self.raise_young(parent, child_name)

    def walk(self, animal_name):
        print(animal_configs[animal_name]["walk"])
        
    def talk(self, animal_name):
        print(animal_configs[animal_name]["talk"])

    def raise_young(self, parent_name, child_name):
        parent_config = animal_configs[parent_name]
        raise_behavior = parent_config["raise_young"].get(child_name, parent_config["raise_young"]["default"])
        print(raise_behavior)


if __name__ == "__main__":
    print("👩‍🌾 Welcome to the farm!")
    print("\nWe have ducks!")
    Farm(["Duck", "Duck"], ["Duck", "Duck"]).simulate()

    print("\nWe have swans!")
    Farm(["Swan", "Swan"], ["Swan", "Swan"]).simulate()

    print("\nWe have ducks and swans!")
    Farm(["Duck", "Swan"], ["Duck", "Swan"]).simulate()