# Assignment 7 "Write a program in java with class Employee and do the following operations on it
# 		1) Accept Basic_Salary from user using 3 Objects of  Employee class using constructor.
# 		2) Create a function called calculateSalary() which calculate the PF and HRA on the salary of employee, and find out total_salary,
#   Criterias are salary between 8000 and 15000 then HRA 4% on Salary and DA % 5 on Salary
# 	salary between 16000 and 25000 then HRA 5% on Salary and DA 6 % on Salary

# 		3) Print Basic_salary, HRA, DA,Total_Salary by calling function PrintInfo() for all 3 Employees'"


class Employee:
    def __init__(self, emp_name, basic_salary, hra=0, da=0, total_salary=0, pf=0):
        self.emp_name = emp_name
        self.basic_salary = basic_salary
        self.hra = hra
        self.da = da
        self.total_salary = total_salary
        self.pf = pf

    def calculateSalary(self):
        if 8000 <= self.basic_salary <= 15000:
            self.hra = self.basic_salary*0.04
            self.da = self.basic_salary*0.05
            self.total_salary = self.basic_salary+self.hra+self.da

        elif 15000 < self.basic_salary <= 25000:
            self.hra = self.basic_salary*0.05
            self.da = self.basic_salary*0.06
            self.total_salary = self.basic_salary+self.hra+self.da

        else:
            self.basic_salary = self.basic_salary

        self.pf = 0.12*self.basic_salary
        self.total_salary = (self.basic_salary+self.hra+self.da)-self.pf

    def PrintInfo(self):
        print(
            f"Employee Name: {self.emp_name}\nBasic Salary: {self.basic_salary}\nHRA: {self.hra}\nDA: {self.da}\nPF: {self.pf}\nTotal Salary: {self.total_salary}")


# e = Employee("Roshan", 15000)
# e.calculateSalary()
# e.PrintInfo()

for i in range(1):
    name = input("Enter Name: ")
    sal = int(input("Enter Basic Salary:"))
    e = Employee(name, sal)
    e.calculateSalary()
    print('-'*10, "Salary Breakup", '-'*10, )
    e.PrintInfo()
    print('-'*30)
