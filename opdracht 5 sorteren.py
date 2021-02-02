def my_sort(lst):
    lst_sorted =lst.copy()

    length_lst = len(lst_sorted)

    for n in range(length_lst):

        for i in range(0,length_lst- n-1):
            c = True

            if lst_sorted[i] > lst_sorted[i+1]:

                lst_sorted[i], lst_sorted[i+1] = lst_sorted[i+1], lst_sorted[i]
                c= False
        if c:
            break

    return lst_sorted

print(my_sort([5,2,6,3,4,1,2]))

