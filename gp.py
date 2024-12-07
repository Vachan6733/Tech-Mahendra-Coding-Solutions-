def gp(s,t,n):
    r = t/s #common ratio
    a = s/r #first term
    nth = a * (r ** (n-1))
    return nth

def main():
    se = float(input("enter secode term "))
    th = float(input("enter third term "))
    no = int(input("enter the nth term to find "))
    nth = gp(se,th,no)
    print(f"The {no}th term of the gp is : {nth}")

if __name__=="__main__":
    main()
