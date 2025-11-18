work_hour = float(input("Enter work hours: "))
pay_rate = float(input("Enter pay rate per hour: "));
standard_hours = 44;
over_standard_hour = max(0, work_hour - standard_hours);
salary = standard_hours * pay_rate + over_standard_hour * pay_rate * 1.5;
print("The salary is: " + str(salary));
