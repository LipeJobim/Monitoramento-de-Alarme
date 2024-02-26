function listarRegistros() {
    var resultadoLabel = document.getElementById("resultado_label");
    resultadoLabel.textContent = "";

    fetch('http://localhost:8080/listarTodos')
        .then(response => response.json())
        .then(registros => preencherTabelaComDados(registros))
        .catch(error => {
            resultadoLabel.textContent = "Erro ao listar registros.";
        });
}

function preencherTabelaComDados(registros) {
    const registrosBody = document.querySelector('#registros_table tbody');
    registrosBody.innerHTML = '';

    registros.forEach(registro => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${registro.id}</td>
            <td>${registro.idVigilante ? registro.idVigilante.nome : ''}</td>
            <td>${registro.descricao}</td>
            <td>${registro.horarioRegistro}</td>
            <td>${registro.motivoAcionamento}</td>
        `;
        registrosBody.appendChild(row);
    });
}

