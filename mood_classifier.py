# mood_classifier.py

from llama_cpp import Llama

# Load your local LLaMA 3 model
llm = Llama(model_path="/Users/abhinavjaikumar/Downloads/llama-3-8b-Instruct.Q4_K_M.gguf")

def infer_mood(prompt: str) -> str:
    """
    Uses LLaMA to classify mood from a free-text user prompt.
    Returns a single mood like: 'dark', 'uplifting', 'emotional', 'intense', 'chill', etc.
    """
    system_prompt = (
        "You are a helpful assistant that classifies the user's emotional mood based on their input.\n"
        "Return only a **single mood word** such as 'dark', 'uplifting', 'emotional', 'chill', 'intense', 'fun', or 'romantic'.\n"
        "Do not include any explanation, just output the mood."
    )

    full_prompt = f"{system_prompt}\n\nUser: {prompt}\nMood:"
    response = llm(full_prompt, max_tokens=10, stop=["\n", "."])

    mood = response["choices"][0]["text"].strip().lower()
    return mood
