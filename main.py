def find_largest_element(arr):
    return max(arr)

def find_largest_digit(num):
    return max(map(int, str(num)))

def reverse_string(ch):
    return ch[::-1]
    
def swap_characters(s):
    return s.replace('a','e')

def main():
    arr = list(map(int,input("Enter array to find the largest element ").split()))
    res1=find_largest_element(arr)
    print(f"Largest element in the array is",res1)
    
    num=int(input("Enter number to find the largest digit "))
    res2=find_largest_digit(num)
    print(f"Largest digit in the number is ",res2)
    
    ch = input("Enter a string to reverse ")
    res3=reverse_string(ch)
    print(f"Reversed string is ",res3)
    
    s = input("Enter to swap ")
    res4=swap_characters(s)
    print(f"After swaping",res4)

if __name__ == "__main__":
    main()
