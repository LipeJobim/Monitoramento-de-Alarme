function listarVigilantes() {
    var resultadoLabel = document.getElementById("resultado_label");
    resultadoLabel.textContent = ""; // Limpar a mensagem de resultado

    fetch("http://localhost:8080/vigilantes")
        .then(response => response.json())
        .then(vigilantes => preencherTabelaComDados(vigilantes))
        .catch(error => {
            resultadoLabel.textContent = "Erro ao listar vigilantes.";
        });
}

function preencherTabelaComDados(vigilantes) {
    var tableBody = document.querySelector("#vigilantes_table tbody");
    tableBody.innerHTML = ""; // Limpar a tabela antes de preenchê-la novamente

    vigilantes.forEach(function (vigilante) {
        var row = document.createElement("tr");

        var nomeCell = document.createElement("td");
        nomeCell.textContent = vigilante.nome || "Nome não encontrado";

        var idCell = document.createElement("td");
        idCell.textContent = vigilante.id || "ID não encontrado";
        idCell.style.display = "none";

        row.appendChild(nomeCell);
        row.appendChild(idCell);

        row.addEventListener("click", function () {
            if (row.classList.contains("selected")) {
                row.classList.remove("selected");
            } else {
                // Remove a seleção de todas as linhas
                var todasLinhas = document.querySelectorAll("#vigilantes_table tbody tr");
                todasLinhas.forEach(function (linha) {
                    linha.classList.remove("selected");
                });

                // Adiciona a seleção à linha clicada
                row.classList.add("selected");
            }
        });

        // Adiciona um evento para clicar no nome e acionar a seleção
        nomeCell.addEventListener("click", function (event) {
            // Impede que o evento de clique da linha seja acionado
            event.stopPropagation();
            // Simula um clique na linha
            row.click();
        });

        tableBody.appendChild(row);
    });
}

function deletarVigilante() {
    var resultadoLabel = document.getElementById("resultado_label");
    resultadoLabel.textContent = ""; // Limpar a mensagem de resultado

    var tabela = document.getElementById("vigilantes_table");
    var linhasSelecionadas = tabela.querySelectorAll("tr.selected");

    if (linhasSelecionadas.length === 0) {
        resultadoLabel.textContent = "Selecione um vigilante na tabela para deletar.";
    } else {
        var vigilanteSelecionado = linhasSelecionadas[0];
        var colunas = vigilanteSelecionado.getElementsByTagName("td");
        var vigilanteId = colunas[colunas.length - 1].textContent;

        // Chame a função para deletar o vigilante com o ID obtido
        deletarVigilantePorId(vigilanteId, resultadoLabel);
    }
}

function deletarVigilantePorId() {
    fetch("http://localhost:8080/vigilantes/" + parseInt(vigilanteId), {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log("Corpo da resposta:", data);

            if (data.ok) {
                resultadoLabel.textContent = "Vigilante deletado com sucesso!";
                console.log("Vigilante deletado com sucesso!");
                // Atualize a tabela ou faça qualquer outra ação necessária após a exclusão
                listarVigilantes();
            } else {
                resultadoLabel.textContent = "Falha ao deletar vigilante!";
                console.error("Falha ao deletar vigilante. Status: " + data.status);
            }
        })
        .catch(error => {
            console.error("Erro ao processar resposta:", error);
        });
}

function criarVigilante() {
    var resultadoLabel = document.getElementById("resultado_label");
    resultadoLabel.textContent = ""; // Limpar a mensagem de resultado
    limparCamposDoFormulario();

    // Abra a modal de criação
    var criarVigilanteModal = new bootstrap.Modal(document.getElementById('criarVigilanteModal'));
    criarVigilanteModal.show();
}

function limparCamposDoFormulario() {
    // Limpar os campos do formulário após criar o vigilante
    document.getElementById("createNome").value = "";
    document.getElementById("createId").value = ""; // Limpar o campo oculto de ID
}

function atualizarVigilante() {
    var resultadoLabel = document.getElementById("resultado_label");
    resultadoLabel.textContent = ""; // Limpar a mensagem de resultado

    var tabela = document.getElementById("vigilantes_table");
    var linhasSelecionadas = tabela.querySelectorAll("tr.selected");

    if (linhasSelecionadas.length === 0) {
        resultadoLabel.textContent = "Selecione um vigilante na tabela para atualizar.";
    } else {
        var vigilanteSelecionado = linhasSelecionadas[0];
        var colunas = vigilanteSelecionado.getElementsByTagName("td");

        var ultimaColunaIndex = colunas.length - 1;

        var vigilante = {
            nome: colunas[0].textContent,
            id: colunas[ultimaColunaIndex].textContent
        };

        // Preencha o formulário de edição com os dados do vigilante
        document.getElementById('editNome').value = vigilante.nome;
        document.getElementById('editId').value = vigilante.id;

        // Abra a modal de edição
        var editarVigilanteModal = new bootstrap.Modal(document.getElementById('editarVigilanteModal'));
        editarVigilanteModal.show();

        // Adicione a classe "selected" à linha para indicar que está em modo de edição
        vigilanteSelecionado.classList.add("selected");
    }
}

function salvarEdicaoVigilante() {
    var resultadoLabel = document.getElementById("resultado_label");
    resultadoLabel.textContent = ""; // Limpar a mensagem de resultado

    var editId = document.getElementById('editId').value;
    var editNome = document.getElementById('editNome').value;

    var urlAtualizarVigilante = "http://localhost:8080/vigilantes/atualizar/" + editId;

    var dadosAtualizados = {
        id: editId,
        nome: editNome
    };

    fetch(urlAtualizarVigilante, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dadosAtualizados)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log("Corpo da resposta:", data);
            console.log("Vigilante atualizado com sucesso!");

            // Exibir mensagem de sucesso no resultadoLabel
            resultadoLabel.textContent = "Vigilante atualizado com sucesso!";

            // Atualize a tabela ou faça qualquer outra ação necessária após a atualização
            listarVigilantes();
        })
        .catch(error => {
            console.error("Erro ao processar resposta:", error);
        });
}

function salvarNovoVigilante() {
    var createId = null;
    var createNome = document.getElementById('createNome').value;

    var urlCriarVigilante = "http://localhost:8080/cadastrar/vigilante";

    var dadosCriados = {
        id: createId,
        nome: createNome
    };

    fetch(urlCriarVigilante, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dadosCriados)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log("Corpo da resposta:", data);
            console.log("Vigilante criado com sucesso!");

            // Exibir mensagem de sucesso no resultadoLabel
            resultadoLabel.textContent = "Vigilante criado com sucesso!";

            // Feche a modal de criação
            var criarVigilanteModal = new bootstrap.Modal(document.getElementById('criarVigilanteModal'));
            criarVigilanteModal.hide();

            // Atualize a tabela ou faça qualquer outra ação necessária após a criação
            listarVigilantes();
        })
        .catch(error => {
            console.error("Erro ao processar resposta:", error);
        });
}
