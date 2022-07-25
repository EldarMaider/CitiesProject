from user import User


class RegUser(User):
    def __init__(self, name, password):
        super().__init__(name)
        self.password = password

    def write_comment(self):
        pass

