def main():
    # Create Record
    Student_Record={101:"Harry",102:"Ron",103:"Hermoine"}
    print(Student_Record)

    # To print all  the keys
    print("The keys in the Dictionary are : ",Student_Record.keys())

    # To print all  the Values
    print("The values in the Dictionary are : ",Student_Record.values())

    # To print all  the entire dictionary
    print("The items in the Dictionary are : ",Student_Record.items())

    # To print a particular record with key
    print("The name of rollno 101 is : ",Student_Record[101])

    # To add new record to dictionary
    Student_Record[104]="Neville"
    print("The new dictionary is : ",Student_Record)
if __name__ == '__main__':
        main()