document.getElementById('training-form').addEventListener('submit', async function(event) {
    event.preventDefault(); 

    const objective = document.getElementById('objective').value;
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;

    const data = { objective, weight, height };

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