# Corrected code after using Cursor AI diagnosis

def process_averages(data_list):
    # Bug previously: tried to divide by len(data_list) even when empty, crashing on zero
    if not data_list:
        return 0
    
    total = 0
    # Bug previously: `for i in range(len(data_list) + 1)` causing IndexError
    for i in range(len(data_list)):
        total += data_list[i]
        
    return total / len(data_list)

if __name__ == "__main__":
    nums = [10, 20, 30, 40]
    print("Calculated Average:", process_averages(nums))
    print("Empty List Average:", process_averages([]))
