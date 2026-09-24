from checkmate import checkmate

def main():

    

    board1 = """\
R...
.K..
..P.
....\
"""
    print("Board1")
    checkmate(board1)

    board2 = """\
...
.K.
...\
"""
    print("Board2")
    checkmate(board2)

    board3 = """\
ABCD
12K4
กข..
..คง\
"""
    print("Board3")
    checkmate(board3)

    board4 = ""
    print("Board4")
    checkmate(board4)

    board5 = """\
.....
.K...
.....\
"""
    print("Board5")
    checkmate(board5)

    board6 = """
🤡R🤡🤡
🤡🤡K🤡
🤡🤡🤡P
🤡🤡🤡🤡\
"""
    print("Board6")
    checkmate(board6)

    board7 = """\
K..K
.KK.
....
....\
"""
    print("Board7")
    checkmate(board7)



if __name__ == "__main__":
    main()
