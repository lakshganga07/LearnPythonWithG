def main():
    # Creating a list
    grocery_list=['Bun','Butter','Jam','Cheese']
    print(grocery_list)

    # Accessing items
    First_item=grocery_list[0]
    Last_item=grocery_list[-1]
    print(' First item in grocery list : ',First_item)
    print(' Last item in grocery list : ',Last_item)

    # Slicing (Choose first 2 items)
    First_two_items=grocery_list[0:2]
    print('The top 2 items are :', First_two_items)

    # Modifying an item
    modify_item=grocery_list[0]
    grocery_list[0]='Bread'
    print(' Modified ' ,grocery_list[0],' instead of ',modify_item)

    #Print Updated List
    print('The updated list is :', grocery_list)


if __name__ == '__main__':
        main()