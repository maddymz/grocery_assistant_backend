from flask import Blueprint, request, jsonify
import os
from src.service.firebaseService import gptServiceDb
import os
import openai
import json
from src.service.searchService import get_item_id_by_search

gpt_routes = Blueprint('gpt_routes', __name__, url_prefix='/gpt')


@gpt_routes.route('/makeDish', methods=['POST'])
def make_dish():
    try:
        inputs = request.json['inputs']
        dishName = inputs[0]
        prompt_dish= "make-dish->"+dishName+" ->"
        # Make Magic Happen
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = "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"
        print(prompt_dish)
        response = openai.Completion.create(
            model="davinci:ft-personal:groceryasst-v9-2023-06-14-00-11-13",
            prompt=prompt_dish,
            temperature=0.2,
            max_tokens=1019,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["##EOF##"]
        )
        
        gpt_final_response = json.loads(response['choices'][0]['text'])
        print("Response from gpt ->",gpt_final_response)
        ingredients = gpt_final_response['ingredients']
        ingredients_mapping = {ingredient: get_item_id_by_search(ingredient) for ingredient in ingredients}
        gpt_final_response['ingredientsMapping'] = ingredients_mapping
        return jsonify(gpt_final_response), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@gpt_routes.route('/bulkShop', methods=['POST'])
def bull_shop():
    try:
        inputs = request.json['inputs']
        prompt = inputs[0]
        prompt_response = ''', Give me response back ONLY in the below JSON format, fill up everything that is enclosed by <..> (angle brackets):
        {
            "dishName": "<NAME OF THE DISH>",
            "howTo": "<HOW TO MAKE THE DISH IN HTML/TEXT FORMAT YOU CAN SKIP NEW LINE CHARACTER>",
            "ingredients": [
                "<INGREDITENT1 NAME ONLY>",
                "<INGREDITENT2 NAME ONLY>",
                "<INGREDITENT3 NAME ONLY>".... and so on
            ],

            "requiredQuantity": "<INGREDIENT ALONG WITH THEIR QUANTITY IN HTML TABLE AS TEXT YOU CAN SKIP NEW LINE CHARACTER>"
        }'''
        # Make Magic Happen
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = "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"
        print(prompt)
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt + ". " + prompt_response,
            temperature=0.2,
            max_tokens=1019,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["##EOF##"]
        )

        gpt_final_response = json.loads(response['choices'][0]['text'])
        print("Response from gpt ->",gpt_final_response)
        ingredients = gpt_final_response['ingredients']
        ingredients_mapping = {ingredient: get_item_id_by_search(ingredient) for ingredient in ingredients}
        gpt_final_response['ingredientsMapping'] = ingredients_mapping
        return jsonify(gpt_final_response), 200
    except Exception as e:
        return f"An Error Occured: {e}"