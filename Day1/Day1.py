from day1data import Data

def day1_firststar():
    left_numbers = []
    right_numbers = []
    for line in Data.split('\n'):
        left, right = line.split()
        left_numbers.append(int(left))
        right_numbers.append(int(right))
        
    sorted_left_numbers = sorted(left_numbers)
    sorted_right_numbers = sorted(right_numbers)
    
    total_difference = 0
    
    for i in range(1000):
        if sorted_left_numbers[i] == sorted_right_numbers[i]:
            continue
        elif sorted_left_numbers[i] < sorted_right_numbers[i]:
            total_difference += sorted_right_numbers[i] - sorted_left_numbers[i]
        elif sorted_right_numbers[i] < sorted_left_numbers[i]:
            total_difference += sorted_left_numbers[i] - sorted_right_numbers[i]

    #print(total_difference)

day1_firststar()

def day1_secondstar():
    left_numbers = []
    right_numbers = []
    for line in Data.split('\n'):
        left, right = line.split()
        left_numbers.append(int(left))
        right_numbers.append(int(right))
        
    sorted_left_numbers = sorted(left_numbers)
    sorted_right_numbers = sorted(right_numbers)
    
    total_similarity = 0
    
    for i in range(1000):
        number_of_matches = 0
        if sorted_left_numbers[i] in sorted_right_numbers:
            for number in sorted_right_numbers:
                if number == sorted_left_numbers[i]:
                    number_of_matches += 1
        new_similarity = number_of_matches * sorted_left_numbers[i]
        total_similarity += new_similarity

    print(total_similarity)

day1_secondstar()