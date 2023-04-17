from flask_app.config.mysqlconnection import connectToMySQL

import re	

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = 'paintings'

from flask_app import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if len(result) > 0:
            return User(result[0])
        else:
            return False
    
    @staticmethod
    def validate_user(user:dict) -> bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,user)
        is_valid = True

        if len(user['first_name']) < 2:
            is_valid = False
            flash("first name must be at least 2 characters")

        if user['password'] != user['confirm-password']:
            is_valid = False
            flash("passwords do not match")

        if not EMAIL_REGEX.match(user['email']): 
            is_valid = False
            flash("Invalid email address!")

        if len(results) >= 1:
            is_valid = False
            flash("Email already taken")

        if len(user['password']) <8:
            is_valid = False
            flash('password must be at least 8 characters')
            
        return is_valid