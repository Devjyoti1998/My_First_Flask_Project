from models.users import User

def authenticate(username,password):
    #user=username_dict.get(username,None)
    user=User.get_by_username(username)
    if user and user.password==password:
        return user

def identity(payload):
    user_id=payload['identity']
    return User.get_by_id(user_id)
