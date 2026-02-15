def main():
    # Creating a Tuple
    Student_Record=['Harry Potter','Gryffindor','21']
    print(Student_Record)

    # Accessing items
    Name=Student_Record[0]
    Roll_No=Student_Record[-1]
    print(' Name of the student : ',Name)
    print(' Roll Number of the student : ',Roll_No)

    # Slicing (Choose first 2 items)
    First_two_items=Student_Record[0:2]
    print('The top 2 items are :', First_two_items)

if __name__ == '__main__':
        main()