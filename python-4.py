inputs=list(map(int,input("enter the array ").split()))
for i in range(1,10):
 count=0
 for num in inputs:
  if num % i==0:
   count+=1
 
 print(f"{i}:{count}")            