import nltk

sentence = "Desserts can be a delightful way to conclude a meal or satisfy your craving for something sweet. With so many options available, some of the most popular dessert choices include cake, ice cream, chocolate, pudding, and cheesecake. Cake, which is available in numerous flavors from rich chocolate to airy and light, is a classic dessert choice. Ice cream is a refreshing treat that can be savored alone or combined with other desserts such as pie or cake. Pudding, which is smooth and comforting, is available in several flavors, including chocolate. Cheesecake, which is rich and decadent, can be enhanced with the addition of fruit or chocolate. With an abundance of dessert options, there is always something to please every sweet tooth."

tokenizer = nltk.tokenize.MWETokenizer([("ice", "cream")])

tokens = tokenizer.tokenize(nltk.word_tokenize(sentence.lower()))

print(tokens)

def food_dfa(input_string):
    current_state = 0
    accepting_states = {4}  # The set of accepting states
    transitions = {
        0: {'c': 1, 'i': 5},
        1: {'a': 2},
        2: {'k': 3},
        3: {'e': 4},
        4: {},  #accepting state
        5: {'c': 6},
        6: {'e': 7},
        7: {'_': 8},
        8: {'c': 9},
        9: {'r': 10},
        10: {'e': 11},
        11: {'a': 12},
        12: {'m': 4}

        
    }  # The dictionary of transitions
    
    for char in input_string:
        if char not in transitions[current_state]:
            return False
        current_state = transitions[current_state][char]
    
    if current_state in accepting_states:
        return True
    else:
        return False


detected_food_names = set()

# Iterate over all substrings of input_text and check if they are food names
for word in tokens:
    if food_dfa(word):
        print('hi:' , word)
        detected_food_names.add(word)

# Display the detected food names
if len(detected_food_names) == 0:
    print("No food names detected.")
else:
    print("Detected food names:")
    for food_name in detected_food_names:
        print(food_name)
