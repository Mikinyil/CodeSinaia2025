import ollama
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = "context_prompt.txt"

file_path = os.path.join(script_dir, filename)

with open(file_path, 'r', encoding='utf-8') as f:
    file_text = f.read()

class SmartAgent:
    def __init__(self, model):
        self.model_name = model
        self.chat_log = []

    def chat(self, message):
        self.chat_log.append({'role':'user','content':file_text})
        self.chat_log.append({'role':'user','content':message})
        answer = ollama.chat(
            model=self.model_name,
            messages=self.chat_log)
        answer_text = answer['message']['content']
        self.chat_log.append({'role':'agent', 'content':answer_text})
        return (answer)