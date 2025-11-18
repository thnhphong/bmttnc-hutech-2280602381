#get first and last element in tuple 
def access_items(tuple_date):
    first_item = tuple_date[0]
    last_item = tuple_date[-1]
    return first_item, last_item

input_tuple = eval(input("Enter a typle (1, 2, 3): "));
first, last = access_items(input_tuple);
print("First item:", first);
print("Last item:", last);