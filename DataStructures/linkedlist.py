class node(object):
    data  = None
    ptr =  None


class LL(object):
    head = None

    def __init__(self):
        pass

    def insert(self , position,value):
        # Insertion when the linked list is empty

        if self.head == None:
            mynode = node()
            mynode.data = value
            mynode.ptr = None
            self.head = mynode
        else:
            sizell=self.size()
            #Insertion in the beginning
            if position == 0:
                mynode = node()
                mynode.data=value
                mynode.ptr = self.head
                self.head = mynode
            #insertion when the position is provided
            elif position <= sizell:
                mynode = node()
                prevnode = node()
                mynode.data = value
                temp=self.traverseposition(position)
                mynode.ptr=temp[0]
               #print "mynode pointer is" , mynode.ptr.data
               #print "position is" , position
                temp = self.traverseposition(position-1)
                prevnode = temp[0]
               #print "prevnode data is" , prevnode.data
                prevnode.ptr = mynode
            else:
                print "Enter the correct postion"

#This function inserts the value at the end of the linkedlist
    def insertend(self,value):
        mynode = node()
        mynode.data= value
        mynode.ptr = None
        temp= self.traverseposition("full")
        lastnode = temp[0]
        lastnode.ptr = mynode

#This fuction deletes the value at the end of the linkedlist
    def delend(self):
        llsize=self.size()
        temp = self.traverseposition(llsize-2)
        lastnode=temp[0]
        lastnode.ptr = None

#This function deletes the  node at the given position
    def delete(self,position):
        sizell = self.size()              
        if (sizell>0 and position<=sizell and position>=0): #Checks boundary conditions
            temp = self.traverseposition(position)
            currentnode = temp[0]
            if position == 0: #Deleting the first node
                temp = self.traverseposition(position+1)
                nextnode = temp[0]
                self.head = nextnode
            elif position >0 :# Function to delete the nodes from 2nd to last
                temp = self.traverseposition(position-1)
                prevnode = temp[0]
                if position <sizell: #Deleting nodes in the middle
                    temp = self.traverseposition(position+1)
                    nextnode = temp[0]
                    prevnode.ptr = nextnode
                else: # Deletes last node
                    prevnode.ptr = None
        else:
            print "Invalid position"




#This function returns the size of the linkedlist
    def size(self):
        sizecount = 0
        temp = self.traverseposition("full")
        size = temp[1]+1
        return size



# Function to traverse through the linked list . It takes in position of the node and gives the size and node at the given position
    def traverseposition(self,location):
        #print "location is" , location
        loccount = 0
        tempnode = self.head
        while (loccount <location and tempnode.ptr !=None): # When the size till the given position is requested
            tempnode = tempnode.ptr
            loccount = loccount+1

        while (loccount == "full" and tempnode.ptr !=None): # When the size of the LL is requested
            tempnode = tempnode.ptr
            loccount = loccount+1

        return [tempnode,loccount]

#This function prints the linked list
    def printll(self):
        tempnode = self.head
        x=[]
        def traversenode(tnode):
            if tnode.ptr != None:
                x.append(tnode.data)
                tnode = tnode.ptr
                traversenode(tnode)
            else:
                x.append(tnode.data)
        traversenode(tempnode)
        print "The Linked list is ",x

newlist = LL()
newlist.insert(0,2)
newlist.insert(0,1)
newlist.insert(1,1.5)
newlist.insertend(3)
newlist.insert(3,2.5)
newlist.printll()
print "The size of the linked list is" , newlist.size()
newlist.delend()
print "The LL after deleting the last node is"
newlist.printll()
print "The size of the linked list after deleting the last node is" , newlist.size()
newlist.delete(2)
print "The LL after deleting node in 2nd position"
newlist.printll()
print "The size of the linked list after deleting node in 2nd position ", newlist.size()
newlist.delete(0)
print "The LL after deleting first node"
newlist.printll()
print "The size of the linked list after deleting 1st node" , newlist.size()
newlist.delete(100)

# print "--------"
# newlist.insert(1,300)
# newlist.printll()


