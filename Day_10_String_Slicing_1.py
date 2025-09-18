def main():
    name = "Harry Potter"

    # Using positive index
    first_word = name[0:5]
    print("First Word:", first_word)

    # Using negative index
    last_word = name[-6:]
    print("Last Word :", last_word)

    # Combining
    print("Magical output:", first_word +" "+ last_word)

if __name__ == '__main__':
    main()