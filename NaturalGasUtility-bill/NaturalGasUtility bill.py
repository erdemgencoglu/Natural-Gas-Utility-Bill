#Python version 3x series

#-----Month------
January=May=March=August=December=31
April=June=July=September=October=November=30
February	=28	

pricePerunit=input("Please enter Priceperunit in terms of m3:")
monthlyExpense=input("Enter Monthly Expense in terms of m3: ")
periot=input("Which can you calculate month:")
Month=eval(periot)
dailyExpense=int(monthlyExpense)/Month
invoice=(float(pricePerunit)*dailyExpense)*Month
unit=input("Lastly Enter your monetary unit: ")
print("Your invoice: ",invoice,unit,"");
