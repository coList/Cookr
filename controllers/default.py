# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
from pydal.helpers.methods import smart_query


# TODO: 
# Wochenplan bearbeiten ermöglichen
# Rezepte zu Wochenplan hinzufügen
# Rezepte im Wochenplan anzeigen (Bild + Link zu Rezept)
# Rezepte: Schritte als einzelne Steps anlegen
# Styling 
# Haushalte statt einzelnen Nutzern
# Rezepte aus Wochenplan löschen, wenn Tag vorbei
# Meine Rezepte schöne Anzeige
# Profilbereich und meinCookr an eine Stelle
# Passwort vergessen nach Login weg
# Login, etc: Sprache Deutsch
# Schönes/ Sinnvolles Home


    
# http://hostname/Cookr/default/index
def index():
    return locals()

#http://hostname/Cookr/default/addToWeekplan/<recipe_id>
#add a recipe to your weekplan: choose at which day you want to cook it
@auth.requires_login()
@auth.requires_login()
def addToWeekplan():
    id = request.args(0, cast=int)
    
    if (request.vars.weekday):
        day = request.vars.weekday
        #db(db.weekplan.household == auth.user.id).update(day = id)
        
        #no weekplan stored yet, insert new weekplan in database
        if (db(db.weekplan.household == auth.user.id).isempty()):
            db.weekplan.insert()
            
            
        #store recipe in selected day
        
        if (day == 'monday'):
            db(db.weekplan.household == auth.user.id).update(monday = id)
        elif (day == 'tuesday'):
            db(db.weekplan.household == auth.user.id).update(tuesday = id)
        elif (day == 'wednesday'):
            db(db.weekplan.household == auth.user.id).update(wednesday = id)
        elif (day == 'thursday'):
            db(db.weekplan.household == auth.user.id).update(thursday = id)
        elif (day == 'friday'):
            db(db.weekplan.household == auth.user.id).update(friday = id)
        elif (day == 'saturday'):
            db(db.weekplan.household == auth.user.id).update(saturday = id)
        elif (day == 'sunday'):
            db(db.weekplan.household == auth.user.id).update(sunday = id)


        #if recipe was to add: redirect to showWeekplan
        redirect(URL('showWeekplan'))

    recipe = db.recipe(id)

    usersWeekplan = db(db.weekplan.household == auth.user.id).select()


    if usersWeekplan:
        monday = usersWeekplan[0].monday
        tuesday = usersWeekplan[0].tuesday
        wednesday = usersWeekplan[0].wednesday
        thursday = usersWeekplan[0].thursday
        friday = usersWeekplan[0].friday
        saturday = usersWeekplan[0].saturday
        sunday = usersWeekplan[0].sunday

    form=SQLFORM(db.weekplan).process()


    return locals()


# http://hostname/Cookr/default/showWeekplan
# shows your weekplan: which recipes to cook on what day of the week
@auth.requires_login()
def showWeekplan():
    usersWeekplan = db(db.weekplan.household == auth.user.id).select()
   
    if usersWeekplan:
        monday = usersWeekplan[0].monday
        tuesday = usersWeekplan[0].tuesday
        wednesday = usersWeekplan[0].wednesday
        thursday = usersWeekplan[0].thursday
        friday = usersWeekplan[0].friday
        saturday = usersWeekplan[0].saturday
        sunday = usersWeekplan[0].sunday

    return locals()

# http://hostname/Cookr/default/newRecipe
@auth.requires_login()
def newRecipe():
    newRecipeForm = SQLFORM(db.recipe).process()

    addIngredientForm = SQLFORM(db.recipeContainsIngredient).process()

    currentIngredients = db(db.ingredient).select()

    newRecipeForm.element(_type='submit')['_class']='mainButton'
    #redirect to http://hostname/default/showRecipe/<recipe.id>
    if newRecipeForm.accepted: redirect(URL('showRecipe', args=(newRecipeForm.vars.id)))
    return locals()

# http://hostname/Cookr/default/recipeList/<page>
def recipeList():
    RECIPES_PER_PAGE = 5

    page = request.args(0, cast=int)

    startValue = page * RECIPES_PER_PAGE
    endValue = page * RECIPES_PER_PAGE + RECIPES_PER_PAGE

    recipes = db(db.recipe).select(orderby=db.recipe.title, limitby=(startValue, endValue))


    #ingredients = db(db.ingredient).select()
    return locals()





# http://hostname/Cookr/default/search
def search():
    #list_of_searchable_fields = [db.category.name, db.origin.name, db.recipe.title]
    #query = smart_query(list_of_searchable_fields, search_text)
    #rows = db(query).select()

    rows = []
    searchKeyword = request.vars["search"]
    if searchKeyword != None and searchKeyword != "":
        list_of_searchable_fields = [db.recipe.title, db.category.name]
        query = smart_query(list_of_searchable_fields, searchKeyword).select()
        rows = db(query).select()
    return locals()

# http://hostname/Cookr/default/categoryRecipeList/<categoryId>/<page>
def categoryRecipeList():
    RECIPES_PER_PAGE = 5
    
    categoryId = request.args(0) 
    page = request.args(1, cast = int)
    
    startValue = page * RECIPES_PER_PAGE
    endValue = page * RECIPES_PER_PAGE + RECIPES_PER_PAGE
    
    recipes = db(db.recipe.category == categoryId).select(orderby = db.recipe.title, limitby = (startValue, endValue))
    
    category = db(db.category.id == categoryId).select()
    categoryName = category[0].name
    return locals()


# http://hostname/Cookr/default/originRecipeList/<originId>/<page>
def originRecipeList():
    RECIPES_PER_PAGE = 5
    
    originId = request.args(0)
    page = request.args(1, cast = int)
    
    startValue = page * RECIPES_PER_PAGE
    endValue = page * RECIPES_PER_PAGE + RECIPES_PER_PAGE
    
    recipes = db(db.recipe.origin == originId).select(orderby = db.recipe.title, limitby = (startValue, endValue))
    
    origin = db(db.origin.id == originId).select()
    originName = origin[0].name
    return locals()

# http://hostname/Cookr/default/showIngredient/<ingredient.id>
def showIngredient():
    ingredient = db.ingredient(request.args(0, cast=int))
    return locals()

# http://hostname/Cookr/default/showRecipe/<recipe.id>
def showRecipe():
    recipe = db.recipe(request.args(0, cast=int))
    items = db(db.recipeContainsItem.recipe == recipe.id).select()
    #ingredients = db(db.recipeContainsIngredient.recipe == recipe.id).select()
    #steps = db(db.recipe_step.recipe == recipe.id).select(orderby = db.recipe_step.stepNumber)
    return locals()



def randomRecipe():
    return 'Zeige zufälliges Rezept'

# http://hostname/Cookr/default/editRecipe/<recipe.id>
def editRecipe():
    id = request.args(0, cast=int)
    recipeForm = SQLFORM(db.recipe, id).process(next=URL('showRecipe', args=id))
    recipeForm.element(_type='submit')['_class']='mainButton'
    return locals()



# http://hostname/Cookr/default/manageRecipes
# shows all own recipes -> edit and delete them easily
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
