#Hailey Wilson
#11/13/26
#Pizza Party Planner
#Plans pizza for a party

#Named constants
SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
SLICE_PRICE = 2.26

#input: host name, number of people, and slices per person
host = input("Host name: ")
people = int(input("Number of people: "))
slices_per_person = int(input("Slices per person: "))

#processing
total_slices = people * slices_per_person
pizzas = total_slices//SLICES_PER_PIZZA
extra = total_slices%SLICES_PER_PIZZA
total_cost = (pizzas * PIZZA_PRICE) + (extra * SLICE_PRICE)
cost_per_person = total_cost / people

#output
print(f"\n=== Pizza Plan for {host}'s Party ===")
print(f"Slices needed:    {total_slices}")
print(f"Whole pizzas:     {pizzas}")
print(f"Extra slices:     {extra}")
print(f"Total cost:       ${total_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")
