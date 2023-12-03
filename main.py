def line_digits(line):
    left = None 
    right = None
    
    for char in line:
        if char.isdigit():
            left = char
            break 
    
    for i in range(len(line)):
        char = line[len(line) - 1 - i]
        if char.isdigit():
            right = char
            break

    return left, right

digit_pairs = []

with open("C:\\Users\\Mahamane Dicko\\Documents\\advent_of_code\\Day-1\\input.txt", 'r') as file:
    for line in file:  # This iterates over each line in the file
        left, right = line_digits(line)
        if left is not None and right is not None:
            digit_pairs.append((left, right))
            
#Creating a list using list comprehension for practice
combined_digits=[left+right for left ,right in digit_pairs]

total_sum=0
for sum in combined_digits:
    total_sum+=int(sum)
print(total_sum)
