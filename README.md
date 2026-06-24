# Food Name Detector using DFA Algorithm

🌐 **[Live Demo](https://foodfinder-dfa.onrender.com)**

A web application that detects food names in free-form text using a **Deterministic Finite Automaton (DFA)** — a concept from the Theory of Computation. Built as a full-stack project with a Python/Flask backend and a dynamic frontend that visualises DFA state transitions in real time.

## 💡 What is a DFA?

A Deterministic Finite Automaton (DFA) is a theoretical model of computation. It reads an input string character by character, moving between states according to a transition function. If it ends in an **accept state**, the input is recognised. If it ends in a **trap/dead state**, the input is rejected.

In this project, the DFA is built from a predefined list of food names. Each food name creates a unique path of states through the DFA:
- Every character moves the DFA to the next state
- If the final state is an **accept state** → the word is a food name ✅
- If not → the word is rejected ❌

Multi-word expressions like `ice cream` and `black forest` are handled by NLTK's `MWETokenizer`, which joins them into a single token before passing to the DFA.

## 🍕 Features

#### **Food Detection**
- Paste any free-form text and detect all food names instantly
- Supports 18 food names including multi-word expressions
- Detected food names are **highlighted in bold** inline within the original text
- Shows each food name's **count** and **word position** in the text
- A predefined food list is shown in the UI so users know what can be detected

#### **DFA State Transition Visualisation**
- After searching, select any token from the dropdown
- Click **Check** to fetch the full state transition table for that word via AJAX
- Shows each character, the current state, and the next state step by step
- Displays **Accepted** (green) or **Rejected** (red) status badge

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
- Deployed on Render with Gunicorn

## 🔍 Supported Food Names

| Single Words | Multi-word Expressions |
|---|---|
| cake, cheesecake, chocolate, pudding | ice cream, black forest |
| pie, tart, macaron, pancake | banana boat, crème brûlée |
| tiramisu, soufflé, charlotte | |
| banana, fruit, coffee | |

> Only these 18 food names are detectable. Any other word will be marked as rejected.

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
│   └── find_food.html       # Jinja2 template — input, results, transition table UI
├── static/
│   └── index.js             # jQuery AJAX — fetches and renders transition table
├── requirements.txt         # Python dependencies (flask, nltk, gunicorn)
├── render.yaml              # Render deployment config
└── text.txt                 # Sample input text for testing
```

## ⚙️ How It Works

**1. Build DFA** — `build_dfa(foods)` in `food_dfa.py`

Constructs a trie-based DFA from the food list. Common prefixes share states — for example `cake` and `cheesecake` share the `c→a→k→e` path. Each food name's final character lands on an accept state. A trap state (`-1`) catches all unrecognised characters.

**2. Tokenise** — `token(text)` in `food_dfa.py`

Uses NLTK's `MWETokenizer` to join multi-word expressions (`ice cream`, `black forest`, `banana boat`, `crème brûlée`) into single tokens before running through the DFA.

**3. Detect** — `detect_food(word, dfa)` in `food_dfa.py`

Runs each token through the DFA character by character. Returns `True` if it ends on an accept state.

**4. Position** — `position(tokens, detected_food_names, accept)` in `food_dfa.py`

Filters out punctuation, then records the word position of each detected food name and calculates the accepted/rejected word counts.

**5. Transition** — `transition(word, dfa)` in `food_dfa.py`

Returns a full state-by-state trace of the DFA for a given word. This is called via the `/transition` GET endpoint and rendered as a table in the UI using jQuery AJAX.

## 🏗️ Deployment

Deployed on [Render](https://render.com) using `gunicorn` as the production WSGI server.

```bash
gunicorn frontend:app
```

`render.yaml` handles:
- Installing all dependencies from `requirements.txt`
- Downloading NLTK tokeniser data (`punkt`, `punkt_tab`) at build time
- Auto-generating a secure `SECRET_KEY` environment variable
- Running the app with gunicorn in production mode
