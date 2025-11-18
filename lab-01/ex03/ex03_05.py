def count_num_appearance(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Enter elements of the list separated by space: ");
word_list = input_string.split();

num_appearance = count_num_appearance(word_list);
print("Number of appearances of each element:", num_appearance);