# Interactive Adventure Game - No imports needed!

def main():
    print("🌟 Welcome to the Mystery Island Adventure! 🌟")
    print("=" * 50)
    
    # Get player info
    name = input("What's your name, brave adventurer? ")
    print(f"\nHello {name}! You've crash-landed on a mysterious island...")
    
    # Game stats
    health = 100
    coins = 0
    inventory = []
    
    while True:
        print(f"\n--- STATUS ---")
        print(f"Health: {health}/100 ❤️")
        print(f"Coins: {coins} 🪙")
        print(f"Inventory: {inventory if inventory else 'Empty'}")
        print("-" * 20)
        
        # Main menu
        print("\nWhere do you want to go?")
        print("1. 🏖️  Explore the Beach")
        print("2. 🌳 Enter the Jungle")
        print("3. 🏔️  Climb the Mountain")
        print("4. 🏪 Visit the Trading Post")
        print("5. 🎒 Check Inventory")
        print("6. 🚪 Quit Game")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            health, coins, inventory = explore_beach(health, coins, inventory)
        elif choice == "2":
            health, coins, inventory = enter_jungle(health, coins, inventory)
        elif choice == "3":
            health, coins, inventory = climb_mountain(health, coins, inventory)
        elif choice == "4":
            coins, inventory = trading_post(coins, inventory)
        elif choice == "5":
            show_inventory(inventory)
        elif choice == "6":
            print(f"\nThanks for playing, {name}! 👋")
            print(f"Final Score - Health: {health}, Coins: {coins}")
            break
        else:
            print("Invalid choice! Please try again.")
        
        # Check if game over
        if health <= 0:
            print("\n💀 GAME OVER! You ran out of health!")
            print("Better luck next time!")
            break

def explore_beach(health, coins, inventory):
    print("\n🏖️ You're walking along the sandy beach...")
    
    events = [
        "You find a shiny seashell! +5 coins",
        "A crab pinches your toe! -10 health",
        "You discover a message in a bottle! +1 map",
        "You find some coconuts! +1 food",
        "The waves wash over you peacefully. +5 health"
    ]
    
    # Random event (using simple method without imports)
    event_num = len(str(hash(str(health + coins)))) % len(events)
    event = events[event_num]
    print(f"🎲 {event}")
    
    # Apply effects
    if "5 coins" in event:
        coins += 5
    elif "10 health" in event:
        health -= 10
    elif "map" in event:
        inventory.append("Treasure Map")
    elif "food" in event:
        inventory.append("Coconut")
    elif "5 health" in event:
        health += 5
    
    return health, coins, inventory

def enter_jungle(health, coins, inventory):
    print("\n🌳 You venture into the dense jungle...")
    
    print("You encounter a wild animal! What do you do?")
    print("1. Fight it!")
    print("2. Run away!")
    print("3. Try to befriend it")
    
    choice = input("Choose (1-3): ")
    
    if choice == "1":
        print("🥊 You fought bravely but got hurt! -15 health, +10 coins")
        health -= 15
        coins += 10
    elif choice == "2":
        print("🏃 You ran away safely! -5 health")
        health -= 5
    elif choice == "3":
        print("🐾 The animal becomes your friend! +1 pet, +5 health")
        inventory.append("Animal Friend")
        health += 5
    else:
        print("You froze in fear! -10 health")
        health -= 10
    
    return health, coins, inventory

def climb_mountain(health, coins, inventory):
    print("\n🏔️ You start climbing the steep mountain...")
    
    if "Treasure Map" in inventory:
        print("🗺️ Your treasure map shows a secret cave!")
        print("You find a chest full of gold! +50 coins")
        coins += 50
        inventory.remove("Treasure Map")
    else:
        print("The climb is exhausting but you find some herbs!")
        print("+20 health, +1 healing herb")
        health += 20
        inventory.append("Healing Herb")
    
    return health, coins, inventory

def trading_post(coins, inventory):
    print("\n🏪 Welcome to the Island Trading Post!")
    print("What would you like to buy?")
    print("1. Health Potion - 15 coins (+30 health)")
    print("2. Lucky Charm - 25 coins (better luck)")
    print("3. Fishing Rod - 20 coins")
    print("4. Leave")
    
    choice = input("Choose (1-4): ")
    
    if choice == "1" and coins >= 15:
        coins -= 15
        inventory.append("Health Potion")
        print("✅ Bought Health Potion!")
    elif choice == "2" and coins >= 25:
        coins -= 25
        inventory.append("Lucky Charm")
        print("✅ Bought Lucky Charm!")
    elif choice == "3" and coins >= 20:
        coins -= 20
        inventory.append("Fishing Rod")
        print("✅ Bought Fishing Rod!")
    elif choice == "4":
        print("Come back anytime!")
    else:
        print("❌ Not enough coins or invalid choice!")
    
    return coins, inventory

def show_inventory(inventory):
    print("\n🎒 Your Inventory:")
    if not inventory:
        print("Your inventory is empty!")
    else:
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")
        
        # Use items
        print("\nWant to use an item? (Enter number or 0 to go back)")
        try:
            choice = int(input("Choice: "))
            if 1 <= choice <= len(inventory):
                item = inventory[choice - 1]
                if "Health Potion" in item:
                    print("🧪 You feel much better! +30 health")
                    inventory.remove(item)
                    return 30  # Health bonus
                elif "Healing Herb" in item:
                    print("🌿 The herb heals your wounds! +15 health")
                    inventory.remove(item)
                    return 15  # Health bonus
                else:
                    print(f"You can't use {item} right now!")
        except:
            print("Invalid input!")
    
    return 0

# Start the game!
if __name__ == "__main__":
    main()
