# import pyperclip
class User:
    """
    Class that generates new instances of user.
    """
    user_list=[]

    def __init__(self,username,passcode):   
        """
        method that defines the properties of a user.
        """    
        self.username=username
        self.passcode=passcode
      
    # def save_user(self):
    #     '''
    #     a method that saves the new instance of user
    #     '''
    #     User.user_list.append(self)

    # def delete_user(self): 
    #     '''
    #     a method that deletes a user's account
    #     '''
    #     User.user_list.remove(self)

    # @classmethod
    # def display_user(cls):
    #     '''
    #     method that returns the user list
    #     '''
    #     return cls.user_list