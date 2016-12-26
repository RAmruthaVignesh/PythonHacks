class computer(object):
    def __init__(self, color , mnftr):
        self.color = color
        self.mnftr = mnftr
        self.os = ""

    def install_os(self,new_os):
        self.os = new_os

    def which_os(self):
        return self.os

c = computer("Black" , "Lenovo")
c.install_os("windows")
print c.which_os()

#Interitance of computer class to another class
class apple(computer):
    def __init__(self,color):
        # Inherit Computer's init method
        # So, call the init method of our superclass
        computer.__init__(self,color,"Mac")
        self.ilife_installed = False

    def install_ilife(self):
        self.ililfe_installed = True

mycomputer = apple("silver") #instantiation
yourcomputer = apple("white")
print mycomputer.mnftr # Macintosh
print yourcomputer.mnftr # Macintosh

mycomputer.install_os("OS X")
print mycomputer.os #OS X
print yourcomputer.os# ""
        