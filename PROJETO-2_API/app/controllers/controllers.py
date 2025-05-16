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
        
    @staticmethod
    def delete_user(data):
        name = data['name']
        cursor.execute("DELETE FROM users WHERE name = %s",(name,))
        connection.commit()
    
    @staticmethod
    def update_user(data):
        id = data['id']
        if 'name' in data:
            cursor.execute("UPDATE users SET name = %s WHERE id = %s",(data['name'], id))
            connection.commit()
            
        if 'age' in data:
            cursor.execute("UPDATE users SET age = %s WHERE id = %s",(data['age'], id))
            connection.commit()
            
        if 'gender' in data:
            cursor.execute("UPDATE users SET gender = %s WHERE id = %s",(data['gender'], id))
            connection.commit()
            
            
    @staticmethod
    def list_user():
        cursor.execute("SELECT * from users")
        dados = cursor.fetchall()
        return dados