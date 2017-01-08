#This example explains the super method and inheritance concept

class polygons(object):
    '''This class has functions that has the functionalities of a polygon'''
    def __init__(self,number_of_sides):#constructor
        self.n = number_of_sides
        print "The total number of sides is" , self.n

    def interior_angle(self):
        '''This function calculates the interior angle of a polygon'''
        return (180*(self.n-2))/self.n 

    def exterior_angle(self):
        '''This function calculates the exterior angle of a polygon'''
        return 360/self.n

    def number_of_diagonals(self):
        '''This function calculates the number of diagonals in a polygon'''
        return ((self.n**2) - (3*self.n))/2

class rectangle(polygons):
    '''This class inherits all the functionalities of a polygon'''

    def __init__(self,length,breadth):
        number_of_sides = 4
        self.l = length
        self.b = breadth
        super(rectangle,self).__init__(number_of_sides)

    def interior_angle(self):
        '''This function calculates the interior angle of a rectangle'''
        return super(rectangle,self).interior_angle()

    def area(self):
        '''This function calculates the area'''
        return self.l*self.b

class square(rectangle):
    '''This class inherits all the functionalities of rectangle class'''
    def __init__(self,side):
        self.side=side
        super(square,self).__init__(self.side,self.side)

    def interior_angle(self):
        return super(square,self).interior_angle()

    def area(self):
        return super(square,self).area()

class rhombus(square):
    pass


#Testcases
rect= rectangle(5,4)
print "The interior angle of the rectangle is" ,rect.interior_angle()
sq = square(5)
print "The interior angle of the square is" ,sq.interior_angle()
rh = rhombus(10)
print "The area of the rhombus is" ,rh.area()




