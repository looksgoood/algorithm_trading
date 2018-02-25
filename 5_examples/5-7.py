def add_start_to_end(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    
    return total

print(add_start_to_end(-10, 10))
print(add_start_to_end(1, 10))