#Get the name of the place
location = raw_input("Enter the name of your location: ")

#Truncate whitespace
while location[-1] == " ":
    location = location[:-1]
#Collect temperature from user
fah = raw_input("Enter the temperature in fahernheit:")

#convert string to float
fah = float(fah)

#convert fahrenheit to celcius
celcius_temp = (fah - 32.0)*(100.0 /180.0)

#Truncate to 3 decimal places 
celcius_temp = round(celcius_temp ,3)

#Recast as string so that we can concatenate
celcius_temp = str(celcius_temp)

#print the result
print "In" , location , "it is" , celcius_temp , "degree celcius"