# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    return locals()

@auth.requires_login()
def newRecipe():
    newRecipeForm = SQLFORM(db.recipe).process()
    
    addIngredientForm = SQLFORM(db.recipeContainsIngredient).process()
    
    currentIngredients = db(db.ingredient).select()
    
    if newRecipeForm.accepted: redirect(URL('showRecipe'))
    return locals()

def recipeList():
    recipes = db(db.recipe).select()
    #ingredients = db(db.ingredient).select()
    return locals()

def showIngredient():
    ingredient = db.ingredient(request.args(0, cast=int))
    return locals()

def showRecipe():
    recipe = db.recipe(request.args(0, cast=int))
    items = db(db.recipeContainsItem.recipe == recipe.id).select()
    ingredients = db(db.recipeContainsIngredient.recipe == recipe.id).select()
    steps = db(db.recipe_step.recipe == recipe.id).select(orderby = db.recipe_step.stepNumber)
    return locals()

@auth.requires_login()
def manageRecipes():
    recipesGrid = SQLFORM.grid(db.recipe.writer == auth.user.id)
    return locals()

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
