import os
import requests
import json
import time

API_KEY = 'YOUR_API_KEY'
API_URL = 'https://api.groq.com/openai/v1/chat/completions'

def generate_prompts_and_save(source_dir, target_dir_base):
    if not os.path.exists(target_dir_base):
        os.makedirs(target_dir_base)

    files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]
    temperatures = [0.5 + 0.05 * i for i in range(10)] 
    request_count = 0

    for index, temp in enumerate(temperatures):
        target_dir = os.path.join(target_dir_base, f'batch_{index + 1}')
        os.makedirs(target_dir, exist_ok=True) 

        for filename in files:
            source_file_path = os.path.join(source_dir, filename)
            target_file_path = os.path.join(target_dir, filename)

            with open(source_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                original_text = lines[0].strip() 
                remaining_text = ''.join(lines[1:]) 

            generated_text = generate_text_with_api(original_text, temp)
            full_text = generated_text + '\n' + remaining_text 

            with open(target_file_path, 'w', encoding='utf-8') as file:
                file.write(full_text)

            print(f"Processed {filename} with temp {temp}")
            request_count += 1

            if request_count % 30 == 0:
                print("Pausing for 60 seconds to comply with API rate limits.")
                time.sleep(60)

def generate_text_with_api(text, temperature):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. What I am sending to you now is the text prompt of my project. These text instructions will be converted into embedding vectors and combined with my other point cloud data to generate the scene corresponding to the text prompt. Now I need you to help me overwrite this text prompt to improve the accuracy of the model. No extra words are needed, just ONLY provide the rewritten language."},
            {"role": "user", "content": text}
        ],
        "max_tokens": 100,
        "temperature": temperature,
        "n": 1
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = response.json()
        generated_text = response_data['choices'][0]['message']['content'].strip()
        return generated_text
    else:
        print(f"Failed to generate text: {response.status_code} {response.text}")
        return "Error in text generation"

source_directory = 'data/protext/proxd_train/context'
target_directory_base = 'data/protext/proxd_train/context_versions'

generate_prompts_and_save(source_directory, target_directory_base)
