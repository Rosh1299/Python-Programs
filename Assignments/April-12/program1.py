# Assignment 1 " Write a  program which initialization earning of an employee.
# The program should calculate the income tax to be paid by the
# employee as per the criteria given below:
# 		Slab rate              IT rate
# 		Upto Rs. 50,000        Nil
# 		Upto Rs. 60,000        10% on additional amount
# 		Upto Rs. 1,50,000      20% on additional amount
# 		Above Rs. 1,50,000     30% on additional amount
# 		Hint: 	- Run: - java calculates 1,25,000
# 		Result: - income tax is …………………………….


earning = int(input("Please enter your yearly earning:"))
if earning <= 50000:
    print("your income tax is nil.")
elif 50000 < earning <= 60000:
    tax = (earning-50000)*10/100
    print(f"Your income tax is {tax} rupees.")
elif 60000 < earning <= 150000:
    tax = (earning-60000)*20/100
    print(f"Your income tax is {tax} rupees.")
elif earning > 150000:
    tax = (earning-150000)*30/100
    print(f"Your income tax is {tax} rupees.")
