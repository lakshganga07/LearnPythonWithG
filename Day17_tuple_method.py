def main():
    # Tuple Methods
    Quidditch_Record=(1,0,0,0,0,1,1,1,1)

    # Count
    Cnt_Wins=Quidditch_Record.count(1)
    #Index
    Position_of_last_match=Quidditch_Record.index(1)
    print(' Number of matches won : ',Cnt_Wins)
    print(' Position in last match : ',Position_of_last_match)

if __name__ == '__main__':
        main()