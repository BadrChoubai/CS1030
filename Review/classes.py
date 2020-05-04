import uuid


class User:
    # Class variables
    uuid = uuid.uuid4()

    # Class constructor
    def __init__(self, first_name, last_name, email):
        '''Instance variables'''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    # Instance method
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def from_string(cls, user_string):
        '''Given a user string: `FirstName, LastName, Email`.
        generate a new User
        '''
        first_name, last_name, email = [
            attr.strip() for attr in user_string.split(',')]
        return cls(first_name, last_name, email)
