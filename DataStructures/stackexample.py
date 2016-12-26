# implementing the stack with 4 functions push , pop , isempty and size
class Stack():
    x =[]
    toppointer = -1
    def __init__(self):
        pass

    #To push an item in the stack    
    def push(self,item):
        self.x.append(item)
        self.toppointer = self.toppointer+1

    #To pop out an item in the stack and returns the popped item
    def pop(self):
        temp = self.x[self.toppointer]
        self.x[self.toppointer] = None
        self.toppointer = self.toppointer-1
        return temp

    #To check if the list is empty , returns True or False
    def isempty(self):
        if(self.toppointer) == -1:
            return True
        else:
            return False

    #Returns the size of the stack
    def sizestack(self):
        if self.isempty():
            return 0
        else:
            return self.toppointer+1

    def printstack(self):
        return self.x

#Instantiate the stack
mystack =  Stack()

#Push an item in the stack
mystack.push(10)
print "The stack after pushing the item is" , mystack.printstack()
print "The size of the stack after pushing is " ,mystack.sizestack()


#Pop out the last item
print "The popped item is", mystack.pop()
print "The stack after popping the item is" ,mystack.printstack()

#Size of the stack
print "The size of the stack is " ,mystack.sizestack()



