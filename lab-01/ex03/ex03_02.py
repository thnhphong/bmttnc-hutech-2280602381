def reverse_list(lst):
    return lst[::-1];

input_list = input("Enter elements of the list separated by commas: ");
numbers = list(map(int, input_list.split(",")));
reversed_list = reverse_list(numbers);
print("Reversed list:", reversed_list);