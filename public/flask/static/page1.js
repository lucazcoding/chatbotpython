const header = document.querySelector('.header');
const trainingForm = document.getElementById('training-form');
const aiResponse = document.getElementById('ai-response');
const closeBtn = document.querySelector('.close-btn');

document.getElementById('training-form').addEventListener('submit', async function(event) {
    event.preventDefault(); 

    const location = document.getElementById('location').value;
    const objective = document.getElementById('objective').value;
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;
    const age = document.getElementById('age').value;
    const salary = document.getElementById('salary').value;
    const days = document.getElementById('days').value;

    const data = { location, objective, weight, height, age, salary, days };

    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify(data)
        });

        const result = await response.json(); 
        header.style.display = 'none';
        trainingForm.style.display = 'none';
        aiResponse.innerHTML = `<p> ${result.routine}</p>`;
        closeBtn.style.display = 'block';
    } catch (err) {
        console.error(err);
        document.getElementById('ai-response').innerHTML = `<p style="color:red;">Erro ao gerar rotina.</p>`;
    }
});

document.querySelector('.close-btn').addEventListener('click', () => {
    closeBtn.style.display = 'none';
    header.style.display = 'block';
    trainingForm.style.display = 'block';
    aiResponse.innerHTML = '';
})

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme && savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }
});

function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
}