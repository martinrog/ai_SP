def fizz():
    for i in range(40):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)

fizz()