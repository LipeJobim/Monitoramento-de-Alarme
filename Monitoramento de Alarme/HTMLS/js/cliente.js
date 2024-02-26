    function navegar(){
        fetch("file:///C:/Users/victor/OneDrive/%C3%81rea%20de%20Trabalho/PATP%20HTMLS/PATP%20HTMLS/descreveOcorrencia.html")
    }    
    
    
    
    
    function listarClientes() {
        var resultadoLabel = document.getElementById("resultado_label");
        resultadoLabel.textContent = ""; // Limpar a mensagem de resultado
        fetch("http://localhost:8080/clientes")
            .then(response => response.json())
            .then(clientes => preencherTabelaComDados(clientes))
            .catch(error => {
                resultadoLabel.textContent = "Erro ao listar clientes.";
            });
    }
    
    function criarCliente() {
        var resultadoLabel = document.getElementById("resultado_label");
        resultadoLabel.textContent = ""; // Limpar a mensagem de resultado
        limparCamposDoFormulario();
    
        resultadoLabel.textContent = "Cliente criado com sucesso!";
    }
    
    function limparCamposDoFormulario() {
        // Limpar os campos do formulário após criar o cliente
        document.getElementById("createNome").value = "";
        document.getElementById("createEmail").value = "";
        document.getElementById("createTelefone").value = "";
        document.getElementById("createEndereco").value = "";
        document.getElementById("createCpf").value = "";
        document.getElementById("createCep").value = "";
        document.getElementById("createDatanascimento").value = "";
        document.getElementById("createid").value = ""; // Limpar o campo oculto de ID
    }
    
    function deletarCliente() {
        var resultadoLabel = document.getElementById("resultado_label");
        resultadoLabel.textContent = ""; // Limpar a mensagem de resultado
    
        var tabela = document.getElementById("clientes_table");
        var linhasSelecionadas = tabela.querySelectorAll("tr.selected");
    
        if (linhasSelecionadas.length === 0) {
            resultadoLabel.textContent = "Selecione um cliente na tabela para deletar.";
        } else {
            var clienteSelecionado = linhasSelecionadas[0];
            var colunas = clienteSelecionado.getElementsByTagName("td");
            var clienteId = colunas[colunas.length - 1].textContent;
    
            // Chame a função para deletar o cliente com o ID obtido
            deletarClientePorId(clienteId);
        }
    }
    
    function deletarClientePorId(clienteId) {
        fetch("http://localhost:8080/clientes/apagar/" + parseInt(clienteId), {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => {
                console.log("Corpo da resposta:", data);
    
                if (data.ok) {
                    alert("Cliente deletado com sucesso!!");
                    console.log("Cliente deletado com sucesso!");
                    // Atualize a tabela ou faça qualquer outra ação necessária após a exclusão
                    
                } else {
                    alert("Falha ao deletar cliente!!");
                    console.error("Falha ao deletar cliente. Status: " + data.status);
                }
            })
            .catch(error => {
                console.error("Erro ao processar resposta:", error);
            });
    }
    
    function atualizarCliente() {
        var resultadoLabel = document.getElementById("resultado_label");
        resultadoLabel.textContent = ""; // Limpar a mensagem de resultado
    
        var tabela = document.getElementById("clientes_table");
        var linhasSelecionadas = tabela.querySelectorAll("tr.selected");
    
        if (linhasSelecionadas.length === 0) {
            resultadoLabel.textContent = "Selecione um cliente na tabela para atualizar.";
        } else {
            var clienteSelecionado = linhasSelecionadas[0];
            var colunas = clienteSelecionado.getElementsByTagName("td");
    
            var ultimaColunaIndex = colunas.length - 1;
    
            var cliente = {
                nome: colunas[0].textContent,
                email: colunas[1].textContent,
                telefone: colunas[2].textContent,
                endereco: colunas[3].textContent,
                cpf: colunas[4].textContent,
                cep: colunas[5].textContent,
                dataNascimento: colunas[6].textContent,
                id: colunas[ultimaColunaIndex].textContent
            };
    
            // Chame a função para abrir a janela de edição com os dados do cliente
            abrirJanelaEdicao(cliente);
    
            // Adicione a classe "selected" à linha para indicar que está em modo de edição
            clienteSelecionado.classList.add("selected");
        }
    }
    
    function abrirJanelaEdicao(cliente) {
        document.getElementById('editNome').value = cliente.nome;
        document.getElementById('editEmail').value = cliente.email;
        document.getElementById('editTelefone').value = cliente.telefone;
        document.getElementById('editEndereco').value = cliente.endereco;
        document.getElementById('editCpf').value = cliente.cpf;
        document.getElementById('editCep').value = cliente.cep;
        document.getElementById('editDatanascimento').value = cliente.dataNascimento;
    
        // Armazene o ID do cliente em um campo oculto
        document.getElementById('editId').value = cliente.id;
    
        // Abra a modal de edição
        var editarClienteModal = new bootstrap.Modal(document.getElementById('editarClienteModal'));
        editarClienteModal.show();
    }
    
    function preencherTabelaComDados(clientes) {
        var tableBody = document.querySelector("#clientes_table tbody");
        tableBody.innerHTML = ""; // Limpar a tabela antes de preenchê-la novamente
    
        clientes.forEach(function (cliente) {
            var row = document.createElement("tr");
    
            var nomeCell = document.createElement("td");
            nomeCell.textContent = cliente.nome || "Nome não encontrado";
    
            var emailCell = document.createElement("td");
            emailCell.textContent = cliente.email || "Email não encontrado";
    
            var telefoneCell = document.createElement("td");
            telefoneCell.textContent = cliente.telefone || "Telefone não encontrado";
    
            var enderecoCell = document.createElement("td");
            enderecoCell.textContent = cliente.endereco || "Endereço não encontrado";
    
            var cpfCell = document.createElement("td");
            cpfCell.textContent = cliente.cpf || "CPF não encontrado";
    
            var cepCell = document.createElement("td");
            cepCell.textContent = cliente.cep || "CEP não encontrado";
    
            var dataNascimentoCell = document.createElement("td");
            dataNascimentoCell.textContent = cliente.dataNascimento || "Data de Nascimento não encontrada";
    
            var dataCadastroCell = document.createElement("td");
            dataCadastroCell.textContent = cliente.created_at || "Data de Cadastro não encontrada";
    
            var idCell = document.createElement("td");
            idCell.textContent = cliente.id || "ID não encontrado";
            idCell.style.display = "none";
    
            row.appendChild(nomeCell);
            row.appendChild(emailCell);
            row.appendChild(telefoneCell);
            row.appendChild(enderecoCell);
            row.appendChild(cpfCell);
            row.appendChild(cepCell);
            row.appendChild(dataNascimentoCell);
            row.appendChild(dataCadastroCell);
            row.appendChild(idCell);
    
            row.addEventListener("click", function () {
                if (row.classList.contains("selected")) {
                    row.classList.remove("selected");
                } else {
                    row.classList.add("selected");
                }
            });
    
            tableBody.appendChild(row);
        });
    }
    function salvarEdicaoCliente() {
        var editId = document.getElementById('editId').value;
        var editNome = document.getElementById('editNome').value;
        var editEmail = document.getElementById('editEmail').value;
        var editTelefone = document.getElementById('editTelefone').value;
        var editEndereco = document.getElementById('editEndereco').value;
        var editCpf = document.getElementById('editCpf').value;
        var editCep = document.getElementById('editCep').value;
        var editDatanascimento = document.getElementById('editDatanascimento').value;
    
        var urlAtualizarCliente = "http://localhost:8080/clientes/atualizar" + editId;
    
        var dadosAtualizados = {
            id: editId,
            nome: editNome,
            email: editEmail,
            telefone: editTelefone,
            endereco: editEndereco,
            cpf: editCpf,
            cep: editCep,
            dataNascimento: editDatanascimento
            // Inclua os outros campos conforme necessário...
        };
    
        fetch(urlAtualizarCliente, {
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
                console.log("Cliente atualizado com sucesso!");
    
                // Exibir um alerta
                alert("Cliente atualizado com sucesso!");
                listarClientes();
            })
            .catch(error => {
                console.error("Erro ao processar resposta:", error);
            });
    }
    
    
    function abrirJanelaCliente(cliente) {
        if (cliente) {
            // Se o cliente existir, preencha os campos de edição
            document.getElementById('editNome').value = cliente.nome;
            document.getElementById('editEmail').value = cliente.email;
            document.getElementById('editTelefone').value = cliente.telefone;
            document.getElementById('editEndereco').value = cliente.endereco;
            document.getElementById('editCpf').value = cliente.cpf;
            document.getElementById('editCep').value = cliente.cep;
            document.getElementById('editDatanascimento').value = cliente.dataNascimento;
    
            // Armazene o ID do cliente em um campo oculto
            document.getElementById('editId').value = cliente.id;
    
            // Abra a modal de edição
            var editarClienteModal = new bootstrap.Modal(document.getElementById('editarClienteModal'));
            editarClienteModal.show();
        } else {
            // Se não houver cliente (criação), limpe os campos de edição
            document.getElementById('createNome').value = "";
            document.getElementById('createEmail').value = "";
            document.getElementById('createTelefone').value = "";
            document.getElementById('createEndereco').value = "";
            document.getElementById('createCpf').value = "";
            document.getElementById('createCep').value = "";
            document.getElementById('createDatanascimento').value = "";
    
            // Limpe o campo oculto de ID
            document.getElementById('createid').value = "";
    
            // Abra a modal de criação
            var criarClienteModal = new bootstrap.Modal(document.getElementById('criarClienteModal'));
            criarClienteModal.show();
        }
    }
    
    
    function salvarNovoCliente() {

        var createId = null;
        var createNome = document.getElementById('createNome').value;
        var createEmail = document.getElementById('createEmail').value;
        var createTelefone = document.getElementById('createTelefone').value;
        var createEndereco = document.getElementById('createEndereco').value;
        var createCpf = document.getElementById('createCpf').value;
        var createCep = document.getElementById('createCep').value;
        var createDatanascimento = document.getElementById('createDatanascimento').value;
    
        var urlCriarCliente = "http://localhost:8080/cadastrar/cliente";
    
        var dadosCriados = {
            id: createId,
            nome: createNome,
            email: createEmail,
            telefone: createTelefone,
            endereco: createEndereco,
            cpf: createCpf,
            cep: createCep,
            dataNascimento: createDatanascimento


        };
    
        fetch(urlCriarCliente, {
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
                console.log("Cliente criado com sucesso!");
    
                // Exibir um alerta
                alert("Cliente criado com sucesso!");
    
                // Atualize a tabela ou faça qualquer outra ação necessária após a criação
                listarClientes();
            })
            .catch(error => {
                console.error("Erro ao processar resposta:", error);
            });
    }
    
   
    function fechar() {
        var editarClienteModal = new bootstrap.Modal(document.getElementById('editarClienteModal'));
        editarClienteModal.hide();
    }
    