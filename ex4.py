# Declaring variable and value is floating number.
cars = 100.0
# Declaring variable and value is floating number.
space_in_a_car = 4.0
# Declaring variable and value is floating number.
drivers = 30
# Declaring variable and value is floating number.
passengers = 90
# Declaring variable and value is mathematical sum using previously declared variables
cars_not_driven = cars - drivers
# Declaring variable and value is mathematical sum using previously declared variables
cars_driven = drivers 
# Declaring variable and value is mathematical sum using previously declared variables
carpool_capacity = cars_driven * space_in_a_car
# Declaring variable and value is mathematical sum using previously declared variables 
average_passengers_per_car = passengers / cars_driven

# Print string and variable
print "There are", cars, "cars available."
# Print string and variable
print "There are only", drivers, "drivers available."
# Print string and variable
print "There will be", cars_not_driven, "empty cars today."
# Print string and variable
print "We can transport", carpool_capacity, "people today."
# Print string and variable
print "We have", passengers, "to carpool today."
# Print string and variable
print "We need to put about", average_passengers_per_car, "in each car."