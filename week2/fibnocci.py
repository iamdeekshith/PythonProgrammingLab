n=int(input("enter the value of n "))
a=0
b=1
while(n>0):
  print(a)
  new=a+b
  a=b
  b=new
  n-=1
