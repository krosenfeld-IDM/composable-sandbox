class Farm():
    def __init__(self, adult_animals, babies):
        self.adult_animals = adult_animals
        self.baby_animals = babies

    def simulate(self):
        print("Watch the animals walk and talk:")
        for animal in self.adult_animals:
            animal.walk()
            animal.talk()

        print("Raising the young:")
        parent = self.adult_animals[0]
        print("Parent says:")
        parent.talk()
        print("Watch the babies:")
        for child in self.baby_animals:
            parent.raise_young(child)


class Animal():

    def walk(self):
        print("🚶 Waddle")
        
    def talk(self):
        print("🗣 Talk")

    def raise_young(self, child):
        pass


class Duck(Animal):
    def __init__(self):
        super().__init__()

    def talk(self):
        print("🦆 Quack")

    def raise_young(self, child):
        if isinstance(child, Duck):
            print("🐤 ➡️ 💧 Lead to water")
        else:
            print("🐤😢 Abandon")


class Swan(Animal):
    def __init__(self):
        super().__init__()

    def talk(self):
        print("🦢 Hiss")

    def raise_young(self, child):
        if isinstance(child, Swan):
            print("🐤 ↗️ 🦢 Carry on back")