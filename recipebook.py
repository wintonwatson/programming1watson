# AI Disclaimer: This code was written with moderate AI assistance.
# Used AI for: code structure suggestions and algorithm guidance.
# I implemented the solutions and modified the AI suggestions to fit the requirements.

import json  # For saving and loading recipes
import random  # For random recipe feature
import os  # To check if file exists

RECIPE_FILE = "recipes.json"


def load_recipes():
    """
    Load recipes from a file when the program starts.
    If the file doesn't exist, start with an empty recipe book.
    """
    try:
        # Check if the file exists
        if os.path.exists(RECIPE_FILE):
            # Open and read the file
            with open(RECIPE_FILE, 'r') as file:
                recipes = json.load(file)
                print(f"✓ Loaded {len(recipes)} recipes from file.")
                return recipes
        else:
            print("Starting with a new recipe book!")
            return {}  # Empty dictionary
    except:      
        print("Could not load recipes. Starting fresh.")
        return {}


def save_recipes(recipes):
    """
    Save all recipes to a file so we don't lose them.
    """
    try:
        # Open file and write recipes to it
        with open(RECIPE_FILE, 'w') as file:
            json.dump(recipes, file, indent=2)
        print("\n✓ All recipes saved!")
    except:
        print("\n⚠ Error: Could not save recipes.")


def add_recipe(recipes):
    """
    Add a new recipe to the recipe book.
    Asks user for name, servings, ingredients, and instructions.
    """
    print("\n" + "=" * 50)
    print("ADD NEW RECIPE")
    print("=" * 50)
    
    # Step 1: Get recipe name
    name = input("\nEnter recipe name: ").strip()
    
    # Make sure they entered something
    if name == "":
        print("Recipe name can't be empty!")
        return
    
    # Check if recipe already exists
    if name in recipes:
        answer = input(f"'{name}' already exists. Replace it? (yes/no): ")
        if answer.lower() != "yes":
            print("Cancelled.")
            return
    
    # Step 2: Get number of servings
    servings = input("Number of servings: ").strip()
    if servings == "":
        servings = "1"  # Default to 1 if empty
    
    # Step 3: Get ingredients
    print("\nEnter ingredients (type 'done' when finished)")
    print("Format: 2 cups flour  OR  1 tsp salt")
    ingredients = []  # Empty list to store ingredients
    
    while True:
        ingredient = input("Ingredient: ").strip()
        
        # Stop when user types 'done'
        if ingredient.lower() == "done":
            break
        
        # Add ingredient to the list
        if ingredient != "":
            ingredients.append(ingredient)
    
    # Step 4: Get cooking instructions
    print("\nEnter instructions (type 'done' when finished)")
    instructions = []  # Empty list to store steps
    step_number = 1
    
    while True:
        step = input(f"Step {step_number}: ").strip()
        
        # Stop when user types 'done'
        if step.lower() == "done":
            break
        
        # Add step to the list
        if step != "":
            instructions.append(step)
            step_number = step_number + 1
    
    # Step 5: Save the recipe
    recipes[name] = {
        "servings": servings,
        "ingredients": ingredients,
        "instructions": instructions
    }
    
    print(f"\n✓ Recipe '{name}' added successfully!")


def list_all_recipes(recipes):
    """
    Show a numbered list of all recipe names.
    Let user choose one to view.
    """
    # Check if recipe book is empty
    if len(recipes) == 0:
        print("\nYour recipe book is empty!")
        print("Try adding a recipe first.")
        return
    
    print("\n" + "=" * 50)
    print("YOUR RECIPES")
    print("=" * 50)
    
    # Get all recipe names and sort them alphabetically
    recipe_names = sorted(recipes.keys())
    
    # Show each recipe with a number
    for i in range(len(recipe_names)):
        print(f"{i + 1}. {recipe_names[i]}")
    
    # Let user pick one to view
    print()
    choice = input("Enter number to view (or press Enter to go back): ")
    
    if choice != "":
        try:
            # Convert to number and subtract 1 (lists start at 0)
            number = int(choice) - 1
            
            # Make sure it's a valid number
            if number >= 0 and number < len(recipe_names):
                selected_recipe = recipe_names[number]
                view_recipe(recipes, selected_recipe)
            else:
                print("Invalid number!")
        except:
            print("Please enter a valid number!")


def view_recipe(recipes, recipe_name):
    """
    Display one recipe with all its details.
    """
    # Check if recipe exists
    if recipe_name not in recipes:
        print(f"\nRecipe '{recipe_name}' not found!")
        return
    
    # Get the recipe data
    recipe = recipes[recipe_name]
    
    # Display recipe in nice format
    print("\n" + "=" * 50)
    print(f"RECIPE: {recipe_name}")
    print("=" * 50)
    print(f"Servings: {recipe['servings']}")
    
    # Show ingredients
    print("\nIngredients:")
    for ingredient in recipe['ingredients']:
        print(f"  - {ingredient}")
    
    # Show instructions
    print("\nInstructions:")
    for i in range(len(recipe['instructions'])):
        step = recipe['instructions'][i]
        print(f"  {i + 1}. {step}")
    
    print("=" * 50)


def search_recipes(recipes):
    """
    Search for recipes by name or by ingredient.
    """
    # Check if recipe book is empty
    if len(recipes) == 0:
        print("\nYour recipe book is empty!")
        return
    
    print("\n" + "=" * 50)
    print("SEARCH RECIPES")
    print("=" * 50)
    
    # Ask how they want to search
    search_type = input("\nSearch by (n)ame or (i)ngredient? ").lower()
    
    if search_type not in ['n', 'i']:
        print("Invalid choice! Use 'n' or 'i'")
        return
    
    search_term = input("Enter search term: ").lower()
    
    if search_term == "":
        print("Search term can't be empty!")
        return
    
    # Find matching recipes
    results = []
    
    if search_type == 'n':
        # Search by recipe name
        for recipe_name in recipes:
            if search_term in recipe_name.lower():
                results.append(recipe_name)
    else:
        # Search by ingredient
        for recipe_name in recipes:
            recipe = recipes[recipe_name]
            # Look through all ingredients
            for ingredient in recipe['ingredients']:
                if search_term in ingredient.lower():
                    results.append(recipe_name)
                    break  # Stop checking this recipe's ingredients
    
    # Show results
    if len(results) == 0:
        print(f"\nNo recipes found with '{search_term}'")
        return
    
    print(f"\nFound {len(results)} recipe(s):")
    for i in range(len(results)):
        print(f"{i + 1}. {results[i]}")
    
    # Let user pick one to view
    print()
    choice = input("Enter number to view (or press Enter to go back): ")
    
    if choice != "":
        try:
            number = int(choice) - 1
            if number >= 0 and number < len(results):
                view_recipe(recipes, results[number])
            else:
                print("Invalid number!")
        except:
            print("Please enter a valid number!")


def get_random_recipe(recipes):
    """
    Pick and display a random recipe.
    """
    # Check if recipe book is empty
    if len(recipes) == 0:
        print("\nYour recipe book is empty!")
        return
    
    # Get all recipe names
    recipe_names = list(recipes.keys())
    
    # Pick one randomly
    random_name = random.choice(recipe_names)
    
    print("\n Random Recipe!")
    view_recipe(recipes, random_name)


def show_menu():
    """
    Display the main menu options.
    """
    print("\n" + "=" * 50)
    print("RECIPE BOOK MANAGER")
    print("=" * 50)
    print("1. Add a new recipe")
    print("2. List all recipes")
    print("3. View a recipe")
    print("4. Search for recipes")
    print("5. Get a random recipe")
    print("6. Save and exit")
    print("=" * 50)


# MAIN PROGRAM STARTS HERE
print("Welcome to Recipe Book Manager!")
print("=" * 50)

# Load existing recipes from file
recipes = load_recipes()

# Main loop - keeps running until user exits
while True:
    show_menu()
    choice = input("\nYour choice (1-6): ")
    
    if choice == '1':
        add_recipe(recipes)
    
    elif choice == '2':
        list_all_recipes(recipes)
    
    elif choice == '3':
        name = input("\nEnter recipe name: ")
        view_recipe(recipes, name)
    
    elif choice == '4':
        search_recipes(recipes)
    
    elif choice == '5':
        get_random_recipe(recipes)
    
    elif choice == '6':
        # Save and exit
        save_recipes(recipes)
        print("\nThanks for using Recipe Book Manager!")
        print("Goodbye! ")
        break  # Exit the loop
    
    else:
        print("\nInvalid choice! Please enter 1-6.")