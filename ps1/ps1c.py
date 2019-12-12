# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:46:04 2019

解题思路
从0-10000搜索一个数，转化为比率，计算该比率在36个月后的所得存款，与首付款进行比较。
若差值在100以内则满足条件，否则，若存款小于首付款则缩小搜索范围起点为当前比率，相反的话，则缩小搜索范围终点为当前比率。
"""
def current_saving_count(portion_save_rate, current_savings = 0,month_num = 0, r = 0.04, semi_annual_raise = 0.07):
    annual_salary = annual_salary_g
    month_salary = float(annual_salary) / 12
    for i in range(36):
        current_savings = current_savings * (1 + r / 12) + month_salary * (portion_save_rate / 10000)
        month_num += 1
        if month_num % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            month_salary = float(annual_salary) / 12
    return current_savings

def b_search(rate_low, rate_high, search_time = 1):
    while True:
        if rate_low >= rate_high:
            return False
        else:
            portion_save_rate = round((rate_high + rate_low) / 2) #使用round，使得可以满足跳出循环的条件，并将比率限制在四位有效数字以内
            if abs(current_saving_count(portion_save_rate) - portion_down_payment) <= 100:
                return portion_save_rate, search_time
            elif current_saving_count(portion_save_rate) < portion_down_payment :
                rate_low = portion_save_rate
                search_time += 1
            else current_saving_count(portion_save_rate) - portion_down_payment :
                rate_high = portion_save_rate
                search_time += 1


annual_salary_g = int(input("Enter your annual salary:​"))
total_cost = 1000000
portion_down_payment = total_cost * 0.25
if b_search(0, 10000) == False:
    print("It is not possible to pay the down payment in three years.")
else:
    rate, search_time = b_search(0, 10000)
    print("Best savings rate:​{:.4f}".format(rate / 10000))
    print("Steps in bisection search:​{}".format(search_time))