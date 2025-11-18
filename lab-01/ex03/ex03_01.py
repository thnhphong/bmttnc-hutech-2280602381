def even_number_sum(list):
    sum = 0;
    for num in list: 
        if num % 2 == 0:
            sum += num;
    return sum;

input_str = input("Enter numbers separated by commas: ");
num_list = list(map(int, input_str.split(",")));
result = even_number_sum(num_list);
print("The sum of even numbers is:", result);