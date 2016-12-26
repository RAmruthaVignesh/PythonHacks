# Problem Statement:
# If you're taller than 56", you can ride Space Mountain at Disneyland.
# If you're shorter, you cannot.
# Additionally if you are greater than 150 inches, you are super tall and deserve a witty message.

#Get height input
height = input("what is your height?")

#height greater than 150
if height >150:
    print(" wow ! you are super tall")

#Check permission to ride
if height <= 56:
    print ("No ! you are too short to ride")
else:
    print("Yes")
