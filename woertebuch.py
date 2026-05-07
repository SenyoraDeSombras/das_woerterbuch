import os
import sys
from typing import Optional

import openai
from openai import OpenAI

# --- Configuration ---
# Using environment variables is best practice for GitHub so users can customize easily
BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:8080/v1")
API_KEY = os.getenv("LLM_API_KEY", "ollama")
MODEL_NAME = os.getenv("LLM_MODEL", "gemma4")
TIMEOUT = 250

SYSTEM_PROMPT = """
Role: You are a German-Russian dictionary.
Input: A single German word or a comma-separated list of words.
Task: For each word provided, you must return:
    1. The Russian translation.
    2. A definition in German.
    3. Morphological/inflectional details.
    4. For nouns: specify the gender and provide the singular form (if the input was plural).
    5. Any other relevant dictionary information (usage notes, etymology, examples) if appropriate.

Output Format: Use terminal-friendly formatting (e.g., code blocks, monospace font, or clear ASCII separators) to ensure readability.
"""

def get_dictionary_translation(client: OpenAI, user_input: str) -> Optional[str]:

    #Sends the user input to the LLM and returns the formatted translation.

    try:
        print(f"🔍 Translating: {user_input}...")
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input.strip()},
            ],
            temperature=0.8,
            timeout=TIMEOUT
        )
        return response.choices[0].message.content

    except openai.APIError as e:
        print(f"❌ API Error: {e}")
    except openai.APITimeoutError:
        print("❌ Error: The request timed out.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    
    return None

def main():

    #Main execution loop for the CLI tool.

    # Initialize client
    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    print("--- German-Russian Dictionary CLI ---")
    print("Type 'exit' or 'nowords' to quit.")

    while True:
        try:
            user_input = input("\nEnter German word(s): ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["nowords", "exit", "quit"]:
                print("👋 Goodbye!")
                break

            result = get_dictionary_translation(client, user_input)

            if result:
                print("\n" + "="*30)
                print(result)
                print("="*30)

        except KeyboardInterrupt:
            print("\n👋 Interrupted by user. Exiting...")
            break

if __name__ == "__main__":
    main()
