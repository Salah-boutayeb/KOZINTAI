# Using flask to make an api
# import necessary libraries and functions


from flask import Flask, jsonify, request,json
from flask_cors import CORS, cross_origin
from utils.utils import *
# creating a Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = [ 'POST'])
def home():
    data = json.loads(request.data)
    ingredients=data['ingredients']
    diet=None
    recipe_suggestions = []
    top_3=calculate_similarity(ingredients)
    for recipe in top_3:
        generated_recipe = generate_recipe_suggestions(recipe, diet)
        print(generated_recipe)
        recipe_suggestions.append(json.loads(generated_recipe))
        
    print(recipe_suggestions)

    return jsonify({'data': recipe_suggestions})
  
  
# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/test', methods = ['GET'])
def disp():
  
    return jsonify({'data': 'hello world'})
  
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)