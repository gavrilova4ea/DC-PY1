import math
def calculateSaveSum(salary, spend, months, spendIncrease = 0.03):
    needSum = 0
    for i in range(1, months + 1):
        needSum -= (salary - spend)
        spend *= (1+spendIncrease)
    return(round(needSum))

salary = 5000
spend = 6000
months = 10

result = calculateSaveSum(salary, spend, months)
print(result)

