print('Enter any integer: ')
n = str(input().strip())
num_places = len(n)

for i in range(num_places) :
    x = num_places - i
    if x >= 10 :
        suffix = "Billion "
    elif x <= 9 and x >= 7 :
        suffix = "Million "
    elif x == 6  :
        suffix = "Hundred "
    elif x == 5  :
        suffix = "Thousand "
    elif x == 4:
        suffix = "Thousand "
    elif x == 3 :
        suffix = "Hundred "
    else :
        suffix = ""
    # the second to last digit will always be the tens, which have special naming
    if i != num_places - 2 :
        if n[i] == '1' :
            # don't make newline
            print("One " + suffix, end='')
        elif n[i] == '2' :
            print("Two " + suffix, end='')
        elif n[i] == '3' :
            print("Three " + suffix, end='')
        elif n[i] == '4':
            print("Four " + suffix, end='')
        elif n[i] == '5':
            print("Five " + suffix, end='')
        elif n[i] == '6':
            print("Six " + suffix, end='')
        elif n[i] == '7':
            print("Seven " + suffix, end='')
        elif n[i] == '8':
            print("Eight " + suffix, end='')
        elif n[i] == '9':
            print("Nine " + suffix, end='')
        else :
            # if n[i] is 0, print "and"
            print(" and ", end='')

    else :
        if n[i] == '1' :
            if n[i+1] == '0' :
                print("Ten ", end='')
            if n[i+1] == '1' :
                print("Eleven ", end='')
            if n[i+1] == '2' :
                print("Twelve ", end='')
            else :
                if n[i+1] == '3' :
                    print("Thir", end='')
                if n[i+1] == '4' :
                    print("Four", end='')
                if n[i+1] == '5' :
                    print("Fif", end='')
                if n[i+1] == '6' :
                    print("Six", end='')
                if n[i+1] == '7' :
                    print("Seven", end='')
                if n[i+1] == '8' :
                    print("Eigh", end='')
                if n[i+1] == '9' :
                    print("Nine", end='')
                print("teen")
            break

        elif n[i] == '2' :
            print("Twenty ", end='')
        elif n[i] == '3' :
            print("Thirty ", end='')
        elif n[i] == '4':
            print("Fourty ", end='')
        elif n[i] == '5':
            print("Fifty ", end='')
        elif n[i] == '6':
            print("Sixty ", end='')
        elif n[i] == '7':
            print("Seventy ", end='')
        elif n[i] == '8':
            print("Eighty ", end='')
        elif n[i] == '9':
            print("Ninety ", end='')
        else :
            # if n[i] is 0, print "and"
            print(" and ", end='')