import unittest
import plotnine as p9
from plotnine.data import mtcars
from p9hsci import theme_hsci_continuous, theme_hsci_discrete
import matplotlib.figure

class TestP9HSCI(unittest.TestCase):
    def test_theme_hsci_discrete(self):
        with self.assertWarns(Warning):
            p = (p9.ggplot(mtcars, p9.aes(x='cyl', y='mpg', fill="name", color="name")) + 
            theme_hsci_discrete() + 
            p9.geom_point())
            self.assertIsInstance(p.draw(show=False), matplotlib.figure.Figure)

    def test_theme_hsci_continous(self):
        p = (p9.ggplot(mtcars, p9.aes(x='cyl', y='mpg', fill="disp", color="hp")) + 
        theme_hsci_continuous() + 
        p9.geom_point())
        self.assertIsInstance(p.draw(show=False), matplotlib.figure.Figure)
