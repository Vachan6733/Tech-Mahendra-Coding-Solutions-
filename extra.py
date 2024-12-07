def find_positive_negative(arr):
    positive = [num for num in arr if num > 0]
    negative = [num for num in arr if num < 0]
    return positive, negative

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def reverse_string(string):
    return string[::-1]

def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Example Usage
array = [10, -20, 15, -5, 0, 7]
positive, negative = find_positive_negative(array)
print("Positive Numbers:", positive)
print("Negative Numbers:", negative)

sentence = "Hello world from Python"
print("Reversed Sentence:", reverse_sentence(sentence))

a, b = 5, 10
a, b = swap_without_temp(a, b)
print("Swapped values:", a, b)

num = 5
print("Factorial:", factorial(num))

string = "hello"
print("Reversed String:", reverse_string(string))

palindrome_check = "radar"
print("Is Palindrome:", is_palindrome(palindrome_check))

fib_length = 10
print("Fibonacci Sequence:", fibonacci(fib_length))
