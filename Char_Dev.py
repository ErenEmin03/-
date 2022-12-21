from distutils import errors

class Menu:
    def __init__(self):
        self.characters=[]
        
    def print_menu(self):
        print("1. Insert Character Name: ")
        print("2. Select gender: ")
        print("3. Select role: ")
        print("4. Select weapon of choice")
        print("5. Select item:")
    
    def command_create_character(self, name, sex, ch_class):
        name = input("Enter Character Name (at least 4 characters): ")
        if len(name) < 4:
            raise errors.InvalidDataFormat("Character name must be at least 4 characters")
        
        if name in [character.name for character in self.characters]:
            raise errors.CharacterExists("This name already")

        gender= input("Select Gender (M or F): ")

        if gender not in ["M" or "F"]:
            raise errors.InvalidDataFormat("Invalid Gender. Doesn't exist")

        role= input("Enter Class(Mage, Warrior, Fighter, Tank, Necromancer, Pyromancer, Monk): ")

        if role not in["Mage", "Warrior", "Fighter", "Tank", "Necromancer", "Pyromancer", "Monk"]:
            raise errors.InvalidCharacterClass("Invalid Character Class")

        weapon= input("Enter Weapon of Choice: ")
        
        if weapon not in ["Sword" or "Shield" or "Wand"]:
            raise errors.InvalidWeaponClass("Invalid Weapon of Choice. Here, have that stick")
        
        item= input("Select an item:")

        if item not in["Broken Key", "Very Big Stone", "Ring"]:
            raise errors.InvalidItemClass("Item doesnt exist. Here is another stick")

    def run(self):
        # infinite menu loop
        while True:  
            # print the menu
            # ...

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:
                # process the user's choice
                if choice == "1":
                    name =input("Enter Name")
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()
menu = Menu()
menu.print_menu()
