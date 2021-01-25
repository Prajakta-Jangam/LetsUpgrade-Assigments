num = int(input("Enter the number "))
factorial=1
if num <0:
 print("Factorail does not exits for negative number")
elif num==0:
 print("Factorial of 0 is 1")
else:
 for i in range(1,num+1):
  factorial= factorial*i
 print("Fatorial is",factorial)
 
 
 
 

