n=int(input())
x=0;
y=1;
for i in range(1,n):
  c=x+y
  x=y
  y=c
  print c
