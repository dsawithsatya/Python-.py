Satya=20+10j
print("complex value :",Satya)
print(Satya.real)
print()
print()
def is_leap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
                return True
    return False
print("The given year is a leap year :")    
print(is_leap(1995))

