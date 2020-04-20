import sys
import unittest
from tkinter import Tk, Canvas, Button, PhotoImage, Label, Scale
class StatisticalAnalisys(object):

    def __init__(self):
        
        """It calculates data for the line of regression"""
        
        self._values = {}
        self._x = 0
        self._y = 0
        self._l=[]
        # self._xy=[]

    def getData(self, data):
        
        """Opens a file and reads the data inside of it
        pre: data is a string
        post:---"""

        d = open(data, "r")
        
        for line in d:
            for content in line.split():
                # print(content)
                if content.isdigit() == True:
                    self._l.append(float(content))
        d.close()
        
        self._x = self._l[:len(self._l)//2]
        self._y = self._l[len(self._l)//2:]
        self._size = len(self._l) // 2
        # self.xy=[self.x.self.y]

    def getDataForSlope(self, data):
        """Will get x values for the x in the slope equation
        pre: data string type
        post: None"""

        d = open(data, "r")
        self._values["x"] = []

        for line in d:
            # print(line.split())
            for content in line.split():
                # print(content)
                if content.isdigit() == True:
                    # print(content)
                    self._values["x"].append(float(content))
                
        d.close()
    # def setY(self):
    #     self._values["y"] = [] 
    #     for x in self._values["x"]:
    #         self._values = self._values["x"][x]

    def getSummations(self):

        """Claculates the sigmas of x and y in the form of
        Ex, Ey, Ex^2, Ey^2, Ex*y
        pre: None
        post: Calculatinf and storing data into self._variable"""
        
        sumX = 0
        sumY = 0
        sumXSquared = 0
        sumYSquared = 0
        sumXY = 0
        
        for i in range(self._size):
            sumX += self._x[i]
            sumY += self._y[i]
            sumXSquared += self._x[i]**2
            sumYSquared += self._y[i]**2
            sumXY += (self._x[i] * self._y[i])
        
        # Creating keys and asigning value to them.
        self._values["sumX"] = sumX
        self._values["sumY"] = sumY
        self._values["sumX^2"] = sumXSquared
        self._values["sumY^2"] = sumYSquared
        self._values["sumX*Y"] = sumXY
        # print("testing self._value",self._values)

    def _setConatantsForTheSpole(self):
        
        """Compute constant numbers a and b for the slope
        as for the formula y = a + b*x
        pre: None
        post: return the constant numbers"""

        numerator = (self._size * self._values["sumX*Y"] - (self._values["sumX"]*self._values["sumY"]))
        denominator = (self._size * self._values["sumX^2"] - self._values["sumX"]**2)
        b = numerator / denominator

        aveX = float(self._values["sumX"] / self._size)
        aveY = float(self._values["sumY"] / self._size)
        a = float(aveY - (b*aveX))

        return a, b
    
    def getTheSplope(self):
        
        """Computers slope list of x
        pre: x = {R}
        post: Returns the slope."""
        
        a, b = self._setConatantsForTheSpole()
        self._values["y"] = []
        y = 0
        for x in self._values["x"]:
            y = a + (b * x)
            self._values["y"].append(y)
    
    def seeValuesOfKeysXandYOfDictionary(self):
        print("list of x values: ",self._values["x"])
        print("list of y values: ",self._values["y"])
        return self._values["x"], self._values["y"]
    # def getX(self, data):
    #     """"""
    #     d = open(data, "r")
    #     y = []
    #     x = []
    #     slope = 0
    #     for line in data:
    #         for char in line.split():
    #             if char.isdigit() == True:
    #                 i = int(char)
    #                 x.append(i)
    #                 slope = self.getTheSplope(i)  
    #                 y.append(slope)
    #     d.close()
    #     print(x,y)
    #     return x, y

    # def getPoints(self):
    #     """"""
    #     for i in 
    def mySwitch(self, case):

        # print(self._values)
        if case == 0:
            return self._values["sumX"]
        elif case == 1:
            return self._values["sumY"]
        elif case == 2:
            return self._values["sumX^2"]
        elif case == 3:
            return self._values["sumY^2"]
        elif case == 4:
            return self._values["sumX*Y"]
        else:
            return self._setConatantsForTheSpole()

class MakeCartesianGraph(object):

    def __init__(self, root):
        self._width = 1600
        self._height = 900
        self._frameThinkness = float(10/self._width) * self._width
        self._root = root
        self._window = Canvas(self._root,
        width = self._width,
        height = self._height,
        borderwidth = self._frameThinkness,
        highlightthickness  = self._frameThinkness,
        highlightbackground = "black",
        bg = "white")#"spring green"

        self._root.wm_title("Statistical Analisys: The Regression Line")

        # self.makeCartesianCoordinateSystem()
        
        # This works only if the size of 
        # the window is bigger than the resizong.
        # for a 1600x900 500x281 is a perfect match.
        # self._root.geometry("1000x563")
        
    def makeCartesianCoordinateSystem(self):

        """Placing the cartesian coodinate system"""

        # Creating the two axes
        # verticalLine

        verticaLine = self._window.create_line(self._width/2, 0,
                                self._width/2, self._height+50,
                                fill = "sky blue",
                                width = "2")
        # verticaLine.scale()
        # horrizontalLine
        horrizonatLine = self._window.create_line(40, self._height/2,
                                self._width, self._height/2,
                                fill = "sky blue",
                                width = "2")
        # self._window.pack() 
        # horrizonatLine.scale(100, 563)
        # self._root.geometry("1000x563")

        # Creating the littlelines here
        # however, make so that you caould \
        # just the local variable horrizontalLine
        # instead of making new object just use 
        # onr that you alrady have and rescale i.
        l=[10,20,30,40,50,60,70,80,90,100]
        # verticalLabel=None
        
        # horrizonla lines
        horrizontalX1 = 0
        horrizontalX2 = 0
        horrizontalY1 = 0
        horrizontalY2 = 0

        # vertical lines

        verticalX1 = 0
        verticalX2 = 0
        verticalY1 = 0
        verticalY2 = 0

        # line formats
        lineWidths = ("1", "2")
        lineColors = ("sky blue", "deep sky blue")

        for i in range(100):

            # Smaller lines

            # Horrizontal lines
            horrizontalX2 = horrizontalX1 = (self._width/100)*i
            horrizontalY1 = (self._height/2)-10
            # horrizontalX2 = (self._width / 10) * (i / 10)
            horrizontalY2 = self._height/2+10

            # Vertical lines
            verticalX1 = (self._width/2)-10
            verticalX2 = (self._width/2)+10
            verticalY2 = verticalY1 = (self._height/100)*i
            # verticalY2 = (self._height/100)*i

            lw = lineWidths[0]
            lc = lineColors[0]

            if i in l:

                # Bigger lines

                # Horrizontal lines
                horrizontalX2 = horrizontalX1 = (self._width / 10)*  (i / 10)
                horrizontalY1 = (self._height / 2) - 20
                # horrizontalX2 = (self._width / 10) * (i / 10)
                horrizontalY2 = self._height/2 + 20
                
                # Vertical lines
                verticalX1 = (self._width/2)-20
                verticalY2 = verticalY1 = (self._height/100)*i
                verticalX2 = (self._width/2)+20
                # verticalY2 = (self._height/100)*i

                lw = lineWidths[1]
                lc = lineColors[1]

                labelX = Label(self._window)
                labelY = Label(self._window)
                labelX["text"] = horrizontalX1 - self._width/2  
                labelX.place(x=horrizontalX1-20, y=horrizontalY2 )
                labelY["text"] = (self._height/2) - verticalY2
                labelY.place(x=verticalX2,y=verticalY2)

            # Horrizontal lines
            self._window.create_line(horrizontalX1, horrizontalY1,
                                horrizontalX2, horrizontalY2,
                                fill = lc,
                                width = lw)

            # Vertical lines
            self._window.create_line(verticalX1, verticalY1,
                            verticalX2, verticalY2,
                            fill = lc,
                            width = lw)


            self._window.pack()
        
    def setPerson(self):
        
        # person={}
        p = PhotoImage(file = "me.png")
        # # p.append(photo)
        # person["person"] = [Label(self._window, image = photo[0])]
        # label.image = photo
        # person["person"]
        label = Label(self._window, image = p)
        label.image = p#PhotoImage(file = "/home/emmanuel/Desktop/FinalProject/me.png")
        # label.pack()
        # person["p"] = label["image"]
        label2 = Label(self._window)
        label2["text"] = "Brought to you by TheWizard91:)"
        label2["foreground"] = "red"
        
        self._window.create_window((self._width/100)+100,
                                self._height-200,
                                anchor=None, 
                                window=label)


        self._window.create_window((self._width/100)+120,
                                self._height-130,
                                anchor=None, 
                                window=label2)

        # self._window.pack()
        # print("PERSON IS: ",person)
    def plotPoints(self, x, y):

        """Will plot the points in the graph
        pre: x and y are arrays of floats
        post: Displays them."""

        for i in range(len(x)):
            self._window.create_oval(x[i]+(self._width/2),
            (self._height/2)-y[i],
            x[i]+(self._width/2),
            (self._height/2)-y[i], 
            fill="blue",width="1",
            outline="red")
            # self._window.pack()


class TestStatisticalAnalisys(unittest.TestCase):
    
    def testOne(self):

        L = [92,617,2338,82389,13642,(33.83,4.51)]
        s = StatisticalAnalisys()
        s.getData("data.txt")
        s.getSummations()
        s._setConatantsForTheSpole()
        # s.getTheSplope()
        for i in range(len(L)):
            # print(L[i])
            self.assertEqual(s.mySwitch(i), L[i])

def main(argv):
    unittest.main()

if __name__ == "__main__":
    # main(sys.argv)
    # s = StatisticalAnalisys()
    # s.get_data("data.txt")
    s = StatisticalAnalisys()
    s.getData("data.txt")
    s.getSummations()
    s.getSummations()
    s.getDataForSlope("x.txt")
    s.getTheSplope()
    x,y=s.seeValuesOfKeysXandYOfDictionary()
    root = Tk()
    d = MakeCartesianGraph(root)
    d.makeCartesianCoordinateSystem()
    d.plotPoints(x,y)
    d.setPerson()
    root.mainloop()

    # d.setPerson()