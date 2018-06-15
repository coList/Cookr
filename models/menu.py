# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Eigene Rezepte verwalten'), False, URL('default', 'manageRecipes'), []),
    (T('Neues Rezept'), False, URL('default', 'newRecipe'), []),
    (T('Rezepte von A bis Z'), False, URL('default', 'recipeList', args = (0)), [])
]

#Menu-Item: "Rezepte nach Kategorien": Add all items from db.category
categories = []
for row in db(db.category).select():
    categories.append((T(row.name), False, URL('default', 'categoryRecipeList', args = (row.id, 0)), []))

response.menu.append((T('Rezepte nach Kategorien'), False, None, categories))

#Menu-Item: "Rezepte nach Herkunftsland": Add all items from db.origin
origins = []
for row in db(db.origin).select():
    origins.append((T(row.name), False, URL('default', 'originRecipeList', args = (row.id, 0)), []))
    
response.menu.append((T('Rezepte nach Herkunftsland'), False, None, origins))
