#Get the input light color
light_color = raw_input("what is the color of the light?")
#Change it to lower case
light_color = light_color.lower()
if light_color == "red":
    print("You need to stop!")
elif light_color == "orange":
    print("you need to wait..")
elif light_color == "green":
    print("Gooo!")
else:
    print ("which country you are in ?")
