# -*- coding: utf-8 -*-

import datetime
now = datetime.date.today()

db.auth_user.first_name.readable = db.auth_user.first_name.writable = False
db.auth_user.last_name.readable = db.auth_user.last_name.writable = False

db.define_table('category', 
                Field('name', requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'category.name')]),
                format = '%(name)s')

db.define_table('difficulty',
                Field('name', requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'difficulty.name')]),
                format = '%(name)s')

db.define_table('priceCategory', 
                Field('name', requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'priceCategory.name')]),
                format = '%(name)s')

db.define_table('origin', 
                Field('name', requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'origin.name')]),
                format = '%(name)s')

db.define_table('measurement', 
                Field('name', requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'measurement.name')]),
                format = '%(name)s')

db.define_table('ingredient',
                Field('name', requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'ingredient.name')]),
                Field('namePlural'),
                Field('description', 'text'))

db.define_table('item',
                Field('name', requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'item.name')]),
                Field('namePlural'),
                Field('description', 'text'))
                


db.define_table('recipe',
                Field('writer', 'reference auth_user'),
                Field('category', 'reference category', label = 'Kategorie'),
                Field('difficulty', 'reference difficulty', label = 'Schwierigkeit', orderby = 'difficulty.id'),
                Field('priceCategory', 'reference priceCategory', label = 'Kosten', orderby = db.priceCategory.id),
                Field('origin', 'reference origin', label = 'Herkunft'),
                Field('title', label = 'Titel', requires = [IS_NOT_EMPTY()]),
                Field('duration', 'integer', label = 'Dauer'),
                Field('forAmountOfPeople', 'integer', label = 'Für Anzahl an Personen'),
                Field('creationDate', 'date', default = now, writable = False, readable = False),
                Field('description', 'text', label = 'Beschreibung'))


db.define_table('recipe_step',
                Field('recipe', db.recipe, requires = [IS_NOT_EMPTY(), IS_IN_DB(db, 'recipe.id')]),
                Field('stepNumber', 'integer', requires = [IS_NOT_EMPTY()]),
                Field('instruction', 'text', requires = [IS_NOT_EMPTY()]))

db.define_table('recipeContainsIngredient',
                Field('recipe', db.recipe, requires = [IS_NOT_EMPTY(), IS_IN_DB(db, 'recipe.id', 'recipe.title')]),
                Field('ingredient', db.ingredient, requires = [IS_NOT_EMPTY(), IS_IN_DB(db, 'ingredient.id', 'ingredient.name')]),
                Field('measurement', db.measurement, requires = [IS_NOT_EMPTY(), IS_IN_DB(db, 'measurement.id', 'measurement.name')]),
                Field('amount', 'double', requires = [IS_NOT_EMPTY()]))

db.define_table('recipeContainsItem',
                Field('recipe', db.recipe, requires = [IS_NOT_EMPTY(), IS_IN_DB(db, 'recipe.id', 'recipe.title')]),
                Field('item', db.item, requires = [IS_NOT_EMPTY(), IS_IN_DB(db, 'item.id', 'item.name')]))
