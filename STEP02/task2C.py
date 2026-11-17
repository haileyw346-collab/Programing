#Hailey Wilson
#11/17/26
#Paycheck Calcultor
#prints a weekly pay stub with taxes taken out, plus yearly totals.

#Named constants
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52

#input
worker = input("Employee name: ")
rate = float(input("Hourly pay rate: "))
hours = float(input("Hours worked this week: "))
print()

#processing: paycheck
gross_pay = rate * hours
fed_tax = gross_pay * FEDERAL_TAX_RATE
state_tax = gross_pay * STATE_TAX_RATE
social_security = gross_pay * SOCIAL_SECURITY_RATE
medicare = gross_pay * MEDICARE_RATE
total = fed_tax + state_tax + social_security + medicare
net_pay = gross_pay - total
kept = net_pay / gross_pay * 100

#processing: yearly numbers
gross_year = gross_pay * WEEKS_PER_YEAR
net_year = net_pay * WEEKS_PER_YEAR

#output
print("=" * 32)
print(f"PAY STUB {worker}")
print("=" * 32)
print(f"Hours worked:      {hours}")
print(f"Hourly rate:       ${rate:.2f}")
print(f"Gross pay:         ${gross_pay:.2f}")
print("-" * 32)
print(f"Federal tax (10%): ${fed_tax:.2f}")
print(f"State tax (3.5%):  ${state_tax:.2f}")
print(f"Social Security:   ${social_security:.2f}")
print(f"Medicare:          ${medicare:.2f}")
print(f"Total taken out:   ${total:.2f}")
print("-" * 32)
print(f"NET PAY:           ${net_pay:.2f}")
print("=" * 32)
print(f"You keep {kept:.1f}% of what you earn.")
print(f"Yearly gross: ${gross_year:.2f}")
print(f"Yearly net:   ${net_year:.2f}")
