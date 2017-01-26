class queue(object):
    '''This class  implements a queue structure with its insert and remove operation'''
    def __init__(self):
        self.sample_queue = []

    def insert(self,*args):
        ''' This function takes any number of inputs and queues them . 
        It returns the queue'''
        self.x =args
        self.sample_queue.append(self.x)
        #This converts list of tuples to list
        self.sample_queue = list(sum(self.sample_queue,()))
        return self.sample_queue

    def remove(self):
        '''This function removes an element from the queue in FIFO fashion'''
        size = len(self.sample_queue)
        print "The current size of the queue is " , size
        if size >0:
            self.sample_queue = self.sample_queue[1:]
            print "The queue after removing a value is of size:" , size-1
            return self.sample_queue
        else:
            return "The queue is empty"

#Testcases
test_queue = queue()
queue_insert = test_queue.insert(3,4,5)
print "The queue after inserting values is" , queue_insert
print test_queue.remove()
print test_queue.remove()
print test_queue.remove()
print test_queue.remove()


