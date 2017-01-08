#def to check for the party requirements
def is_party(apples , pizzas):
    if apples>10 and pizzas>5:
        return True
    else:
        return False

#def for the current party 
def throw_party():
    num_apples = input("How many apples do you have?")
    num_pizzas = input("How many pizzas do you have?")
    if is_party(num_apples,num_pizzas):
        print "Yayy! Throw a party"
    else:
        print "Go to the store now !"

#Now call the function
throw_party()
