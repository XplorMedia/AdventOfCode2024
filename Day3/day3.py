from day3data import Data

def Day3_first_star(text):
    index = 0
    results = []
    multiplied_results = []
    sum_of_multiplied_results = 0
    
    while True:
        # Find next occurrence of "abc("
        index = text.find("mul(", index)
        if index == -1:
            break
            
        first_num = ""
        second_num = ""
        pos = index + 4  # Skip past "abc("
        
        # Get first number
        while pos < len(text) and len(first_num) < 3:
            if text[pos].isdigit():
                first_num += text[pos]
                pos += 1
            else:
                break
                
        # Check for comma
        if pos < len(text) and text[pos] == ',':
            pos += 1  # Skip comma
            
            # Get second number
            while pos < len(text) and len(second_num) < 3:
                if text[pos].isdigit():
                    second_num += text[pos]
                    pos += 1
                else:
                    break
            
            # Check for closing parenthesis
            if pos < len(text) and text[pos] == ')':
                if first_num and second_num:  # Make sure both numbers exist
                    results.append((first_num, second_num))
                    value_to_add = int(first_num) * int(second_num)
                    multiplied_results.append(value_to_add)
                    sum_of_multiplied_results += value_to_add
        
        index += 4  # Move past current "abc("
    print (results)
    print(sum_of_multiplied_results) 
    return results

#Day3_first_star(Data)

def Day3_second_star(text):
    index = 0
    results = []
    multiplied_results = []
    sum_of_multiplied_results = 0
    is_enabled = True
    
    while index < len(text):
        # Check for state change instructions
        if text[index:].startswith("do()"):
            is_enabled = True
            index += 4
            continue
            
        if text[index:].startswith("don't()"):
            is_enabled = False
            index += 7
            continue
        
        # Only process abc patterns if currently enabled
        if is_enabled and text[index:].startswith("mul("):
            first_num = ""
            second_num = ""
            pos = index + 4
            
            # Get first number
            while pos < len(text) and len(first_num) < 3:
                if text[pos].isdigit():
                    first_num += text[pos]
                    pos += 1
                else:
                    break
                    
            # Check for comma
            if pos < len(text) and text[pos] == ',':
                pos += 1
                
                # Get second number
                while pos < len(text) and len(second_num) < 3:
                    if text[pos].isdigit():
                        second_num += text[pos]
                        pos += 1
                    else:
                        break
                
                # Check for closing parenthesis
                if pos < len(text) and text[pos] == ')':
                    if first_num and second_num:
                        results.append((index, first_num, second_num))
                        value_to_add = int(first_num) * int(second_num)
                        multiplied_results.append(value_to_add)
                        sum_of_multiplied_results += value_to_add
            
            index += 1
        else:
            index += 1
    print(sum_of_multiplied_results)
    return results

Day3_second_star(Data)