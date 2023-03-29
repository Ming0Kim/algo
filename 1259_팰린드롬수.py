while True:
    a = input()
    if a == '0':
        break
    else:
        if a[::-1] == a:
            print('yes')
        else:
            print('no')
