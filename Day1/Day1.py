from day1data import Data

def main():
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

    print(total_difference)

main()