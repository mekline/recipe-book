#don't forget to source .venv/bin/activate!

import pandas as pd
import numpy as np
import re, os

outstring = ''
recipes = pd.read_csv('recipes_peter_leah.tsv', sep='\t')
print(recipes.head(5))

recipes = recipes.rename(index=str, columns={"Your name": "Name",\
    "Name of your recipe": "RecipeName",\
    "Description or story about your recipe": "Story",\
    "Thank you!": "Notes",\
    "What kind of recipe is this?":"Rtype"})

recipes["Rtype"] = pd.Categorical(recipes["Rtype"], ["Breakfast", "Appetizer", "Soup", "Salad", "Main Dish", "Side Dish", "Dessert", ""])

recipes['Ordering'] = np.where(recipes["Rtype"] == 'Breakfast', 1, recipes["Rtype"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Appetizer', 2, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Salad', 3, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Soup', 3, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Main Dish', 4, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Side Dish', 5, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Dessert', 6, recipes["Ordering"])

recipes = recipes.fillna("")

#New: Attempt some reformatting before concatenating text!!
recipes["Ingredients"] = recipes["Ingredients"].replace(to_replace=r'\*', value=r'\n*', regex=True)

recipes["FullText"] = '<h1 style="page-break-before: always">' + recipes["RecipeName"] + '</h1>' + \
"<p><i>" + recipes["Story"] + "</i></p>" + \
"<p>---"+ recipes["Name"] + "</p><br>" + \
"<h3>Ingredients</h3>" + \
"<p>"+ recipes["Ingredients"] + "</p><br>" + \
"<h3>Instructions</h3>" + \
"<p>"+ recipes["Instructions"] + "</p><br>" + \
"<p><i>" + recipes["Notes"] + "</i></p>"


recipes["FullText"] = recipes["FullText"].replace(to_replace=r'([0-9]+\))', value=r'</p><p>\1', regex=True)
recipes["FullText"] = recipes["FullText"].replace(to_replace=r'([0-9]+\.)', value=r'</p><p>\1', regex=True)
recipes["FullText"] = recipes["FullText"].replace(to_replace=r'\n\*', value=r'</p><p>*', regex=True)
recipes["FullText"] = recipes["FullText"].replace(to_replace=r'\n', value=r'</p><p>', regex=True)

recipes = recipes.sort_values("Ordering")

recipes["FullText"].to_csv('recipetext.html', index=False, header=False) 

with open('recipetext.html') as f:
	newText=f.read().replace('"\n"', '\n')

#More encoding nonsense
newText=newText.replace('\"<h1','<h1')
newText=newText.replace('</p>\"','</p>')
newText=newText.replace('\"\"','\"')

with open('recipetext.html', "w") as f:
  	f.write(newText)