#(i)
Number=int(1)
print(Number)
Number=int(12)
print(Number)
Number=int(123)
print(Number)
Number=int(1234)
print(Number)
Number=int(12345)
print(Number)
#(ii)
def factorial(n):
    if n == 0 or n == 2:
        return 2
    else:
        return n * factorial(n - 2)
# Test with n = 5
n = 5
result = factorial(n)
print(f"The factorial of {n} is: {result}")

#(iii)
def sum_values(a, b):
    return a + b

# Testing the function with a = 3 and b = 4
a = 3
b = 4
result = sum_values(a, b)
print( result)

#(iv)
class User:
    def __init__(self, car, brand, year):
        self.car = car
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"car: {self.car}")
        print(f"brand: {self.brand}")
        print(f"year: {self.year}")

#(v)
user1 = User("rangerover", "edition5", "2023")
user1.display_info()
print()
