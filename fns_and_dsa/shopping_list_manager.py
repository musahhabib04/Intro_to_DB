def display_menu():
<<<<<<< HEAD
    print("\nShopping List Manager")
=======
    print("Shopping List Manager")
>>>>>>> 562f7f6 (Create shopping_list_manager.py with required functionality)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item cannot be empty.")
        
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == '3':
            if shopping_list:
<<<<<<< HEAD
                print("\nShopping List:")
=======
                print("Shopping List:")
>>>>>>> 562f7f6 (Create shopping_list_manager.py with required functionality)
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Shopping list is currently empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
<<<<<<< HEAD

=======
>>>>>>> 562f7f6 (Create shopping_list_manager.py with required functionality)
