from user import user
import unittest
# import pyperclip

class TestPassward(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    # def setUp(self):
    #     self.new_passward = Passward("norah","waswala","test-test2","norah@gmail.com","@34hgxvgs")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
    
        self.assertEqual(self.new_passward.username,"test-test2")
        self.assertEqual(self.new_passward.passcode,"@34hgxvgs")
    
#     def tearDown(self):
        
#         Passward.passward_list = []