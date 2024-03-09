module Farm

export simulate_farm, Swan, Duck

function simulate_farm(adult_animals, baby_animals)

    println("Watch the animals walk and talk:")
    for animal in adult_animals
        walk(animal)
        talk(animal)
    end

    println("Raising the young:")
    # choose the first adult and make it the parent for all the baby_animals
    parent = first(adult_animals)
    println("Parent says:")
    talk(parent)
    println("Watch the babies:")
    for child in baby_animals
        raise_young(parent, child)
    end
end

abstract type Animal end
walk(self::Animal) = println("🚶 Waddle")
talk(self::Animal) = println("🗣 Talk")

struct Duck <: Animal end
raise_young(self::Duck, child::Animal) = println("🐤😢 Abandon")
raise_young(self::Duck, child::Duck) = println("🐤 ➡️ 💧 Lead to water")
talk(self::Duck) = println("🦆 Quack")

struct Swan <: Animal end
talk(self::Swan) = println("🦢 Hiss")
raise_young(self::Swan, child::Swan) = println("🐤 ↗️ 🦢 Carry on back")

end