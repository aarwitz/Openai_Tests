import base64
import requests

prompt = """
The submitted image is a Letter of Intent to Lease. Extract the clauses, including titles and content, and additionally include numbers, bullets, tabs, and newlines ('\t' and '\n') so that the structure of the clause content is preserved. Then store and format them as JSON like:
{
  "clauses": [
    {"title": "Clause 1", "content": "Content of Clause 1"},
    {"title": "Clause 2", "content": "Content of Clause 2"}
  ]
}
"""

# Set up OpenAI API key
with open('openaikey.txt', 'r') as file:
    # Read the contents of the file
    api_key = file.read()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def create_request(base64_images):
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o-mini",
    "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt.strip()
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_images[0]}"
                },
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_images[1]}"
                },
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_images[2]}"
                },
                }
            ]
            }
        ],
        "max_tokens": 1500
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    print(f'response: {response}')
    print(f'response.json(): {response.json()}')
    return response.json()['choices'][0]['message']['content']