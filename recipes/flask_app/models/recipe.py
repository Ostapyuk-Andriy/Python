from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash

DATABASE = 'recipes'

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']






    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM recipes;"
    #     results = connectToMySQL(DATABASE).query_db( query )
    #     recipes = []
    #     for recipe in results:
    #         recipes.append(cls(recipe))
    #     return recipes 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db( query )
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes 
    
    @staticmethod
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True
        if len(recipe['name'])<3:
            flash('Name must be three characters')
            is_valid = False

        if len(recipe['description'])<3:
            flash('Description must be three characters')
            is_valid = False

        if len(recipe['instructions'])<3:
            flash('Instructions must be three characters')
            is_valid = False

        if not 'under_30' in recipe:
            flash('must select option for under 30 min.')
            is_valid = False

        if recipe['date_made'] == '':
            flash('Please select a date')
            is_valid = False
            
        return is_valid

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db( query,data )
        return Recipe(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30=%(under_30)s, date_made=%(date_made)s WHERE recipes.id =%(id)s;"
        return connectToMySQL(DATABASE).query_db( query,data )

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)