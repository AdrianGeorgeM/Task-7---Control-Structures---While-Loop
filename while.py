# Initialize the total sum of numbers and the count of numbers entered
total_sum = 0
count = 0

# Use a while loop to continually ask for numbers
while True:
    # Ask the user to enter a number
    number = input("Enter a number (or -1 to stop): ")

    # Check if the user entered '-1'. If so, stop asking for more numbers
    if number == "-1":
        break

    # Convert the entered number to a float and add it to the total sum
    total_sum += float(number)

    # Increment the count of numbers entered
    count += 1

# Calculate the average if at least one number was entered
if count > 0:
    average = total_sum / count
    print("The average of entered numbers is:", average)
else:
    print("No numbers were enttered.")
