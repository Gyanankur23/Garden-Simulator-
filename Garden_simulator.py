# Garden Simulator

# We use two lists: one for plant names and one for their growth levels
plants = []
growth = []

def plant_seed():
    name = input("Enter the name of the plant: ")
    plants.append(name)
    growth.append(0)
    print(f"You planted a {name}!")

def water_plants():
    if not plants:
        print("No plants to water.")
        return
    for i in range(len(plants)):
        growth[i] += 1
    print("You watered all the plants!")

def show_garden():
    if not plants:
        print("Your garden is empty.")
    else:
        print("Garden status:")
        for i in range(len(plants)):
            print(f"{plants[i]} - Growth level: {growth[i]}")

def main():
    while True:
        print("\n--- Garden Simulator ---")
        print("1. Plant a seed")
        print("2. Water plants (make them grow)")
        print("3. Show garden")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            plant_seed()
        elif choice == "2":
            water_plants()
        elif choice == "3":
            show_garden()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3 or 4.")

main()
