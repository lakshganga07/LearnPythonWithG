def main():
    name = "Harry Potter"

    # Using positive index
    first_word_intial = name[0]
    print("First Word Initial:", first_word_intial)

    # Using negative index
    last_word_initial = name[-6]
    print("Last Word Initial:", last_word_initial)

    # Combining
    print("Magical output:", first_word_intial + last_word_initial)

if __name__ == '__main__':
    main()