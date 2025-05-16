from ..db.db import connection, cursor


class user():
    @staticmethod
    def create_user(data):
        name = data['name']
        age = data['age']
        gender = data['gender']
        values = (name, age, gender)
        cursor.execute("INSERT INTO users (name, age, gender) VALUES (%s, %s, %s)", values)
        connection.commit()
    
    def delete_user(data):
        name = data['name']
        cursor.execute("DELETE FROM users WHERE name = %s",(name,))
        connection.commit()
    
    def update_user(data):
        id = data['id']
        if 'name' in data:
            cursor.execute("UPDATE users SET name = %s WHERE id = %s",(data['name'], id))
            connection.commit()