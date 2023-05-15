import string
from flask import Flask, render_template, request,jsonify
import food_dfa
import json
app = Flask(__name__)
app.secret_key = "Hello"

def build_food_dfa(text):
    foods = ['cake', 'ice cream', 'chocolate', 'pudding', 'cheesecake', 'black forest','tiramisu','pie','banana boat', 'crème brûlée', 'macaron', 'pancake','tart', 'soufflé','charlotte','fruit','coffee']
    dfa = food_dfa.build_dfa(foods)
    tokens = food_dfa.token(text)
    detected_food_names, accept = food_dfa.find_food(tokens, dfa)
    position, accept, reject, filtered_token = food_dfa.position(tokens, detected_food_names, accept)
    return detected_food_names, position, accept, reject, tokens, filtered_token

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        if request.is_json:
            foods = ['cake', 'ice cream', 'chocolate', 'pudding', 'cheesecake', 'black forest','tiramisu','pie','banana boat', 'crème brûlée', 'macaron', 'pancake','tart', 'soufflé','charlotte','fruit','coffee']
            dfa = food_dfa.build_dfa(foods)
            word = request.args.get('word')
            states = food_dfa.transition(word, dfa)
            print(json.dumps(states))
            return jsonify(json.dumps({'accept':list(dfa[2]),'states':states}))
        
        food_names = {}
        position={}
        result=0
        return render_template('find_food.html', food_names = food_names, position = position, result=result )

    elif request.method == 'POST':
        text = request.form['text']
        detected_food_names, position, accept, reject, tokens, filtered_token = build_food_dfa(text)
        strings = [f"<strong>{word}</strong>" if word.lower() in detected_food_names.keys() else word for word in tokens]
        result = ''
        for index,word in enumerate(strings):
            if index == 0:
                result += word
            elif word in string.punctuation:
                result += word
            else:
                result += f" {word}"
        return render_template('find_food.html', token = filtered_token, food_names = detected_food_names, position = position, accept=accept, reject = reject, result=result )
app.run(debug=True)