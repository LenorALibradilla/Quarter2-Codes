places= []
for x in range(5):
    destination = input("Destination for trip {}: ".format(x + 1))
    places.append(destination)
print("\nOriginal Travel Itinerary:")
for i, place in enumerate(places, start=1):
    print(" {}. {}".format(i, place))
    
print("\nLet's update your 2nd and 5th destinations.")
places2= input(" New destination for trip 2: ")
places5 = input("New destination for trip 5: ")

places[1] = places2
places[4] = places5

print("\nUpdated Travel Itinerary:")
for i, place in enumerate(places, start=1):
    print(" {}. {}".format(i, place))

       


