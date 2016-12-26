class person(object):
    def __init__(self,first,last):
        self.firstname = first
        self.lastname =last

    def  name(self):
        return  self.firstname + "" + self.lastname

class employee(person):
    def __init__(self,first,last,staffnum):
        person.__init__(self,first,last)
        self.staffnumber = staffnum

    def getemployee(self):
        return self.name() + "," + self.staffnumber

staff1 = employee("Amrutha" , "Vignesh" , "2714111")
print staff1.getemployee()
