PETROL_PRICE_PER_LITRE = 4.50

print("*** Welcome to the fuel efficiency calculator! ***\n")

name = input("Enter your name: ")

distance_travelled = float(input("Enter distance travelled in km: "))
amount_paid = float(input("Enter monetary value of fuel bought for the trip: R"))

fuel_consumed = amount_paid / PETROL_PRICE_PER_LITRE
efficiency_l_per_100_km = fuel_consumed / distance_travelled * 100
efficiency_km_per_l = distance_travelled / fuel_consumed

print("Hi, %s!" % name)
print("Your car's efficiency is %.2f litres per 100 km." % efficiency_l_per_100_km)
print("This means that you can travel %.2f km on a litre of petrol." % efficiency_km_per_l)
print("\nThanks for using the program.")