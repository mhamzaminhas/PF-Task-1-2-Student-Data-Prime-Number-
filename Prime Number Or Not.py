def Prime_Num():
  x=int(input("Enter any values: "))
  for i in range(2,x):
      if x%i==0:
        return -1
  else:
    totalvalue=0
    for i in range(x+1):
      totalvalue=totalvalue+1
    return "Number is prime and its sum is: ", str(totalvalue)
print(Prime_Num())