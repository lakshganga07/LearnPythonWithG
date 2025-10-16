def main():
    grocery_list = ['Bun', 'Butter', 'Jam', 'Cheese','Jam']
    num_list=[8,56,25,12,0]

    # Sort
    num_list.sort()
    print(num_list)

    #Reverse Sort
    num_list.sort(reverse=True)
    print(num_list)

    # Reverse
    print('Before Reversing :')
    print(grocery_list)
    grocery_list.reverse()
    print('After Reversing :')
    print(grocery_list)

    # Find index of item
    idx=grocery_list.index('Cheese')
    print(' The index of cheese is ',idx)

    # Find count of item
    cnt = grocery_list.count('Jam')
    print(' The count of Jam is ', cnt)

if __name__ == '__main__':
        main()