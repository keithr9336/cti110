#Ryne Keith
#12-11-25
#final_project.py

import random
import time

# -----------------------------
# Character Setup
# -----------------------------
def create_character():
    character = {
        "name": "Alex Rivers",     # main character
        "energy": 100,
        "coins": 0,
        "location": "Whisperwind Forest Entrance",
    }
    inventory = {
        "berry": 0,
        "mushroom": 0,
        "crystal": 0
    }
    return character, inventory


# -----------------------------
# Helper Function
# -----------------------------
def print_pause(message):
    print(message)
    time.sleep(1)


# -----------------------------
# Exploring the Forest
# -----------------------------
def explore_forest(character, inventory):
    print_pause(f"\n🌲 {character['name']} walks deeper into Whisperwind Forest...")

    event = random.choice(["berries", "mushroom", "coins", "npc", "nothing"])

    if character["energy"] <= 0:
        print_pause("❗ You are too tired to explore! Try resting.")
        return

    # Exploration possibilities
    if event == "berries":
        amount = random.randint(1, 3)
        inventory["berry"] += amount
        character["energy"] -= 5
        print_pause(f"🫐 You found {amount} forest berries!")
    
    elif event == "mushroom":
        inventory["mushroom"] += 1
        character["energy"] -= 5
        print_pause("🍄 You found a rare Mooncap Mushroom!")

    elif event == "coins":
        found = random.randint(5, 15)
        character["coins"] += found
        character["energy"] -= 5
        print_pause(f"🪙 You found {found} shiny coins hidden beneath a log!")

    elif event == "npc":
        meet_npc(character)

    else:
        character["energy"] -= 5
        print_pause("😕 Nothing special happened this time.")

    character["location"] = "Deep Whisperwind Forest"


# -----------------------------
# NPC Encounters
# -----------------------------
def meet_npc(character):
    npcs = ["Elder Rowan", "Mira the Botanist", "Finn the Forest Guide"]
    npc = random.choice(npcs)

    print_pause(f"\n🌟 You encounter **{npc}**!")

    if npc == "Elder Rowan":
        print_pause("Elder Rowan says: 'Stay aware, young traveler. The forest rewards the patient.'")

    elif npc == "Mira the Botanist":
        print_pause("Mira smiles: 'If you find any Mooncap Mushrooms, handle them gently!'")

    elif npc == "Finn the Forest Guide":
        print_pause("Finn waves excitedly: 'If you're low on energy, be sure to rest!'")

    character["energy"] -= 3


# -----------------------------
# Rest to Recover Energy
# -----------------------------
def rest(character):
    gained = random.randint(10, 25)
    character["energy"] += gained

    if character["energy"] > 100:
        character["energy"] = 100

    print_pause(f"\n😴 You rest under a tall oak tree and regain {gained} energy.")


# -----------------------------
# Visit the Forest Shop
# -----------------------------
def visit_shop(character, inventory):
    print_pause("\n🏪 You arrive at Elder Rowan's Shop.")
    print_pause("Elder Rowan smiles warmly: 'Welcome back, traveler.'")

    while True:
        print("\n-- Rowan's Forest Shop --")
        print("1. Sell berries (+3 coins each)")
        print("2. Sell mushrooms (+8 coins each)")
        print("3. Leave shop")

        choice = input("Choose an option: ")

        if choice == "1":
            if inventory["berry"] > 0:
                sell = inventory["berry"]
                earnings = sell * 3
                inventory["berry"] = 0
                character["coins"] += earnings
                print_pause(f"🫐 Rowan buys your berries for {earnings} coins!")
            else:
                print_pause("You have no berries to sell.")

        elif choice == "2":
            if inventory["mushroom"] > 0:
                sell = inventory["mushroom"]
                earnings = sell * 8
                inventory["mushroom"] = 0
                character["coins"] += earnings
                print_pause(f"🍄 Rowan buys your mushrooms for {earnings} coins!")
            else:
                print_pause("You have no mushrooms to sell.")

        elif choice == "3":
            print_pause("👋 You say goodbye to Elder Rowan and step outside.")
            character["location"] = "Forest Path"
            break

        else:
            print_pause("That is not a valid choice. Try again.")


# -----------------------------
# Display Character Stats
# -----------------------------
def show_stats(character, inventory):
    print("\n📊 --- Current Stats ---")
    print(f"Name: {character['name']}")
    print(f"Location: {character['location']}")
    print(f"Energy: {character['energy']}")
    print(f"Coins: {character['coins']}")
    print("Inventory:")
    for item, qty in inventory.items():
        print(f"  - {item}: {qty}")
    print("-------------------------")


# -----------------------------
# Main Game Loop
# -----------------------------
def main():
    print("🌟 Welcome to *Whisperwind Forest Explorer*! 🌟")
    print_pause("Your goal: Explore, gather items, meet NPCs, and earn coins.\n")

    character, inventory = create_character()

    while True:
        show_stats(character, inventory)

        print("\nWhat would you like to do?")
        print("1. Explore the forest 🌲")
        print("2. Rest 😴")
        print("3. Visit Elder Rowan’s shop 🏪")
        print("4. Quit the adventure 🚪")

        choice = input("Choose an action: ")

        if choice == "1":
            explore_forest(character, inventory)
        elif choice == "2":
            rest(character)
        elif choice == "3":
            visit_shop(character, inventory)
        elif choice == "4":
            print_pause("\nThank you for exploring Whisperwind Forest! 🌿")
            break
        else:
            print_pause("Invalid choice, please try again.")


# Run the game
if __name__ == "__main__":
    main()
