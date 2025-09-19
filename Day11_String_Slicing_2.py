def main():
    name = "Harry Potter"

    # Part Slicing by skipping letters
    Skip_every_two = name[0:5:2]
    print("Word with skipped words:", Skip_every_two)

    # Reverse words with negative index
    Reverse_letters = name[::-1]
    print("Reversed word :", Reverse_letters)

if __name__ == '__main__':
    main()