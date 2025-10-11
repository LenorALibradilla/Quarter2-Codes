distance = float(input("Enter the distance in kilometers:"))
rate = float(input("Enter the rate per kilometer:"))  # Rate per kilometer
delivery_fee = distance * rate
print(f"Total Delivery Fee: ₱{delivery_fee:.2f}")