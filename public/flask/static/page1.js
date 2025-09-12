function toggleTheme() 
    {
            const body = document.body;
            body.classList.toggle('dark-mode');
    }



document.getElementById('training-form').addEventListener('submit', async function(event) {
    event.preventDefault(); 

    // Captura os valores de todos os campos do formulário
    const objective = document.getElementById('objective').value;
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;
    const age = document.getElementById('age').value;
    const salary = document.getElementById('salary').value;
    const days = document.getElementById('days').value;

    // Cria um objeto 'data' com todos os valores
    const data = { objective, weight, height, age, salary, days };

    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify(data)
        });

        const result = await response.json(); 
        document.getElementById('ai-response').innerHTML = `<p><b>Sonoma:</b> ${result.routine}</p>`;
    } catch (err) {
        console.error(err);
        document.getElementById('ai-response').innerHTML = `<p style="color:red;">Erro ao gerar rotina.</p>`;
    }
});



document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme && savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }
});