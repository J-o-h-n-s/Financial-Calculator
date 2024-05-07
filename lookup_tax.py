def get_tax_data(file_name):
    with open (f'Tax brackets/{file_name}', 'r') as file:
        return file.read()

def get_tax(bracket_number):
    bracket_data = get_tax_data(f"{bracket_number}.txt")
    lines = bracket_data.splitlines()
    lookup_table = {}
    for line in lines:
        parts = line.split()
        if parts:
            key = int(parts[0] + parts[1][:3])
            value = int(parts[1][3:])
            if len(parts) > 2:
                value = int(str(value) + parts[2])
                
            lookup_table[key] = value
    return lookup_table

def find_tax_value(lookup_table, number):
    current_key = float('-inf')  
    for key in sorted(lookup_table.keys()):
        if key <= number:
            current_key = key
        else:
            break

    if current_key == float('-inf'):
        return None
    return lookup_table[current_key]

if __name__ == "__main__":
    try:
        tax_bracket = "7100"
        test_table = get_tax(tax_bracket)
        print(f"Tax table for bracket {tax_bracket}:")
        for k, v in test_table.items():
            print(f"{k}; {v}")
    except ValueError as e:
        print(e)
