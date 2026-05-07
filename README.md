# 🇩🇪 German-Russian LLM Dictionary CLI 🇷🇺

A lightweight, terminal-based dictionary tool that leverages Large Language Models (LLMs) to provide high-quality German-to-Russian translations. Unlike standard dictionaries, this tool provides deep linguistic context, including German definitions, morphological details, and grammatical corrections.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **Smart Translation:** Converts German words or lists into Russian.
- **Linguistic Depth:** Provides German definitions, etymology, and usage notes.
- **Grammar Intelligence:** Automatically identifies noun genders and provides singular forms for plural inputs.
- **Local LLM Ready:** Designed to work seamlessly with **Ollama** or any OpenAI-compatible API provider.
- **Terminal Optimized:** Clean, monospace output formatted for easy reading in your terminal.

## 🚀 Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- An OpenAI-compatible API server (e.g., [Ollama](https://ollama.com/))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/german-russian-dict.git
   cd german-russian-dict
   ```

2. **Install dependencies:**
   ```bash
   pip install openai
   ```

### Configuration

The application uses environment variables for configuration. This allows you to switch between local models and cloud APIs without changing the code.

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `LLM_BASE_URL` | The API endpoint (e.g., Ollama URL) | `http://localhost:8080/v1` |
| `LLM_API_KEY` | Your API key (use `ollama` for local) | `ollama` |
| `LLM_MODEL` | The name of the model to use | `gemma4` |

### Usage

Run the script via your terminal:

```bash
# Using default settings (Local Ollama)
python main.py

# Using a specific model or remote API
LLM_MODEL="llama3" python main.py
```

## 📖 Example Output

**Input:**
```text
Enter German word(s): Haus
```

**Output:**
```text
==============================
Haus
==============================
Translation: дом (Russian)
Definition: ein Gebäude, in dem Menschen wohnen.
Gender: neuter (das Haus)
Plural: Häuser
Note: ...
==============================
```

## 🛠️ Technical Details

- **Engine:** Uses the `openai` Python library to communicate with LLM backends.
- **Prompt Engineering:** Utilizes a specialized System Prompt to enforce dictionary-style formatting and grammatical accuracy.
- **Error Handling:** Built-in handling for API timeouts, connection errors, and user interruptions (`Ctrl+C`).

## 📄 License

Distributed under the GPL License. See `LICENSE` for more information.

