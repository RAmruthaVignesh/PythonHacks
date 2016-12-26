#Zellers algorithm computes the day of the week on which a given date will fall (or fell).
A = input("month? \n 1.March \n 2.April \n 3.May \n 4.June \n 5.July \n 6.August \n 7.September \n 8.October \n 9.November \n 10.December \n 11.January \n 12.February -----")
B = input("Day?-----")
D = input("Century? eg. 19 for 1989----")
C = input("Year? eg. 89 for year 1989 ------")



# -- W = (13*A - 1) / 5
# -- X = C / 4
# -- Y = D / 4
# -- Z = W + X + Y + B + C - 2*D
# --R = the remainder when Z is divided by 7
W = (13*A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z%7

while R<0:
    R=R+7

Day = {0:'Sunday' , 1:'Monday' , 2:'Tuesday', 3:'Wednesday' , 4:'Thursday' , 5:'Friday' , 6:'Saturday'}

print "The entered date falls on", Day[R]