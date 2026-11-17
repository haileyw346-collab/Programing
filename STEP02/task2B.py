#Hailey Wilson
#11/13/26
#Road Trip Calculator
#calculates gas, cost per person, and dricing time for a road trip.

AVERAGE_SPEED = 55

#input
destination = input("Destination: ")
distance = float(input("Trip distance(miles): "))
miles_per_gal = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
people = int(input("Number of people splitting the cost: "))

#processing
gallons = distance / miles_per_gal
gas_cost = gallons * gas_price
cost_per_person = gas_cost / people
driving_time = int(distance / AVERAGE_SPEED * 60)
hours = driving_time//60
minutes = driving_time%60
round_gas = gas_cost*2

#output
print(f"\n--- Trip to {destination} ---")
print(f"Gallons of gas:   {gallons}")
print(f"Gas cost:         ${gas_cost}")
print(f"Cost per person:  ${cost_per_person}")
print(f"Driving time:     {hours} hr {minutes} min (at {AVERAGE_SPEED} mph)")
print(f"Round trip gas:   ${round_gas}")
