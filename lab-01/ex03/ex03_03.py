def create_typle_from_list(lst):
    return tuple(lst);

input_list = input("Enter numbers of the list separated by commas: ");
numbers = list(map(int, input_list.split(",")));

my_tuple = create_typle_from_list(numbers);
print("List: ", numbers);
print("Tuple: ", my_tuple);