f = [0,1,1,1,1,2,2,2,2,2,3,3,4,4,4,4]

def count(lst, x):
    aantal = 0
    for number in lst:
        if number == x:
            aantal += 1
    print(f"Het nummer {x} komt {aantal} keer voor in de lijst.")


#count(f,1)

# b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.

def diff():
    pass













# def diff(lst,index0=0, index1=1, index2=2):
#     x = lst[index1] - lst[index0]
#     print(x)
#     y = lst[index2] - lst[index1]
#     print(y)
#     if y > x:
#         x = y
#         diff(lst, index1+1,index2+1)
#     else:
#         diff(lst, index1+1,index2+1)
#
#     return print(x)

# diff([1,2,5,8,20])