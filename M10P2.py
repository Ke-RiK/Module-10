# Kirill Kaminskyi M10P2.py 10/26/2026

#input
do_program = input("Do you want to do this program? ").lower()

def calculations (lngth: float, wdth: float, hght: float):
    area = (2 * lngth * hght) + (2 * wdth * hght)

    return area

def calculations2 (lngth: float, wdth: float):
    area = lngth * wdth

    return area


while do_program == "yes":
    length = float(input("Enter length:"))
    width = float(input("Enter width:"))
    height_of_room = float(input("Enter height of the room:"))


    wall_area = calculations(length, width, height_of_room)
    celling_area = calculations2(length, width)

    gallons_needed = wall_area / 50
    gallons_needed2 = celling_area / 50

    print()
    print(f"Gallons needed for wall: {gallons_needed:,.2f} gallons")
    print(f"Gallons needed for celling: {gallons_needed2:,.2f} gallons")
    print()
    
    do_program = input("Do you want to do this program? ").lower()