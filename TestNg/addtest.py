import unittest

def addition(x,y,z=0):
    return x+y+z

class AddTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_addition(self):
        self.assertEqual(addition(10,11,12),33)
        self.assertNotEqual(addition(11,12),44)
        self.assertEqual((addition(10,10,10)),30)
    def tes_negative_value(self):

        self.assertEqual(addition(-9,25),16)
        self.assertNotEqual(addition(-9,25),17)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()


# def addition(x,y,z=0):
#     return x+y+z
# class AddTest(unittest.TestCase):
#
#     def setUp(self):   # initialization code for the testcase/testsuite can be added here
#         pass
#
#     def test_addtion(self):
#
#         self.assertEqual(addition(10,11,12), 33)
#         self.assertNotEqual(addition(11,12), 44)
#
#     def test_negative_values(self):
#
#         self.assertEqual(addition(-9,25), 16)
#
#         self.assertNotEqual(addition(-9,25), 17)
#
#     def tearDown(self):
#         pass
#
# if __name__=='__main__':
#
#     unittest.main()