import string
from flask import Flask, render_template, request
import food_dfa
app = Flask(__name__)
app.secret_key = "Hello"

def dfa(text):
    foods = ['cake', 'ice cream', 'chocolate', 'pudding', 'cheesecake']
    dfa = food_dfa.build_dfa(foods)
    tokens = food_dfa.token(text)
    detected_food_names, accept = food_dfa.find_food(tokens, dfa)
    position, accept, reject = food_dfa.position(tokens, detected_food_names, accept)
    return detected_food_names, position, accept, reject, tokens

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        detected_food_names, position, accept, reject, tokens= dfa(text)
        strings = [f"<strong>{word}</strong>" if word.lower() in detected_food_names.keys() else word for word in tokens]
        result = ''
        for index,word in enumerate(strings):
            if index == 0:
                result += word
            elif word in string.punctuation:
                result += word
            else:
                result += f" {word}"
        print(result)
        return render_template('find_food.html', food_names = detected_food_names, position = position, accept=accept, reject = reject, result=result )
    else:

        return render_template('find_food.html')
app.run(debug=True)