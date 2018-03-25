from passlib.hash import pbkdf2_sha256
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('[^@]+@[^@]+\.[^@]+')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha256.verify(password, hashed_password)
