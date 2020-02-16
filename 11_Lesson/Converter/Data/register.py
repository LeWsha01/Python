from converter.db.models import User, session


def registration():
    """
    Method for registering new users
    """
    all_login = [instance.login for instance in session.query(User).all()]

    new_name = input('Enter your name: ')
    new_surname = input('Enter your surname: ')
    new_login = input('Enter your login: ')
    new_password = input('Enter your password: ')

    if new_login not in all_login:
        session.add(User(new_name, new_surname, new_login, new_password))
        session.commit()
    else:
        print('This username is being used by another user.')
