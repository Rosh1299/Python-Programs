# Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__()method.
import webbrowser
# Create a variable named number_of_sides and set it equal to 3.
# Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
# Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
# Print out my_triangle.number_of_sides and print out my_triangle.check_angles()


"""class Triangle:
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        sum_of_angle = self.angle1+self.angle2+self.angle3
        if sum_of_angle == 180:
            return True
        else:
            return False


my_triangle = Triangle(40, 50, 90)
print(my_triangle.check_angles())
print(my_triangle.number_of_sides)"""


# Exercise 2
# Define a class called Songs, it will show the lyrics of a song.
# Its __init__() method should have two arguments:self and lyrics.lyrics is a list. Inside your class create a method called sing_me_a_songthat prints each element of lyricson his own line. Define a varible:

# happy_bday = Song(["May god bless you, ",
#                    "Have a sunshine on you,",
#                    "Happy Birthday to you !"])
# Call the sing_me_songmehod on this variable.


"""class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)


happy_bday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
happy_bday.sing_me_a_song()"""


# Exercise 3
# Define a class called Lunch.Its __init__() method should have two arguments:selfanf menu.Where menu is a string. Add a method called menu_price.It will involve a ifstatement:

# if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
# To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().

"""class Lunch:
    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):
        if self.menu.lower() == "menu 1":
            print("Your Choice:", self.menu)
            print("Price:12.00")
        elif self.menu.lower() == "menu 2":
            print("Your Choice:", self.menu)
            print("Price:13.40")
        else:
            print("Error")


Paul = Lunch("Menu 1")
Paul.menu_price()
John = Lunch("Menu 2")
John.menu_price()"""

# Exercise 4
# Define a Point3D class that inherits from object Inside the Point3D class,
# define an __init__() function that accepts self, x, y, and z, and assigns these
# numbers to the member variables self.x,self.y,self.z. Define a __repr__() method
# that returns "(%d, %d, %d)" % (self.x, self.y, self.z). This tells Python to
# represent this object in the following format: (x, y, z). Outside the class
# definition, create a variable named my_point containing a new instance of Point3D
#  with x=1, y=2, and z=3. Finally, print my_point.


"""
class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return "(%d,%d,%d)" % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print(my_point)"""

# datetime
"""from datetime import date, datetime
dt = datetime(2012, 2, 23)
dt = datetime.now()
dt = datetime.strptime("2022/2/12", "%Y/%m/%d")
print(dt, type(dt))
dt = datetime.now().strftime("%dth %B %Y")"""


# Opening Browser

print("Deployment Completed")
webbrowser.open("http://google.com")
