#don't forget to source .venv/bin/activate!

import pandas as pd
import numpy as np
import re

outstring = ''
recipes = pd.read_csv('recipes_peter_leah.tsv', sep='\t')
print(recipes.head(5))

recipes = recipes.rename(index=str, columns={"Your name": "Name",\
    "Name of your recipe": "RecipeName",\
    "Description or story about your recipe": "Story",\
    "Thank you!": "Notes",\
    "What kind of recipe is this?":"Rtype"})

recipes['Ordering'] = np.where(recipes["Rtype"] == 'Breakfast', 1, recipes["Rtype"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Appetizer', 2, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Salad', 3, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Side Dish', 3, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Soup', 3, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Main Dish', 4, recipes["Ordering"])
recipes['Ordering'] = np.where(recipes["Rtype"] == 'Dessert', 5, recipes["Ordering"])

#recipes["Rtype"] = pd.Categorical(recipes["Rtype"], ["Breakfast", "Appetizer", "Soup", "Salad", "Main Dish", "Side Dish", "Dessert"])

recipes = recipes.fillna("")

#print recipes.head(5)
print(recipes["Ordering"])

recipes["FullText"] = '<h1>' + recipes["RecipeName"] + '</h1>' + \
"<p><i>" + recipes["Story"] + "</i></p>" + \
"<p>---"+ recipes["Name"] + "</p><br>" + \
"<h3>Ingredients</h3>" + \
"<p>"+ recipes["Ingredients"] + "</p><br>" + \
"<h3>Instructions</h3>" + \
"<p>"+ recipes["Instructions"] + "</p><br>" + \
"<p><i>" + recipes["Notes"] + "</i></p><p>*****</p>"

recipes["FullText"] = recipes["FullText"].replace(to_replace=r'([0-9]\))', value=r'</p><p>\1', regex=True)

recipes = recipes.sort("Ordering")

recipes["FullText"].to_csv('recipetext.html', index=False)

with open('recipetext.html') as f:
	newText=f.read().replace('"\n"', '\n')

with open('recipetext.html', "w") as f:
  	f.write(newText)