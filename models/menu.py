# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Alle Rezepte'), False, URL('default', 'recipeList'), []),
    (T('Eigene Rezepte verwalten'), False, URL('default', 'manageRecipes'), []),
    (T('Neues Rezept'), False, URL('default', 'newRecipe'), []),
]