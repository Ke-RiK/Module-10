# Kirill Kaminskyi M10P3.py 10/26/2026

#input
do_program = input("Do you want to do this program? ").lower()

sum_of_msrp = 0
sum_of_final_car_price = 0

#function
def car (msrp:float, make, model, electric_car):
    if make and model == "Honda Accord":
        msrp_percent = 0.10
    elif make and model == "Toyota Rav4":
        msrp_percent = 0.15
    elif electric_car == "Y":
        msrp_percent = 0.30
    else:
        msrp_percent = 0.05

    discount_amount = msrp_percent * msrp
    discounted_price = msrp - discount_amount
    sales_tax = discounted_price * 0.07
    out_the_door_price = discounted_price + sales_tax

    return out_the_door_price

#process + outputs
while do_program == "yes":
    car_make = input("Enter car make: ").capitalize()
    car_model = input("Enter car model: ").capitalize()
    electric_vehicle = input("Enter electric vehicle Y/N: ").capitalize()
    car_msrp = float(input("Enter car msrp: "))

    final_price = car(car_msrp, car_make, car_model, electric_vehicle)

    if electric_vehicle == "Y":
        electric_vehicle = "Yes"
    elif electric_vehicle == "N":
        electric_vehicle = "No"


    sum_of_msrp += car_msrp
    sum_of_final_car_price += final_price

    print(f"{"Make:":<20} {"Model:":<20} {"Electric vehicle:":<20} {"msrp:":<20} {"Final price:":<20}")
    print(f"{car_make:<20} {car_model:<20} {electric_vehicle:<20} ${car_msrp:<20,.2f} ${final_price:<20,.2f}")

    do_program = input("Do you want to do this program? ").lower()

#final outputs
print()
print(f"The sum of total msrp is ${sum_of_msrp:.2f}")
print()
print(f"The sum of final total car price is ${sum_of_final_car_price:.2f}")
