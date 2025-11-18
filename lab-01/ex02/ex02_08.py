def isDivisibleBy5(binary_num):
    decimal_num = int(binary_num, 2)
    if decimal_num % 5 == 0:
        return True
    else: 
        return False
    
binary_input_string = input("Enter binary numbers separated by commas: ")
binary_num_list = binary_input_string.split(",")
divisible_by_5_list = [num for num in binary_num_list if isDivisibleBy5(num)];

if len(divisible_by_5_list) > 0:
    result = ",".join(divisible_by_5_list)
    print("Binary numbers divisible by 5 are: " + result)
else:
    print("No binary numbers divisible by 5 were found.")