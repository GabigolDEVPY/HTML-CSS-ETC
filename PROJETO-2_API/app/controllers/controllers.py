from ..db.db import connection, cursor


class user():
    @staticmethod
    def create_user(data):
        connection = connection()
        cursor = cursor()
    
    