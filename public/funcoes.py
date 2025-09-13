from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("apikey"))

def sendMessage(msg , history=[]):
    history.append({"role": "user", "content": msg})
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

def IaPersonalTrainer(msg=None, history=[], user_info={"age": None, "weight": None, "height": None, "objective": None, "salary": None, "days": None, "location": None}):
    
    system_prompt = f"""
    Você é um personal trainer virtual. Com base nas informações fornecidas pelo usuário, crie um plano de dieta e treino personalizados.

    Informações do Usuário:
    - Idade: {user_info['age']}
    - Peso: {user_info['weight']} kg
    - Altura: {user_info['height']} cm
    - Objetivo: {user_info['objective']}
    - Renda Salarial: {user_info['salary']}
    - Dias de Treino: {user_info['days']}
    - Local de Treino: {user_info['location']}

    Instruções Técnicas para a resposta:
    - Retorne a resposta EXCLUSIVAMENTE como um único bloco de código HTML.
    - O código deve estar estilizado para parecer um card moderno, usando CSS embutido.
    - O card principal deve ter a fonte 'Courier New', Courier, monospace.
    - O card deve conter duas seções principais: 'Dieta' e 'Treino'.
    - Para a seção 'Dieta', crie uma tabela HTML (<table>) com cabeçalhos 'Refeição', 'Alimento' e 'Quantidade'. O plano deve ser realista com base na renda salarial.
    - Para a seção 'Treino', crie uma tabela HTML (<table>) com cabeçalhos 'Dia', 'Exercício', 'Séries' e 'Repetições'. O plano deve ser adaptado para os dias e local de treino informados.

    Exemplo de formato para a resposta (o conteúdo real deve ser preenchido pela IA):
    
    <div style="font-family: 'Courier New', Courier, monospace; background-color: #f0f4f8; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
      <h2 style="color: #2c3e50; text-align: center;">Seu Plano Personalizado</h2>
      
      <div style="margin-top: 30px;">
        <h3 style="color: #3498db; border-bottom: 2px solid #3498db; padding-bottom: 5px;">Dieta</h3>
        <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
          <thead>
            <tr style="background-color: #ecf0f1;">
              <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Refeição</th>
              <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Alimento</th>
              <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Quantidade</th>
            </tr>
          </thead>
          <tbody>
            <!-- O conteúdo da tabela de dieta será preenchido aqui -->
          </tbody>
        </table>
      </div>

      <div style="margin-top: 30px;">
        <h3 style="color: #e74c3c; border-bottom: 2px solid #e74c3c; padding-bottom: 5px;">Treino</h3>
        <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
          <thead>
            <tr style="background-color: #ecf0f1;">
              <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Dia</th>
              <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Exercício</th>
              <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Séries</th>
              <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Repetições</th>
            </tr>
          </thead>
          <tbody>
            <!-- O conteúdo da tabela de treino será preenchido aqui -->
          </tbody>
        </table>
      </div>
    </div>
    
    """
    history.append({"role": "system", "content": system_prompt})
    history.append({"role": "user", "content": msg})
    try:
        completion = client.chat.completions.create(
            model="openrouter/sonoma-dusk-alpha",
            messages=history
        )
        res = completion.choices[0].message.content
        history.append({"role": "assistant", "content": res})
        return res
    except Exception as e:
        return f"Erro ao chamar a API: {str(e)}"
    
