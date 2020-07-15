list = []
nl = int(input("Enter the number of list(s)- "))
for x in range(nl):
    ele = int(input("Enter the number of elements of the list" + str(x+1) + "- "))           
    for y in range(ele):
        el = input("Element" + str(y) + "- ")
        list.append(el)
    print("The list" + str(x) + " you entered is- ")
    print(list)
