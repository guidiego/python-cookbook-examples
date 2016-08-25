from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

def sort_users():
    return sorted(users, key=lambda u: u.user_id)

def sort_users_w_attrgetter():
    return sorted(users, key=attrgetter('user_id'))

def exec():
    print(sort_users())
    print(sort_users_w_attrgetter())

if __name__ == '__main__':
    exec()
