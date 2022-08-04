# Assignment 6 "Write a Java method to compute the future
# investment value at a given interest rate for a specified number of years.
# 		Sample data (Monthly compounded) and Output:
# 		Input the investment amount: 1000
# 		Input the rate of interest: 10
# 		Input number of years: 5

# 		Expected Output:

# 		Years    FutureValue
# 		1            1104.71
# 		2            1220.39
# 		3            1348.18
# 		4            1489.35
# 		5            1645.31 "

# fv=pv(1+i)t

amount = int(input("Enter investment amount:"))
interest = int(input("Enter rate of interest:"))
years = int(input("Enter number of year:"))

# calculate interest on monthly basis
interest = (interest/100)/12

print("-"*20)
print("Years\tFuture Value")
# loop for calculating future value per year
for year in range(1, years+1):
    # calculate number of months
    n = year*12
    # formula for calculate future value
    fv = amount*((1+interest)**n)
    print(year, "\t", round(fv, 2))
print("-"*20)
