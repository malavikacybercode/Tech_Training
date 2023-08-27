def pre(list):

    if not list:
        print("''")
    
    a = list[0]
    for i in range(1, len(list)):
        while list[i].find(a) != 0:
            a = a[:-1]
            if not a:
                print("''")
    print(a)

list= ["light","live","liver"]
a= pre(list)
