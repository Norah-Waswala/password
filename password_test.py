from user import User
from credentials import credentials
import unittest
import pyperclip
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
        self.assertEqual(self.new_user.password,"@3773jsg")
    
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

    def test_delete_user(self):
        '''
         test_delete_credentials to test if we can remove a credentials from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials =credentials("instagram","insta-norah","$!dg68r6hd") # new credentials object
        self.new_credentials.delete_credentials()# Deleting a credentials object
        self.assertEqual(len(credentials.credentials_list),0)
       
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
        self.assertEqual(self.new_credentials.password,"@#he37336")
    
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
    
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials =credentials("instagram","insta-norah","$!dg68r6hd") # new credentials object
        test_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),2)


    def test_delete_credentials(self):
        '''
         test_delete_credentials to test if we can remove a credentials from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials =credentials("instagram","insta-norah","$!dg68r6hd") # new credentials object
        self.new_credentials.delete_credentials()# Deleting a credentials object
        self.assertEqual(len(credentials.credentials_list),0)

    def test_find_credentials_by_account_name(self):
        '''
         test to check if we can find a credential entry by account username and display the details of the credential
        '''
        self.new_credentials.save_credentials()
        test_credentials=credentials("instagram","insta-norah","$!dg68r6hd") # new credential
        test_credentials.save_credentials()
        # test_credentials = Credentials("Test","test@user.com") # new contact
        found_credentials = credentials.find_by_account_name("instagram")
        self.assertEqual(found_credentials.account,test_credentials.account)

    def test_credentials_exists(self):
        '''
        test to check if we can return a true or false based on whether we find or can't find the credential.
        '''
        self.new_credentials.save_credentials()
        test_credentials =credentials("instagram","insta-norah","$!dg68r6hd") # new contact
        test_credentials.save_credentials()
        credentials_exists = credentials.credentials_exist("instagram")
        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
         test method to test if we can display all credentials from our credentials_list
        '''
        self.assertEqual(credentials.display_credentials(),credentials.credentials_list) 

    # def test_copy_passcode(self):
    #     '''
    #     Test to confirm that we are copying the passward code from a found credential
    #     '''

    #     self.new_credentials.save_credentials()
    #     credentials.copy_passcode("insta-norah")

    #     self.assertEqual(self.new_credentials.passcode,pyperclip.paste())

       
    
   


if __name__ == '__main__':
    unittest.main()