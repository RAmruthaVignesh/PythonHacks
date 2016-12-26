#This program represents a 2d point , x and y coordinate
class point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def return_string(self):
        print "The 2D point is:" ,str((self.x,self.y))

    def move_point(self,deltax,deltay):
        self.x = deltax+self.x
        self.y = deltay+self.y
        return (self.x,self.y)



point1=point(5,4)
point1.return_string()
print "After moving the point" , point1.move_point(0.3,0.5)
