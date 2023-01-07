booking_of = {
        "1" : "Flights",
        "2" : "Attractions",
        "3" : "Car",
        "4" : "Hostels",
        "5" : "Flight and hotel together",
        "6" : "Airport Taxi"
}

print(booking_of)

booking_input = input("choose the serial number of the booking type drom the list: ")


def travel():

    if booking_input == "1":
        from flights import Flights

    elif booking_input == "2":
        from attractions import Attractions
        
    elif booking_input == "3":
        from car import Car

    elif booking_input == "4":
        from hotels import Hotels

    elif booking_input == "5":
        from flightsplushotels import FlightnHotels

    elif booking_input == "6":
        from car import Car

    else:
      print("Wrong input")

    

travel()
    
