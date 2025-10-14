def main():
    grocery_list = ['Bun', 'Butter', 'Jam', 'Cheese']

    # Adding item using append
    grocery_list.append('Tea')
    print(grocery_list)

    # Inserting at specific place
    grocery_list.insert(2,'Marmalade')
    print(grocery_list)

    # Removing an item
    grocery_list.remove('Tea')
    print(grocery_list)

    # Popping out an item at specific index
    grocery_list.pop(2)
    print(grocery_list)

    #Clear the list
    grocery_list.clear()
    print(grocery_list)


if __name__ == '__main__':
        main()