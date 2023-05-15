import nltk
import string

def next_state(transitions, state, char):
    if state in transitions and char in transitions[state]:
        return transitions[state][char]
    elif state == -1:
        return -1
    else:
        return transitions[-1]['_']

def is_accept_state(accept_states, state):
    return state in accept_states

def build_dfa(foods):
    transitions = {}
    start_state = 0
    accept_states = set()
    next_state = 1

    for food in foods:
        state = start_state
        for char in food:
            if state not in transitions:
                transitions[state] = {}

            if char not in transitions[state]:
                transitions[state][char] = next_state
                state = next_state
                next_state += 1
            else:
                state = transitions[state][char]

        accept_states.add(state)
    transitions[-1] = {}
    transitions[-1]['_'] = -1
    return transitions, start_state, accept_states

def detect_food(input_string, dfa):
    current_state = dfa[1]
    input_string = input_string.lower()
    for char in input_string:
        current_state = next_state(dfa[0], current_state, char)
    
    if is_accept_state(dfa[2], current_state):
            print(dfa[2])
            return True
    return False

def transition(input_string, dfa):
    current_state = dfa[1]
    input_string = input_string.lower()
    states = {}
    for char in input_string:
        previous_state = current_state
        if previous_state != -1:
            current_state = next_state(dfa[0], current_state, char)
            if states.get(previous_state,'') == '':
                states[previous_state] = {}
                states[previous_state]["char"]= char
                states[previous_state]["next_state"]= current_state
            else:
                states[previous_state]["char"]= char
                states[previous_state]["next_state"]= current_state
        else:
            if states.get(previous_state,'') == '':
                states[previous_state] = []
                states[previous_state].append({'char':char,'next_state':previous_state})
            else:
                states[previous_state].append({'char':char,'next_state':previous_state})

    
    return states

def token(text):
    tokenizer = nltk.tokenize.MWETokenizer([("ice", "cream"),("Ice", "cream"),("crème", "brûlée"),("banana","boat"),("black","forest")], separator=' ')
    tokens = tokenizer.tokenize(nltk.word_tokenize(text))
    return tokens


def find_food(tokens, food_dfa):
    detected_food_names = {}
    accept = 0

    # Iterate over all substrings of input_text and check if they are food names
    for word in tokens:
        if detect_food(word.lower(), food_dfa):
            if word.lower() not in detected_food_names:
                detected_food_names[word.lower()] = 1
            else:
                detected_food_names[word.lower()] += 1
    
    # Display the detected food names
    if len(detected_food_names) == 0:
        print("No food names detected.")
    else:
        print("Detected food names:")
        for food_name, count in detected_food_names.items():
            print(f"{food_name}: {count}")
            accept += count

    return detected_food_names, accept

def position(tokens, detected_food_names, accept):
        
    filtered_token = list(filter(lambda x:x not in string.punctuation,tokens))

    total_word = len(filtered_token)

    position = {}
    for food in detected_food_names:
        position[food] = [(index+1) for index,word in enumerate(filtered_token) if food == word.lower()]
    print(position)

    reject = total_word-accept
    print('Accepted words: ' , accept)
    print('Rejected words: ' , reject)

    return position, accept, reject, filtered_token