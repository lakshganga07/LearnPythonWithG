def main():
   #for loop
    print('*******************for loop program**************************************************')
    for i in range(1,11):
        if(i==5):
            print("Oops! Found a melted chocolate at", i)
            break
        print("Chocolate :", i)

    #while loop
    print('*******************while loop program**************************************************')
    water_level=0
    while (water_level<5):
        if(water_level==3):
            print("Bubble at level", water_level, "– skipping!")
        print('water_level :' ,water_level)
        water_level+=1
if __name__ == '__main__':
    main()