import array as arr

def display_menu():
    print("\n--- ARRAY OPERATIONS MENU ---")
    print("1. Display Array")
    print("2. Append Element (Add to End)")
    print("3. Insert Element (At Specific Index)")
    print("4. Delete Element by Value (First Occurrence)")
    print("5. Delete Element by Index (Pop)")
    print("6. Search for an Element Index")
    print("7. Update Element at Index")
    print("8. Reverse the Array")
    print("9. Exit")

def main():
    # Initialize an integer array ('i' stands for signed integer)
    my_array = arr.array('i', [10, 20, 30, 40, 50])
    
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-9): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 9.")
            continue

        if choice == 1:
            print(f"📊 Current Array: {list(my_array)}")

        elif choice == 2:
            try:
                val = int(input("Enter integer to append: "))
                my_array.append(val)
                print(f"✅ Appended {val}. New array: {list(my_array)}")
            except ValueError:
                print("❌ Please enter a valid integer.")

        elif choice == 3:
            try:
                idx = int(input(f"Enter index (0 to {len(my_array)}): "))
                val = int(input("Enter integer to insert: "))
                my_array.insert(idx, val)
                print(f"✅ Inserted {val} at index {idx}. New array: {list(my_array)}")
            except IndexError:
                print("❌ Index out of range!")
            except ValueError:
                print("❌ Invalid input data type.")

        elif choice == 4:
            try:
                val = int(input("Enter value to delete: "))
                my_array.remove(val)
                print(f"✅ Removed first occurrence of {val}. New array: {list(my_array)}")
            except ValueError:
                print(f"❌ Value {val} not found in the array.")

        elif choice == 5:
            try:
                idx = int(input(f"Enter index to pop (0 to {len(my_array)-1}): "))
                removed_val = my_array.pop(idx)
                print(f"✅ Popped element {removed_val} from index {idx}. New array: {list(my_array)}")
            except IndexError:
                print("❌ Index out of range!")
            except ValueError:
                print("❌ Please enter a valid integer index.")

        elif choice == 6:
            try:
                val = int(input("Enter value to search: "))
                idx = my_array.index(val)
                print(f"🔍 Value {val} found at index: {idx}")
            except ValueError:
                print(f"❌ Value {val} does not exist in the array.")

        elif choice == 7:
            try:
                idx = int(input(f"Enter index to update (0 to {len(my_array)-1}): "))
                val = int(input("Enter new value: "))
                my_array[idx] = val
                print(f"✅ Updated index {idx} to {val}. New array: {list(my_array)}")
            except IndexError:
                print("❌ Index out of range!")
            except ValueError:
                print("❌ Invalid input data type.")

        elif choice == 8:
            my_array.reverse()
            print(f"🔄 Array reversed! New array: {list(my_array)}")

        elif choice == 9:
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select an option from 1 to 9.")

if __name__ == "__main__":
    main()
