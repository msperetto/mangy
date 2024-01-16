# to run the server, go to python folder and execute:
# uvicorn app:app --reload
# where the first app is the python file name and the second is the FastAPI object name.
# the option --reload is to reload the server for every time the project is saved.

from typing import Optional

from sqlmodel import Field, SQLModel, create_engine
from fastapi import FastAPI
from pydantic import BaseModel

class Ingredient(BaseModel):
    name: str
    quantity: int
    description: str | None = None
    measure_type: str #ml, gr, lt
    nutrition_facts: dict[str, str]

class Recipe(BaseModel):
    name: str
    description: str | None = None
    ingredients: dict[Ingredient, int] # ingredient, quantity
    servings: int
    preparation_time: int #in minutes
    cooking_time: int | None = None #in minutes
    initial_instructions: str | None = None
    directions: str # could be a sequence of steps? Can any step be repeatable in other recipes? use some Artificial inteligence here?
    #future additions:
        # nutritio_label ?
        # valuation / rating
        # reviews   

class Menu(BaseModel):
    menu_id: int
    frequency: int #days amount
    recipes: dict[Recipe, tuple[int, int]] # the tuple represents the day and the meal number of that day

class Shopping_list(BaseModel):
    shopping_list_id: int
    ingredients: dict[Ingredient, int] #ingredient, quantity

app = FastAPI()

@app.get("/")
async def root():
    return { 
        "message": "I'm root"
    }

@app.get("/ingredients/{ingredient_id}")
async def get_ingredient(ingredient_id: int):
    return {"ingredient_id": ingredient_id}

@app.post("/ingredients/")
async def new_ingredient(ingredient: Ingredient):
    return ingredient

@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    return {"recipe_id": recipe_id}

@app.post("/recipes/")
async def new_recipe(recipe: Recipe):
    return recipe

@app.get("/menus/{menu_id}")
async def get_menu(menu_id: int):
    return {"menu_id": menu_id}

@app.post("/menus/")
async def new_menu(menu: Menu):
    return menu

@app.get("/shopping_lists/{shopping_list_id}")
async def get_shopping_list(shopping_list_id: int):
    return {"shopping_list_id": shopping_list_id}

@app.post("/shopping_lists/")
async def new_shopping_list(shopping_list: Shopping_list):
    return shopping_list
