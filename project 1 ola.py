print("***  welcome to GRAND TRAVELLES  ***")
print()

current_location=input("enter your current location : ")
print()

dropping_point=input("enter your droping point : ")
print()

print("Our avilable packages :")
package=["daily","Rental","Outstations"]
for i in range(len(package)):
    print(i+1,package[i])
select_package=int(input("Select your package :"))
print()

print("Our avilable vehicale :")
vehicle=["Bike","Auto","Car Mini","Car Prime"]
vehicle_number=["MH12 67","MH12 89","MH12 2345","MH12 6789"]
vehicle_colour=["Black","Yellow","White","Navy Blue"]
for i in range(len(vehicle)):
    print(i+1,vehicle[i])
    print(" ","Vehicle Number: ",vehicle_number[i])
    print(" " ,"Vehicle Colour: ",vehicle_colour[i])
select_vehicle=int(input("select your vehical : "))

print()
driver_name=["Harish","Ramesh","Jayesh","Mahesh"]
phone_number=['7890653423','6789099867','8912345656','9087654367']
rating=[6,9,8,7]
feedback=["good","very good","bad","good"]
price=[200,145,275,250]
driver_location=["khed-shivapur","katraj","kopi","pune station"]
for i in range(len(driver_name)):
    print(i+1,"driver name :",driver_name[i])
    print( " ","phone number:",phone_number[i])
    print(" ","Rating :",rating[i])
    print(" ","feedback :",feedback[i])
    print(" ","price :",price[i])

select_rider=int(input("Select your rider : "))
print()

import random
km=random.randint(1,60)
print("distance between",current_location, "to",dropping_point, "is :",km,"km")
print()

rate_per_km=[8,10,12,15]
print("Your total fare is Rs.",km*rate_per_km[select_vehicle-1])
print()
print("Time for reach to :",dropping_point,km/10,"hr")
print()
import random
otp=random.randint(1000,3000)
print("Your OTP is : ",otp)
print()
otp=int(input("please give your otp :" ))
print()
print("Avilable payment mode :")
payment=["cash","phone pay","ola money wallet"]
for i in range(len(payment)):
    print(i+1,payment[i])
print()
payment_mode=input("Would you like which type of payment mode :")
print("Your payment is successfully done.")
print()
rating=int(input("Give your rating here :"))
print()
feedback=input("please give your feedback :")
print("Thank you.")