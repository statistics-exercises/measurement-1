import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xvals(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        myy = np.loadtxt("data.dat")
        self.assertTrue( len(this_x)==200, "you have not plotted the correct number of data points" ) 
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i - this_x[i])<1e-7, "the x-coordinates of your points are not correct" )
            self.assertTrue( np.abs(myy[i] - this_y[i])<1e-7, "the y-coordinates of your points are not correct" )
            
