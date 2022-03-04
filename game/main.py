from Board import board
def main():
    my_baord = board()
    done = False
    while not done:
        done = bool(input("exit?"))
    print("welecome to snake!")


if __name__ =='__main__':
    main()