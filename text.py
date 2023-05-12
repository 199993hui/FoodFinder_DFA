class DFA:
    def __init__(self, transitions, start_state, accept_states):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def next_state(self, state, char):
        return self.transitions.get((state, char), self.start_state)

    def is_accept_state(self, state):
        return state in self.accept_states

def build_dfa(foods):
    transitions = {}
    start_state = 0
    accept_states = set()
    next_state = 1

    for food in foods:
        state = start_state
        for char in food:
            next = transitions.get((state, char))
            if next is None:
                transitions[(state, char)] = next_state
                state = next_state
                next_state += 1
            else:
                state = next

        accept_states.add(state)

    return DFA(transitions, start_state, accept_states)

detected_food_names = set()

def find_food(text, dfa):
    state = dfa.start_state

    for char in text.lower():
        state = dfa.next_state(state, char)
        if dfa.is_accept_state(state):
            if state == 4:
                detected_food_names.add('cake')
            if state == 13:
                detected_food_names.add('ice cream')
            if state == 21:
                detected_food_names.add('chocolate')
            if state == 28:
                detected_food_names.add('pudding')
            if state == 36:
                detected_food_names.add('cheesecake')



foods = ['cake', 'ice cream', 'chocolate', 'pudding', 'cheesecake']

text = "Desserts can be a delightful way to conclude a meal or satisfy your craving for something sweet. With so many options available, some of the most popular dessert choices include cakes, ice creams, chocolate, pudding, and cheesecake. Cakes, which is available in numerous flavors from rich chocolate to airy and light, is a classic dessert choice. Ice creams is a refreshing treat that can be savored alone or combined with other desserts such as pie or cake. Pudding, which is smooth and comforting, is available in several flavors, including chocolate. Cheesecake, which is rich and decadent, can be enhanced with the addition of fruit or chocolate. With an abundance of dessert options, there is always something to please every sweet tooth."

food_dfa = build_dfa(foods)
result = find_food(text, food_dfa)

if len(detected_food_names) == 0:
    print("No food names detected.")
else:
    print("Detected food names:")
    for food_name in detected_food_names:
        print(food_name)