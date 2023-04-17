from flask_app import app, render_template, session, redirect, request
from flask_app.models.recipe import Recipe


@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html', recipes = Recipe.get_all())

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods = ['POST'])
def create_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id':id}
    return render_template('recipes_show.html', recipe = Recipe.get_one(data))

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id':id}
    return render_template('recipes_edit.html', recipe = Recipe.get_one(data))

@app.route('/update/recipe', methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{request.form['id']}")    
    print(request.form)
    Recipe.update(request.form)
    return redirect('/recipes')

@app.route('/delete/recipe/<int:id>')
def delete(id):
    data ={'id':id}
    Recipe.destroy(data)
    return redirect('/recipes')
