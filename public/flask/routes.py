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

        prompt = f"Crie uma rotina de treino personalizada com base nos seguintes dados:\n" \
                 f"Objetivo: {objective}\nPeso: {weight}kg\nAltura: {height}cm"

        routine_response = sendMessage(prompt)
        return jsonify({'routine': routine_response})

    return render_template('page1.html')
