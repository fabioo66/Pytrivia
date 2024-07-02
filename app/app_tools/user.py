class User():
    """ define entity that represent user person in PyTrivia"""

    def __init__ (self, username, full_name, email, date_of_birth, gender):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.gender = gender