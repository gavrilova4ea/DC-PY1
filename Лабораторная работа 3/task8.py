money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
while money_capital >= spend:
    money_capital -= spend
    money_capital += salary
    spend *= (1 + increase)
    month = month + 1

print(month)
