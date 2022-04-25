from user import User
from credentials import credentials
import unittest
# import pyperclip
#user tests
class Testuser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
         Set up method to run before each test cases.
        '''
        self.new_user = User("test-test2","@3773jsg")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
    
        self.assertEqual(self.new_user.username,"test-test2")
        self.assertEqual(self.new_user.passcode,"@3773jsg")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
       
        # credentials tests
class Testcredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    '''
    def setUp(self):
        '''
         Set up method to run before each test cases.
        '''
        self.new_credentials = credentials("twitter","twit-norah","@#he37336")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name,"twitter")
        self.assertEqual(self.new_credentials.account_username,"twit-norah")
        self.assertEqual(self.new_credentials.passcode,"@#he37336")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        credentials.credentials_list = []
        
    def test_save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),1)
    
#     def test_save_multiple_credentials(self):
#         '''
#         test_save_multiple_credentials to check if we can save multiple credentials
#             objects to our credentials_list
#         '''
#         self.new_credentials.save_credentials()
#         test_credentials =credentials("instagram","insta-norah","$!dg68r6hd") # new credentials object
#         test_credentials.save_credentials()
#         self.assertEqual(len(credentials.credentials_list),2)


#     def test_delete_credentials(self):
#         '''
#          test_delete_credentials to test if we can remove a credentials from our credentials list
#         '''
#         self.new_credentials.save_credentials()
#         test_credentials =credentials("instagram","insta-norah","$!dg68r6hd") # new credentials object
#         self.new_credentials.delete_credentials()# Deleting a credentials object
#         self.assertEqual(len(credentials.credentials_list),0)



if __name__ == '__main__':
    unittest.main()