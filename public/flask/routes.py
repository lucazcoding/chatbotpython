from app import app
from flask import render_template, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from funcoes import sendMessage

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        objective = data.get('objective')
        weight = data.get('weight')
        height = data.get('height')

        prompt = f"""
Crie uma rotina de alimentação e treino personalizada baseada nos dados do usuário:

- Objetivo: {objective}
- Peso: {weight} kg
- Altura: {height} cm

O retorno deve ser APENAS em HTML válido, no seguinte formato:

<h2>Seu Plano de Treino</h2>
<p>Plano semanal para {objective}. Consulte um médico antes de iniciar.</p>

<table>
  <tr>
    <th>Refeição</th>
    <th>Alimento</th>
    <th>Quantidade</th>
  </tr>
  <tr>
    <th>Dia</th>
    <th>Exercício</th>
    <th>Séries</th>
  </tr>
  <!-- repita para cada dia -->
</table>

Nada além desse HTML deve ser retornado sem infomações adicionais, apenas as tabelas.
"""

        routine_response = sendMessage(prompt)
        return jsonify({'routine': routine_response})

    return render_template('page1.html')
