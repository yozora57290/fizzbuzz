for i in range(1, 101):
    print([i, "Fizz", "Buzz", "FizzBuzz"][3 - i**2 % 3 - i**4 % 5 * 2])
