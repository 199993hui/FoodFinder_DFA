# FoodFinder DFA

🌐 **[Live Demo](https://foodfinder-dfa.onrender.com)**

A DFA (Deterministic Finite Automaton) based food name detection web app. Paste any text and it will identify food names, highlight them inline, show their positions, and visualise the DFA state transitions for each token.

## 🍰 Detection Capabilities

#### **Supported Food Names**
- **Desserts**: cake, cheesecake, chocolate, pudding, pie, tart, macaron, pancake, soufflé, charlotte, tiramisu
- **Multi-word Foods**: ice cream, black forest, banana boat, crème brûlée
- **Others**: fruit, coffee

#### **Text Analysis**
- **Tokenisation**: NLTK-powered tokeniser with multi-word expression (MWE) support — treats "ice cream", "black forest", etc. as single tokens
- **Case Insensitive Matching**: All input normalised to lowercase before DFA traversal
- **Inline Highlighting**: Detected food names bolded directly within the original text
- **Position Tracking**: Reports every word position where each food name appears
- **Accept/Reject Count**: Counts total accepted (food) words vs rejected (non-food) words

#### **DFA Visualisation**
- **Per-token State Transitions**: Select any token from the dropdown to see its full state transition table
- **Accept/Reject Badge**: Instantly shows whether the selected word was accepted or rejected by the DFA
- **Trap State Handling**: Rejected tokens show all transitions including the trap state (state `-1`)
- **AJAX-powered**: Transition table loads without page refresh via jQuery AJAX

## ⚡ Technical Details

#### **DFA Architecture**
- **Trie-based DFA Construction**: Builds a shared prefix trie from all food names — common prefixes share states (e.g. "cake" and "cheesecake" share the `c`, `a`, `k`, `e` path)
- **Trap State**: State `-1` is a dead/sink state; any unrecognised character transitions here and loops indefinitely
- **Accept States**: Final states of each food name path are collected into an accept state set
- **Single-pass Detection**: Each token is run through the DFA in one linear pass — O(n) per token

#### **Backend**
- **Flask**: Handles both form POST (text analysis) and GET with JSON (transition lookup)
- **Dual Response Modes**: Returns rendered HTML for the main form, and raw JSON for the AJAX transition table endpoint

#### **Frontend**
- **Jinja2 Templating**: Server-rendered results with inline food name highlighting via `|safe` filter
- **jQuery AJAX**: Fetches per-word transition data dynamically without full page reload
- **Bootstrap 5**: Responsive layout with cards, tables, and status badges

## 🛠️ Tech Stack

- Python 3.x
- Flask
- NLTK
- Jinja2
- jQuery 3.6
- Bootstrap 5.3

## 🎯 Core Features

- **Text Input**: Paste any free-form text and submit to detect food names
- **Highlighted Output**: Food names bolded inline within the original text
- **Food Name Table**: Lists every detected food with its count and word positions
- **State Transition Viewer**: Select any token to inspect its full DFA transition path and accept/reject status
- **Accept/Reject Summary**: Total count of accepted vs rejected tokens across the full input

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/<your-username>/FoodFinder_DFA.git
cd FoodFinder_DFA

# Install dependencies
pip install flask nltk

# Download NLTK tokeniser data
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

# Start the server
python frontend.py
```

**Application will be available at `http://localhost:5000`**

## 📁 Project Structure

```
FoodFinder_DFA/
├── frontend.py              # Flask app — routes, form handling, AJAX endpoint
├── food_dfa.py              # Core DFA logic — build, detect, transition, tokenise
├── templates/
│   └── find_food.html       # Jinja2 template — input form, results, transition table
├── static/
│   └── index.js             # jQuery AJAX — fetches and renders transition table
└── text.txt                 # Sample input text for testing
```
