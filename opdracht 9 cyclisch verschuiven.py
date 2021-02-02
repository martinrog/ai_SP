def verschuiven(n,ch):
    print(ch[n:])
    print(ch[:n])
    return ch[n:] + ch[:n]


print(verschuiven(1,"11110"))



"""" ik wil dat als n> 0, de hele reeks n plekjes naar links schuift. Hetzelfde als n < 0, maar dan naar rechts.
 
 maar in het eerst geval, moet het getal op index 0, op de laatste index komen"""

# for bit in (range(len(str(new_lst)))):
#     print(bit)
