# Food Name Detector using DFA Algorithm

🌐 **[Live Demo](https://foodfinder-dfa.onrender.com)**

A web application that detects food names in free-form text using a **Deterministic Finite Automaton (DFA)** — a concept from the Theory of Computation. Built as a full-stack project with a Python/Flask backend and a dynamic frontend that visualises DFA state transitions in real time.

## 💡 What is a DFA?

A Deterministic Finite Automaton (DFA) is a theoretical model of computation. It reads an input string character by character, moving between states according to a transition function. If it ends in an **accept state**, the input is recognised. If it ends in a **trap/dead state**, the input is rejected.

In this project, the DFA is built from a list of known food names. Each food name creates a unique path of states. When a word is checked:
- Every character moves the DFA to the next state
- If the final state is an **accept state** → the word is a food name ✅
- If not → the word is rejected ❌

## 🍕 Features

#### **Food Detection**
- Paste any free-form text and detect all food names instantly
- Supports 17 food names including multi-word expressions (e.g. `ice cream`, `black forest`, `crème brûlée`)
- Detected food names are **highlighted in bold** inline within the original text
- Shows each food name's **count** and **word position** in the text

#### **DFA Visualisation**
- Select any token from the dropdown after searching
- View the full **state transition table** for that word step by step
- Shows **Accepted** (green) or **Rejected** (red) status badge

#### **Word Statistics**
- Counts total **accepted** words (food names found)
- Counts total **rejected** words (non-food words)
- Shows **total word count** of the input

## 🛠️ Tech Stack

- Python 3
- Flask
- NLTK (tokenisation + multi-word expression handling)
- Jinja2 (server-side templating)
- jQuery (AJAX state transition lookup)
- Bootstrap 5

## 🔍 Supported Food Names

| Single Words | Multi-word Expressions |
|---|---|
| cake, cheesecake, chocolate, pudding | ice cream, black forest |
| pie, tart, macaron, pancake | banana boat, crème brûlée |
| tiramisu, soufflé, charlotte | |
| fruit, coffee | |

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/<your-username>/FoodFinder_DFA.git
cd FoodFinder_DFA

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python frontend.py
```

**Application will be available at `http://localhost:5000`**

## 📁 Project Structure

```
FoodFinder_DFA/
├── frontend.py              # Flask app — routes, form handling, /transition endpoint
├── food_dfa.py              # Core DFA logic — build, detect, transition, tokenise
├── templates/
│   └── find_food.html       # Jinja2 template — input, results, transition table
├── static/
│   └── index.js             # jQuery AJAX — fetches and renders transition table
├── requirements.txt         # Python dependencies
├── render.yaml              # Render deployment config
└── text.txt                 # Sample input text for testing
```

## ⚙️ How It Works

**1. Build DFA** — `food_dfa.build_dfa(foods)`

Constructs a trie-based DFA from the food list. Common prefixes share states (e.g. `cake` and `cheesecake` share the `c→a→k→e` path). Each food name's final character lands on an accept state.

**2. Tokenise** — `food_dfa.token(text)`

Uses NLTK's `MWETokenizer` to join multi-word expressions like `ice cream` into a single token before passing to the DFA.

**3. Detect** — `food_dfa.detect_food(word, dfa)`

Runs each token through the DFA character by character. Returns `True` if it lands on an accept state.

**4. Transition** — `food_dfa.transition(word, dfa)`

Returns a full state-by-state trace of the DFA for a given word, used to populate the transition table in the UI via AJAX.

## 🏗️ Deployment

Deployed on [Render](https://render.com) using `gunicorn` as the WSGI server.

```bash
# Production server
gunicorn frontend:app
```

The `render.yaml` handles:
- Installing dependencies
- Downloading NLTK tokeniser data at build time
- Auto-generating a secure `SECRET_KEY`
- Running the app with gunicorn
