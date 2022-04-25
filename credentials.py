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