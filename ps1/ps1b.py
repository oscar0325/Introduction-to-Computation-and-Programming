# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:13:59 2019

@author: Lenovo
"""

current_savings = 0
month_num = 0
r = 0.04
flag = 0
annual_salary = int(input("Enter your annual salary:​"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int((input("Enter the cost of your dream home:​")))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:​"))
portion_down_payment = total_cost * 0.25
month_salary = float(annual_salary) / 12

while True:
    if current_savings < portion_down_payment :
        current_savings = current_savings * r / 12 + current_savings + month_salary * portion_saved
        month_num += 1
        if month_num % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            month_salary = float(annual_salary) / 12
    else:
        break

print("Number of months:​ {}".format(month_num))