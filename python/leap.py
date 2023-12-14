year=int(input("enter the year:"))
if((year%4==0)&(year%100==0)):
    print("is a leap year",year)
else:
    print("is not leap year",year)
