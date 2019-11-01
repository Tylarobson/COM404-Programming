print ("How many miles must i travel..")
miles_to_travel = int(input())

miles_left = miles_to_travel

print ("I will count the miles..")

while (miles_left > 0 ):
    print ("I have", miles_left, "miles to go before i reach the base")
    miles_left = miles_left - 1

print("I have arrived at the secret headquarters of the MIB", miles_left, "miles_left")
print ("Its time to sneak in")
