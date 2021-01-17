import unittest
import Ifttt

class TestIfttt(unittest.TestCase):
    def testWhenTemIsLessThan70TurnOn(self):
        """
        Test that the temp turns on when too cold
        """
        curretTemp = 68
        result = Ifttt.checkTemperature(curretTemp)
        self.assertEqual(result, "fermenton")

    def testWhenTempIsGreaterThan70point8ThenTurnOff(self):
        """
        Test That the heat is turned off when warm enough
        """
        currentTemp = 71
        result = Ifttt.checkTemperature(currentTemp)
        self.assertEqual(result, "fermentoff")

    def testWhenTempIsJustRight(self):
        """
        Test That the nothing happens when temp is OK
        """
        currentTemp = 70
        result = Ifttt.checkTemperature(currentTemp)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()