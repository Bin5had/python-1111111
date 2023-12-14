y=int(input("current year:"))
c=int(input("future year:"))
for year in range(y,c):
    if((year%4==0)&(year%100!=0)|(year%400==0)):
        print(year)
