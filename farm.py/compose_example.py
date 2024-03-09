from FarmClass import Farm, Duck, Swan
print("👩‍🌾 Welcome to the farm!")

print("\nWe have ducks!")
Farm([Duck(), Duck()], [Duck(), Duck()]).simulate()

print("\nWe have swans!")
Farm([Swan(), Swan()], [Swan(), Swan()]).simulate()

print("\nWe have ducks and swans!")
Farm([Duck(), Swan()], [Duck(), Swan()]).simulate()