# Kirill Kaminskyi M10P4.py 10/26/2026

#input
do_program = input("Do you want to do this program? ").lower()

sum_of_market_values = 0
sum_of_assessed_values = 0

#function
def house (location, price:float):
   if location == "cook":
        value  = 0.90
   elif location == "dupage":
        value = 0.80
   elif location == "mchenry":
        value = 0.75
   elif location == "kane":
        value = 0.60
   else:
        value = 0.70

   final_value = price * value

   return final_value

#process + outputs
while do_program == "yes":
    county = input("Enter your county: ").lower()
    market_value = float(input("Enter your market value: "))

    assessed_value = house(county, market_value)

    sum_of_market_values += market_value
    sum_of_assessed_values += assessed_value

    print(f"{"County:":<20} {"Market value:":<20}  {"Assessed value:":<20}")
    print(f"{county:<20} {market_value:<20,.2f}  ${assessed_value:<20,.2f}")

    do_program = input("Do you want to do this program? ").lower()

# final outputs
print()
print(f"Sum of market value: ${sum_of_market_values:,.2f}")
print(f"Sum of assessed value: ${sum_of_assessed_values:,.2f}")