import pyperclip
import random
class credentials:
    """
    Class that generates new instances of credentials.
    """
    credentials_list=[]

    def __init__(self,account_name,account_username,passcode):   
        """
        method that defines the properties of a credentials.
        """ 
        self.account_name=account_name  
        self.account_username=account_username
        self.passcode=passcode
      
    def save_credentials(self):
        '''
        a method that saves the new instance of credentials
        '''
        credentials.credentials_list.append(self)

    def delete_credentials(self): 
        '''
        a method that deletes a credentials's account
        '''
        credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account_username(cls,string):
        for credentials in cls.credentials_list:
            if credentials.account_username == string:
                return credentials

                            
    @classmethod
    def credentials_exist(cls,string):
        """checks if a credential exists

        Args:
            string (string): account_name 
        """        
        for credentials in cls.credentials_list:
            if credentials.account_name == string:
                return True
        return False

    @classmethod
    def display_credentialss(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    # @classmethod
    # def copy_passcode(cls,string):
    #     credentials_found = credentials.find_by_account_username(string)
    #     pyperclip.copy(credentials_found.account_username)

       

chars="abcdefghijklmnopqrstuvwxyz123456789#@$*&!"

while 1:
    passward_len=int(input("what length would you want your passward to be:"))
    passward_count=int(input("how many passwards do you need:"))
    for x in range(0,passward_count):
        passward=""
        for x in range(0,passward_len):
            passward_char=random.choice(chars)
            passward     =passward+passward_char
        print("Here is your passward : ",passward)



        
