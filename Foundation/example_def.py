base = 10
exp = 4
# Example of basic def with no parameter
def hello_world():
    base = 20
    print "inside of hello_world base is" , base
    return "Hello World!"

print hello_world()
print "outside of hello_world base is" , base

#Example of def with parameters
def compute_exp(base,exp):
    print "inside of compute_exp base is" , base
    print "inside of compute_exp exp is" , exp
    return base**exp

print "outside of compute_exp base is" , base
print "outside of compute_exp exp is" , exp
print compute_exp(10,2)




