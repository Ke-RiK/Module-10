# Kirill Kaminskyi M10P4.py 10/26/2026

#input
do_program = input("Do you want to do this program? ").lower()

total_ticket_price = 0

#functon
def travel (miles:float):
    if miles >= 30:
        price  = 12
    elif miles >= 20 and miles < 30:
        price = 10
    elif miles >= 10 and miles < 20:
        price = 8
    else :
        price = 5

    return price

#process + outputs
while do_program == "yes":
    last_name = input("Last Name: ")
    number_of_miles = float(input("Amount of Miles: "))

    ticket_price = travel(number_of_miles)

    total_ticket_price += ticket_price

    print()
    print(f"{"Last name:":<20} {"Miles:":<20}  {"Ticket price:":<20}")
    print(f"{last_name:<20} {number_of_miles:<20}  ${ticket_price:<20,.2f}")
    
    do_program = input("Do you want to do this program? ").lower()

#final output
print()
print(f"Total ticket price: ${total_ticket_price:,.2f}")