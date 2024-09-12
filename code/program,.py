'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''
import packaging
import json

with open('data\packaging.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()

lines = content.splitlines()


# Print the content
parsed_list = []
for package in lines:
    package_parsed = packaging.parse_packaging(package)
    number_of_items = packaging.calc_total_units(package_parsed)
    item_name = packaging.get_unit(package_parsed)
    print(package, "=> total units:", number_of_items, item_name)
    parsed_list.append(package_parsed)


print("\n\n", parsed_list)

with open('packaging_export.json', 'w') as file:
    # Serialize the list to JSON and write it to the file
    json.dump(parsed_list, file, indent=4)