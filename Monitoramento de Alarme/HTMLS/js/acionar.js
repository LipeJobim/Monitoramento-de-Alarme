
// Função para listar alarmes disponíveis
function listarAlarmesDisponiveis() {
    try {
        // Substitua a URL abaixo pela URL real da sua API Spring
        const apiUrl = "http://localhost:8080/alarmes";
        fetch(apiUrl)
            .then(response => response.json())
            .then(alarmes => {
                const alarmesDisponiveis = document.getElementById('alarmesDisponiveis');
                alarmesDisponiveis.innerHTML = ""; // Limpa a lista antes de adicionar os novos itens
                alarmes.forEach(alarme => {
                    alarmesDisponiveis.insertAdjacentHTML('beforeend', `<li>ID: ${alarme.id}, Local: ${alarme.locala}</li>`);
                });
            })
            .catch(error => {
                document.getElementById('resultado').textContent = `Erro na solicitação: ${error}`;
            });
    } catch (error) {
        document.getElementById('resultado').textContent = `Erro desconhecido: ${error}`;
    }
}

// Função para acionar o alarme
function acionarAlarme() {
    const idAlarme = document.getElementById('idAlarme').value;

    try {
        const apiUrl = `http://localhost:8080/alarmes/${idAlarme}/modificar-status`;
        fetch(apiUrl, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({}) // Envie um corpo vazio
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error ${response.status}`);
                }
                return response.text(); // Alterado para text para capturar o conteúdo do corpo da resposta
            })
            .then(result => {
                document.getElementById('resultado').textContent = result || 'Status do Alarme acionado com sucesso!';
            })
            .catch(error => {
                document.getElementById('resultado').textContent = `Erro na solicitação: ${error}`;
            });
    } catch (error) {
        document.getElementById('resultado').textContent = `Erro desconhecido: ${error}`;
    }

}