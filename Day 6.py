# Function to calculate sum and average
def calculate_sum_and_average(numbers):
    # Calculate the sum of numbers
    total_sum = sum(numbers)
    
    # Calculate the average of numbers
    average = total_sum / len(numbers) if numbers else 0  # Avoid division by zero
    
    return total_sum, average

# Collect input from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, user_input.split()))

# Call the function and get the sum and average
total_sum, average = calculate_sum_and_average(numbers)

# Print the results
print(f"Sum: {total_sum}")
print(f"Average: {average}")
