import bcrypt

salt = bcrypt.gensalt()

def generate_hash(passwd, salt=salt):
    return str(bcrypt.hashpw(passwd, salt))


def match_password(req_pwd, db_pwd):
    db_pwd = db_pwd.replace('b\'','').replace('\'','').encode('utf-8')
    return db_pwd == bcrypt.hashpw(req_pwd, db_pwd)
