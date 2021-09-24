# 5-Write a program to sort a list of dictionaries using Lambda.  
# Original list of dictionaries :[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

dict = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :", dict)

sorted_dict = sorted(dict, key = lambda x: x['color'])
print("Sorting the List of dictionaries :", sorted_dict)
