from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("apikey"))

def sendMessage(msg , history=[]):
    history.append({"role": "user", "content": msg})
    content = [{"type": "text", "text": msg}]
    try:
        completion = client.chat.completions.create(
            model="openrouter/sonoma-dusk-alpha",
            messages= history 
        )
        res = completion.choices[0].message.content
        history.append({"role": "assistant", "content": res})
        return res
    
    except Exception as e:
        return f"Erro ao chamar a API: {str(e)}"


 