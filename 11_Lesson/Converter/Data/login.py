from converter.db.models import User, session


def log_in(login):
    """
    Login Method
    :param login:
    :return:
    """
    all_login = [instance.login for instance in session.query(User).all()]

    if login in all_login:
        password = input('Enter password: ')
        password_user = [instance.password for instance in session.query(User.password).filter_by(login=login)]
        if password in password_user:
            print('OK!')
            return True
    else:
        print('This login is not found.')
        return False
