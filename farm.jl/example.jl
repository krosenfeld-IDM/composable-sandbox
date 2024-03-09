using Revise

include("Farm.jl")
using .Farm

println("👩‍🌾 Welcome to the farm!")

# Simulate ducks
println("\nWe have ducks!")
simulate_farm([Duck(), Duck()], [Duck(), Duck()])

# Simulate swans
println("\nWe have swans!")
simulate_farm([Swan(), Swan()], [Duck(), Swan()])

# Both swans and ducks
println("\nWe have ducks and swans!")
simulate_farm([Duck(), Swan()], [Swan(), Duck()])

