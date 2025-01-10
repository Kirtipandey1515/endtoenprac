#from endtoendtest import successText
from page_obj1.homeclass import TestHomeClass
from utilities.Baseclass1 import BaseClass1



class TestHome(BaseClass1):
    def test_Home(self):
        self.test_loggingDemo()
        log = self.test_loggingDemo()

        shopitems = TestHomeClass(self.driver)
        shopitems.Home()
        Register = TestHomeClass(self.driver)
        Register.register()
        log.info("getting register details")




