# Kirill Kaminskyi M10P1.py 10/26/2026

#input
do_program = input("Do you want to do this program? ").lower()

#function
def forecast (mnth):
    if mnth == "January" or mnth == "February" or mnth == "March":
        percent  = 0.10
    elif mnth == "April" or mnth == "May" or mnth == "June":
        percent = 0.15
    elif mnth == "July" or mnth == "August" or mnth == "September":
        percent = 0.20
    elif mnth == "October" or mnth == "November" or mnth == "December":
        percent = 0.25
    else :
        print("invalid month")
        return 0
    return percent

#process + outputs
while do_program == "yes":
    last_name = input("Enter your last name: ")
    month = input("Enter your month: ").capitalize()
    number_of_sales = float(input("Enter your number of sales: "))

    forecast_percent = forecast(month)

    next_sales = number_of_sales * (1 + forecast_percent)

    # final outputs
    print()
    print(f"Last Name: {last_name}")
    print()
    print(f"Next month sales: ${next_sales:,.2f}")

    do_program = input("Do you want to do this program? ").lower()

