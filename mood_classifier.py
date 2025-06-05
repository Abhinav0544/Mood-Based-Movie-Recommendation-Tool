import subprocess

def get_mood_from_plot(plot):
    prompt = f"""You are a movie mood classifier. Given this plot, reply with a few comma-separated mood tags only (like 'feel-good', 'intense', 'romantic', 'dark', 'uplifting', 'emotional').

Plot:
{plot}

Mood tags:"""
    result = subprocess.run(
        ["ollama", "run", "phi"],
        input=prompt,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
