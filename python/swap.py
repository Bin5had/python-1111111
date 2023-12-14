a=[1,2,3,4,5,6,7,8]
print(a)
n=a[7]
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("new list is:")
print(a)
