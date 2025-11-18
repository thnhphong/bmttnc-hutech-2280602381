#delete an item in dictionary 
def delete_item_dict(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'};
key_to_delete = 'city';
result = delete_item_dict(my_dict, key_to_delete);

if result: 
    print(f"Item with key '{key_to_delete}' has been deleted.", my_dict);
else:
    print(f"Key '{key_to_delete}' not found in the dictionary.");