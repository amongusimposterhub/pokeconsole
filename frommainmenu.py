input("PROFESSOR BROAK: Hey I'm Professor Broak! ")
input("PROFESSOR BROAK: Welcome to the world of Consolemons! ")
input("PROFESSOR BROAK: Consolemons are our friends in this world and you can feel free to catch one! ")
input("nPROFESSOR BROAK: I'll get you started!")
input("\nIn this game, you pick 3 starter consolemons Here are your choices!")
starter_pokemon = input("Select 1. for Balbasaur\nSelect 2. for Charmander\nSelect 3. for Squirtle\n")

if starter_pokemon == "1":
    print("\nYou have selected Balbasaur!")
    selected_pokemon = "Balbasaur"
elif starter_pokemon == "2":
    print("\nYou have selected Charmander!")
    selected_pokemon = "Charmander"
elif starter_pokemon == "3":
    print("\nYou have selected Squirtle")
    selected_pokemon = "Squirtle"

input("/n PROFESSOR BROAK",selected_pokemon,", what a great choice!")
