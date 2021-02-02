def tekstcheck():
    t1= input("Geef een string:")
    t2= input("Geef een string:")
    index = 0
    for i in t1:
        if i != t2[index]:
            e = t1.index(i)
            return print(f"Het verschil zit op index: {e}")
        else:
            index += 1


tekstcheck()