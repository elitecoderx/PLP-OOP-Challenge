from pet import Pet

name = input("Enter name of your pet: ")
pet_type = input("Enter type of your pet (e.g., Dog, Cat): ")

my_pet = Pet(name=name, pet_type=pet_type)
print(f"Creating pet: {my_pet.name} 🐾")

def show_menu():
    print("\nChoose an action:")
    print("1. Get status")
    print("2. Eat")
    print("3. Play")
    print("4. Sleep")
    print("5. Train a new trick")
    print("6. Show tricks")
    print("7. Check if hungry")
    print("8. Cheer up")
    print("9. Quit")

while True:
    show_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        my_pet.get_status()
    elif choice == "2":
        my_pet.eat()
    elif choice == "3":
        my_pet.play()
    elif choice == "4":
        my_pet.sleep()
    elif choice == "5":
        trick = input("Enter trick to train: ")
        my_pet.train(trick)
    elif choice == "6":
        my_pet.show_tricks()
    elif choice == "7":
        if my_pet.is_hungry():
            print(f"⚠️ {my_pet.name} seems hungry! Maybe feed them again?")
        else:
            print(f"{my_pet.name} is not hungry.")
    elif choice == "8":
        my_pet.cheer_up()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
        
