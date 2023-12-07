#(i)

#(ii)
def sum_of_natural_numbers(n):   
    if n <= 1:
        return n
    else:
        return n + sum_of_natural_numbers(n - 1)

# Test with n = 4
n = 4
result = sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is: {result}")
#(iii)
numbers = [1, 3, 6, 7, 9]
del numbers[2]
numbers.append(10)
print(numbers) 

#(iv)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
#(v)
student_info ={
  "name":"Alice",
  "age": 20,
  "grade": "A"
}
print(student_info)

student_info['age'] = 25
print(student_info)

#(vi)
original_dict={
    "a":3,
    "b":8,
    "c":2,
    "d":7
}
new_dict = {key: value for key, value in original_dict.items() if value > 5}
print(new_dict)
