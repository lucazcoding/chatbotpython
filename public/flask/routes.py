from app import app
from flask import render_template, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from funcoes import IaPersonalTrainer

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        location = data.get('location')
        objective = data.get('objective')
        weight = data.get('weight')
        height = data.get('height')
        age = data.get('age')
        salary = data.get('salary')
        days = data.get('days')

        routine_response = IaPersonalTrainer("Preciso de um plano de treino e dieta para ganhar massa muscular.", user_info={"age": age, "weight": weight, "height": height, "objective": objective, "salary": salary, "days": days, "location": location})
        return jsonify({'routine': routine_response})

    return render_template('page1.html')
