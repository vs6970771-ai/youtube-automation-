import os
import requests


def generate_script(topic, category, language, duration):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OpenAI API key is not configured")

    prompt = f"""
    Create an engaging YouTube Shorts script.

    Topic: {topic}
    Category: {category}
    Language: {language}
    Duration: {duration} seconds

    Requirements:
    - Powerful opening hook
    - Engaging storytelling
    - Short sentences
    - Strong ending
    - Scene-by-scene narration
    - Original content
    """

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.8
        },
        timeout=60
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
