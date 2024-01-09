# -------- This program is to implement stack functionality using list in python -------
l = []
while True:
    choice = int(input('''Enter your choice:
                1 - Push
                2 - Pop
                3 - Display top of the stack
                4 - Display full stack
                5 - Exit
                '''))

    if choice == 1:
        n = input("Enter Item to Add: ")
        l.append(n)
    elif choice == 2:
        if len(l) == 0:
            print('Empty Stack')
        else:
            p = l.pop()
            print(p)
    elif choice == 3:
        if len(l) == 0:
            print('Empty Stack')
        else:
            print(l[-1])
    elif choice == 4:
        if len(l) == 0:
            print('Empty Stack')
        else:
            print(l)
    elif choice == 5:
        break
    else:
        print('Invalid choice/operation. Please retry.')
