from day2data import Data

def day2_firststar():
    how_many_safe_reports = 0
    how_many_unsafe_reports = 0
    safe_values = [1,2,3]
    for report in Data.split('\n'):
        split_report = report.split(" ")
        how_many_levels = len(split_report)
        for i in range(0, how_many_levels):
            current_level = int(split_report[i])
            last_level = int(split_report [i - 1])
            if i == 0:
                continue
            if i >= 1 and i < (how_many_levels - 1):
                next_level = int(split_report [i + 1])
                if current_level > last_level:
                    if current_level - last_level in safe_values and next_level - current_level in safe_values:
                        pass
                    else:
                        how_many_unsafe_reports += 1
                        break
                if current_level < last_level:
                    if last_level - current_level in safe_values and current_level - next_level in safe_values:
                        pass
                    else:
                        how_many_unsafe_reports += 1
                        break
                if current_level == last_level or current_level == next_level:
                    how_many_unsafe_reports += 1
                    break
            if i >= 1 and i == (how_many_levels - 1):
                if current_level > last_level:
                    if current_level - last_level in safe_values:
                        how_many_safe_reports += 1
                    else:
                        how_many_unsafe_reports += 1
                        break
                if current_level < last_level:
                    if last_level - current_level in safe_values:
                        how_many_safe_reports += 1
                    else:
                        how_many_unsafe_reports += 1
                        break
                  
    print(how_many_safe_reports)

#day2_firststar()

def day2_secondstar():
    how_many_new_safe_reports = 0
    how_many_unsafe_reports = 0
    safe_values = [1,2,3]
    for report in Data.split('\n'):
        split_report = report.split(" ")
        split_report_set = []
        how_many_levels = len(split_report)
        report_set_failures = 0
        report_set_successes = 0
        for i in range(0, how_many_levels):
            split_report_to_slice = split_report[:i] + split_report[i+1:]
            split_report_set.append(split_report_to_slice)
        print(split_report_set)
        for sliced_report in split_report_set:
            if report_set_successes == 1:
                continue
            print(sliced_report)
            how_many_sliced_levels = len(sliced_report)
            for i in range(0, how_many_sliced_levels):
                current_level = int(sliced_report[i])
                last_level = int(sliced_report [i - 1])
                if i == 0:
                    print(str(i) + " - Step Success")
                    pass
                if i >= 1 and i < (how_many_sliced_levels - 1):
                    next_level = int(sliced_report [i + 1])
                    if current_level > last_level:
                        if current_level - last_level in safe_values and next_level - current_level in safe_values:
                            print(str(i) + " - Step Success")
                            pass
                        else:
                            report_set_failures += 1
                            print("fail")
                            break
                    if current_level < last_level:
                        if last_level - current_level in safe_values and current_level - next_level in safe_values:
                            print(str(i) + " - Step Success")
                            pass
                        else:
                            report_set_failures += 1
                            print("fail")
                            break
                    if current_level == last_level or current_level == next_level:
                        report_set_failures += 1
                        print("fail")
                        break
                if i >= 1 and i == (how_many_sliced_levels - 1):
                    if current_level > last_level:
                        if current_level - last_level in safe_values:
                            report_set_successes += 1
                            print(str(i) + " - Step Success")
                            print("Victory")
                        else:
                            report_set_failures += 1
                            print("fail")
                            break
                    if current_level < last_level:
                        if last_level - current_level in safe_values:
                            report_set_successes += 1
                            print(str(i) + " - Step Success")
                            print("Victory")
                        else:
                            report_set_failures += 1
                            print("fail")
                            break
        if report_set_successes >= 1:
            how_many_new_safe_reports += 1
            return True
        else:
            print("Report Status: Failed")
            
                  
    print(how_many_new_safe_reports)

#day2_secondstar()

def is_sequence_safe(nums):
    """Check if a sequence is safe (all increasing or decreasing by 1-3)"""
    if len(nums) < 2:
        return True
        
    # Check first pair to determine direction
    is_increasing = nums[1] > nums[0]
    
    # Check each adjacent pair
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        
        if is_increasing:
            if diff <= 0 or diff > 3:
                return False
        else:
            if diff >= 0 or diff < -3:
                return False
    
    return True

def is_report_safe_with_dampener(levels):
    """
    Check if a report is safe, either naturally or by removing one number.
    Returns True if safe, False if unsafe.
    """
    # Convert all levels to integers
    nums = [int(x) for x in levels]
    
    # First check if it's safe without removing anything
    if is_sequence_safe(nums):
        return True
        
    # Try removing each number one at a time
    for i in range(len(nums)):
        # Create new list without current number
        test_sequence = nums[:i] + nums[i+1:]
        if is_sequence_safe(test_sequence):
            return True
            
    return False

def count_safe_reports(data):
    safe_count = 0
    for report in data.split('\n'):
        if report.strip():  # Skip empty lines
            levels = report.split()
            if is_report_safe_with_dampener(levels):
                safe_count += 1
    print(safe_count)

count_safe_reports(Data)

def compare_versions(Data):
    # Your original function wrapped to return True/False
    def original_version(report):
        split_report = report.split(" ")
        split_report_set = []
        how_many_levels = len(split_report)
        report_set_failures = 0
        report_set_successes = 0
        for i in range(0, how_many_levels):
            split_report_to_slice = split_report[:i] + split_report[i+1:]
            split_report_set.append(split_report_to_slice)
            
        for sliced_report in split_report_set:
            if report_set_successes == 1:
                continue
            how_many_sliced_levels = len(sliced_report)
            for i in range(0, how_many_sliced_levels):
                current_level = int(sliced_report[i])
                last_level = int(sliced_report [i - 1])
                if i == 0:
                    pass
                if i >= 1 and i < (how_many_sliced_levels - 1):
                    next_level = int(sliced_report [i + 1])
                    if current_level > last_level:
                        if current_level - last_level in [1,2,3] and next_level - current_level in [1,2,3]:
                            pass
                        else:
                            report_set_failures += 1
                            break
                    if current_level < last_level:
                        if last_level - current_level in [1,2,3] and current_level - next_level in [1,2,3]:
                            pass
                        else:
                            report_set_failures += 1
                            break
                    if current_level == last_level or current_level == next_level:
                        report_set_failures += 1
                        break
                if i >= 1 and i == (how_many_sliced_levels - 1):
                    two_levels_ago = int(sliced_report [i - 2])
                    if current_level > last_level and last_level > two_levels_ago:
                        if current_level - last_level in [1,2,3]:
                            report_set_successes += 1
                        else:
                            report_set_failures += 1
                            break
                    if current_level < last_level and last_level < two_levels_ago:
                        if last_level - current_level in [1,2,3]:
                            report_set_successes += 1
                        else:
                            report_set_failures += 1
                            break
        return report_set_successes >= 1

    # Compare each report
    for report in Data.split('\n'):
        if not report.strip():
            continue
            
        orig_result = original_version(report)
        new_result = is_report_safe_with_dampener(report.split())
        
        # Only print reports where results differ
        if orig_result != new_result:
            print("\nFound differing report:", report)
            print(f"Your code says: {orig_result}")
            print(f"New code says: {new_result}")
            
            # Show what happens with each number removed
            nums = [int(x) for x in report.split()]
            print("\nAnalyzing each possible removal:")
            for i in range(len(nums)):
                test_sequence = nums[:i] + nums[i+1:]
                print(f"Removing {nums[i]} gives: {test_sequence}")
                print(f"Is this sequence valid? {is_sequence_safe(test_sequence)}")
            print("-" * 50)

compare_versions(Data)