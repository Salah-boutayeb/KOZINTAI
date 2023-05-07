import cohere
import os
import numpy as np
import math
import pickle

# import openai_secret_manager
import openai
import re
import json
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('cohere_key')
co = cohere.Client(key)
openai.api_key = os.getenv('openai_key')


def get_recipe_from_file():
    absolute_path = os.path.dirname(__file__)
    relative_path = "../../data/data.txt"
    full_path = os.path.join(absolute_path, relative_path)
    file = open(full_path, "r")

    texts = []
    for line in file:
        texts.append(line.split(":")[1])

    return texts


def calculate_similarity(ingredients):

    top_3_recipes = []
    response = co.embed(
        texts=[ingredients],
        model='small',
    )
    embedding_for_recipe_test = response.embeddings

    cosine_similarity_list = []
    absolute_path = os.path.dirname(__file__)
    relative_path = "../../data/embeddings.npy"
    full_path = os.path.join(absolute_path, relative_path)

    all_embeddings = np.load(full_path)
    for i in range(len(all_embeddings)):
        # Calculate the dot product of the two arrays
        dot_product = np.dot(embedding_for_recipe_test, all_embeddings[i])

        # Calculate the norm of the two arrays
        norm_embedding_for_recipe_test = np.linalg.norm(
            embedding_for_recipe_test)
        norm_embedding = np.linalg.norm(all_embeddings[i])

        # Calculate the cosine similarity
        cosine_similarity = dot_product / (norm_embedding_for_recipe_test *
                                           norm_embedding)

        cosine_similarity_list.append((i, cosine_similarity))

    # Sort the list by the variable in descending order
    cosine_similarity_list.sort(key=lambda x: x[1], reverse=True)

    # Select the top 3 by ID
    top_3 = [x for x in cosine_similarity_list[:3]]
    print("Top 3 IDs:", top_3)
    my_recipes_from_data = get_recipe_from_file()
    for recipe in top_3:
        top_3_recipes.append(my_recipes_from_data[recipe[0]])
    return top_3_recipes


def generate_recipe_suggestions(ingredients, diet):
    if diet is not None:
        prompt = f"Generate a traditional Moroccan recipe using: {ingredients}. Be careful, The person has {diet}. For the response It should be a json object that contains, Name of the recipe, Ingredients, Instructions, Calories and the last one the date of today."
    else:
        prompt = f"Generate a traditional Moroccan recipe using: {ingredients}. For the response It should be a json object that contains, Name of the recipe, Ingredients, Instructions, Calories and the last one the date of today."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    recipe = json.loads(json.dumps(response))["choices"][0]["text"]
    return recipe
