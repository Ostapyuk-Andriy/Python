from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash

DATABASE = 'djs'

class Track:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.dj_id = data['dj_id']
        self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']






    @classmethod
    def save(cls, data):
        query = "INSERT INTO tracks (name, genre, dj_id) VALUES (%(name)s, %(genre)s, %(dj_id)s);"
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
        query = "SELECT * FROM tracks JOIN djs ON djs.id = tracks.dj_id;"
        results = connectToMySQL(DATABASE).query_db( query )
        tracks = []
        for track in results:
            tracks.append(cls(track))
        return tracks
    
    @staticmethod
    def validate_track(track:dict) -> bool:
        is_valid = True
        if len(track['name'])<3:
            flash('Name must be three characters')
            is_valid = False

        if len(track['genre'])<3:
            flash('Genre must be three characters')
            is_valid = False

        return is_valid

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM tracks JOIN djs ON djs.id = tracks.dj_id WHERE tracks.id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db( query,data )
        return Track(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE tracks SET name=%(name)s, genre=%(genre)s WHERE tracks.id =%(id)s;"
        return connectToMySQL(DATABASE).query_db( query,data )

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM tracks WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)