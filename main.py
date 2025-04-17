from pet import Pet

name = input("Enter name of your pet: ")
pet_type = input("Enter type of your pet (e.g., Dog, Cat): ")

my_pet = Pet(name=name, pet_type=pet_type)
print(f"Creating pet: {my_pet.name} 🐾")

my_pet.get_status()

my_pet.eat()
my_pet.play()
my_pet.sleep()

my_pet.train("roll over")
my_pet.train("play dead")
my_pet.train("roll over")

my_pet.show_tricks()

if my_pet.is_hungry():
    print(f"⚠️ {my_pet.name} seems hungry! Maybe feed them again?")

my_pet.cheer_up()

my_pet.get_status()
