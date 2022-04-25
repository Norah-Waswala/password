from user import User
import unittest
# import pyperclip

class TestPassward(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
         Set up method to run before each test cases.
        '''
        self.new_user = User("test-test2","@34hgxvgs")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
    
        self.assertEqual(self.new_passward.username,"test-test2")
        self.assertEqual(self.new_passward.passcode,"@34hgxvgs")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []