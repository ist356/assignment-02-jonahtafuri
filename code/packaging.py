'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''



# for index, part in enumerate(input_split):
# Input from user
    unique_items = []
    unique_quantities = []
    count = -1
    initial_entry = packaging_data.strip().lower()

    # Split input string
    entry_split = initial_entry.split("/")


    #pulling values and order of occurence (item and quantity)
    for part in entry_split:
        # Further split by "in"
        single_entry_split = part.split(" in ")
        
        for entry in single_entry_split:
            count += 1
            entry = entry.strip()
            
            # Split by space to get quantity and item
            single_entry_items = entry.split(" ")
            
            if len(single_entry_items) >= 2:
                quantity = single_entry_items[0]
                item = single_entry_items[1]
                unique_items.append(item)
                unique_quantities.append(quantity)
    
    # building out arrangement of values extracted, skipping values that are built on in second iteration
    list_of_dict = []
    for index in range(0, len(unique_items), 2):
        item = unique_items[index]
        new_dict = {item: int(unique_quantities[index])}
        list_of_dict.append(new_dict)
    if len(unique_items) % 2 == 0: # if even
        new_dict = {unique_items[-1]: int(unique_quantities[-1])}
        list_of_dict.append(new_dict)
    # print(f"ITEMS: {unique_items}")
    # print(f"QUANTITIES: {unique_quantities}")
    return list_of_dict




# print(f"\n1: {parse_packaging("12 eggs in 1 carton")}")
# print(f"\n2: {parse_packaging("6 bars in 1 pack / 12 packs in 1 carton")}")
# print(f"\n3: {parse_packaging("20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box")}")
# print(f"\n4: {parse_packaging("2 foo in 1 bar / 3 bars in 1 baz / 4 baz in 1 qux / 2 qux in 1 biz ")}")
# print(f"\n5: {parse_packaging("25 balls in 1 bucket / 4 buckets in 1 bin")}")

order = parse_packaging("25 balls in 1 bucket / 4 buckets in 1 bin")



def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''
    int_list = []
    for dictionary in package:
        # Extract the first (and only) value from each dictionary
        value = list(dictionary.values())[0]
        int_list.append(value)
    
    product = int_list[0]  # Start with the first value
    for value in int_list[1:]:  # Iterate from the second element to the end
        product *= value  # Multiply current product by the next value

    return product

calc_total_units(order)

def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    value = list(package[0].keys())[0]
    # print("VALUE", value)
    return(value)

get_unit(order)

# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")