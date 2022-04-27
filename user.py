# import pyperclip
class User:
    """
    Class that generates new instances of user.
    """
    user_list=[]

    def __init__(self,username,password):   
        """
        method that defines the properties of a user.
        """    
        self.username=username
        self.password=password
      
    def save_user(self):
        '''
        a method that saves the new instance of user
        '''
        User.user_list.append(self)

    def delete_user(self): 
        '''
        a method that deletes a user's account
        '''
        User.user_list.remove(self)

    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user


    @classmethod
    def display_user(cls): 
        '''
        method that returns the user list
        '''
        return cls.user_list
    