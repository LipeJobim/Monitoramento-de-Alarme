import json
import tkinter as tk
from tkinter import ttk

import requests

def label()
def button()

def cadastrar_cliente():
    def cadastrar():
        nome = nome_entry.get()
        email = email_entry.get()
        data_nascimento = data_nascimento_entry.get()
        endereco = endereco_entry.get()
        telefone = telefone_entry.get()
        cep = cep_entry.get()
        cpf = cpf_entry.get()

        # Criar um dicionário com os dados do cliente
        dados = {
            "nome": nome,
            "email": email,
            "dataNascimento": data_nascimento,
            "endereco": endereco,
            "telefone": telefone,
            "cep": cep,
            "cpf": cpf
        }
        print(dados)

        # URL da sua API Spring para cadastrar clientes
        url_da_api = "http://localhost:8080/cadastrar/cliente"  # Substitua pela URL real da sua API

        headers = {'Content-Type': 'application/json'}

        json.dumps(dados, ensure_ascii=False)

        try:
            # Enviar os dados para a API Spring usando uma requisição POST
            response = requests.post(url_da_api, data=json.dumps(dados), headers=headers)

            if response.status_code == 200:
                result_label.config(text="Cliente cadastrado com sucesso.")
            else:
                result_label.config(text=f"Falha ao cadastrar cliente. Status: {response.status_code}")
        except Exception as e:
            result_label.config(text=f"Erro ao cadastrar cliente: {str(e)}")

    root = tk.Tk()
    root.title("Cadastro de Cliente")

    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=20)

    nome_label = ttk.Label(frame, text="Nome:")
    nome_label.grid(row=0, column=0)
    nome_entry = ttk.Entry(frame)
    nome_entry.grid(row=0, column=1)

    email_label = ttk.Label(frame, text="Email:")
    email_label.grid(row=1, column=0)
    email_entry = ttk.Entry(frame)
    email_entry.grid(row=1, column=1)

    data_nascimento_label = ttk.Label(frame, text="Data de Nascimento:")
    data_nascimento_label.grid(row=2, column=0)
    data_nascimento_entry = ttk.Entry(frame)
    data_nascimento_entry.grid(row=2, column=1)

    endereco_label = ttk.Label(frame, text="Endereço:")
    endereco_label.grid(row=3, column=0)
    endereco_entry = ttk.Entry(frame)
    endereco_entry.grid(row=3, column=1)

    telefone_label = ttk.Label(frame, text="Telefone:")
    telefone_label.grid(row=4, column=0)
    telefone_entry = ttk.Entry(frame)
    telefone_entry.grid(row=4, column=1)

    cep_label = ttk.Label(frame, text="CEP:")
    cep_label.grid(row=5, column=0)
    cep_entry = ttk.Entry(frame)
    cep_entry.grid(row=5, column=1)

    cpf_label = ttk.Label(frame, text="CPF:")
    cpf_label.grid(row=6, column=0)
    cpf_entry = ttk.Entry(frame)
    cpf_entry.grid(row=6, column=1)

    cadastrar_button = ttk.Button(frame, text="Cadastrar", command=cadastrar)
    cadastrar_button.grid(row=7, columnspan=2)

    result_label = ttk.Label(frame, text="")
    result_label.grid(row=8, columnspan=2)

    root.mainloop()


def listar_clientes():
    def listar_clientes():
        # Limpar a tabela
        for row in clientes_treeview.get_children():
            clientes_treeview.delete(row)

        # Fazer uma solicitação GET para a API Spring para obter a lista de clientes
        response = requests.get("http://localhost:8080/clientes")

        if response.status_code == 200:
            dados_json = response.json()

            for cliente in dados_json:
                # Extrair os dados desejados
                nome = cliente.get("nome", "Nome não encontrado")
                email = cliente.get("email", "Email não encontrado")
                nasc = cliente.get("dataNascimento", "Data Nascimento não encontrado")
                endereco = cliente.get("endereco", "Endereço não encontrado")
                telefone = cliente.get("telefone", "Telefone não encontrado")
                cep = cliente.get("cep", "CEP não encontrado")
                cpf = cliente.get("cpf", "CPF não encontrado")
                idCliente = cliente.get("id", "ID não encontrado")

                # Adicionar os dados à tabela
                clientes_treeview.insert('', 'end',
                                         values=(nome, nasc, email, telefone, endereco, cep, cpf, idCliente,))
        else:
            resultado_label.config(text="Erro ao buscar clientes da API")

    def mostrar_detalhes(event):
        item = clientes_treeview.selection()
        if item:
            item = item[0]
            cliente = clientes_treeview.item(item, 'values')
            resultado_label.config(
                text=f"Detalhes do Cliente:\nNome: {cliente[0]}, Data Nascimento: {cliente[1]}, Email: {cliente[2]}, Telefone: {cliente[3]},"
                     f"Endereço: {cliente[4]}, CEP: {cliente[5]}, CPF: {cliente[6]}, ID: {cliente[7]}")
        else:
            resultado_label.config(text="Selecione um cliente")

    def atualizar_cliente():
        item = clientes_treeview.selection()
        if item:
            item = item[0]
            cliente = clientes_treeview.item(item, 'values')
            # Abra a janela de edição com campos para todos os dados
            editar_cliente_window(cliente)
        else:
            resultado_label.config(text="Selecione um cliente")

    def editar_cliente_window(cliente):
        global editar_cliente_dialog
        editar_cliente_dialog = tk.Toplevel(root)
        editar_cliente_dialog.title("Editar Cliente")

        # Crie rótulos e campos de entrada para edição
        nome_label = tk.Label(editar_cliente_dialog, text="Nome:")
        nome_label.pack()
        nome_entry = tk.Entry(editar_cliente_dialog)
        nome_entry.insert(0, cliente[0])
        nome_entry.pack()

        email_label = tk.Label(editar_cliente_dialog, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(editar_cliente_dialog)
        email_entry.insert(0, cliente[2])
        email_entry.pack()

        nasc_label = tk.Label(editar_cliente_dialog, text="Data Nascimento:")
        nasc_label.pack()
        nasc_entry = tk.Entry(editar_cliente_dialog)
        nasc_entry.insert(0, cliente[1])
        nasc_entry.pack()

        telefone_label = tk.Label(editar_cliente_dialog, text="Telefone:")
        telefone_label.pack()
        telefone_entry = tk.Entry(editar_cliente_dialog)
        telefone_entry.insert(0, cliente[3])
        telefone_entry.pack()

        endereco_label = tk.Label(editar_cliente_dialog, text="Endereço:")
        endereco_label.pack()
        endereco_entry = tk.Entry(editar_cliente_dialog)
        endereco_entry.insert(0, cliente[4])
        endereco_entry.pack()

        cep_label = tk.Label(editar_cliente_dialog, text="CEP:")
        cep_label.pack()
        cep_entry = tk.Entry(editar_cliente_dialog)
        cep_entry.insert(0, cliente[5])
        cep_entry.pack()

        cpf_label = tk.Label(editar_cliente_dialog, text="CPF:")
        cpf_label.pack()
        cpf_entry = tk.Entry(editar_cliente_dialog)
        cpf_entry.insert(0, cliente[6])
        cpf_entry.pack()

        idCliente_label = tk.Label(editar_cliente_dialog, text="ID Cliente:")
        idCliente_label.pack()
        idCliente_entry = tk.Entry(editar_cliente_dialog)
        idCliente_entry.insert(0, cliente[7])
        idCliente_entry.pack()

        salvar_button = tk.Button(editar_cliente_dialog, text="Salvar",
                                  command=lambda: salvar_edicao_cliente(cliente, nome_entry, email_entry, nasc_entry,
                                                                        telefone_entry, endereco_entry, cep_entry,
                                                                        cpf_entry, idCliente_entry))
        salvar_button.pack()

    def salvar_edicao_cliente(cliente, nome_entry, email_entry, nasc_entry, telefone_entry, endereco_entry, cep_entry,
                              cpf_entry, idCliente_entry):
        # Obtenha os dados editados dos campos de entrada
        novo_nome = nome_entry.get()
        novo_email = email_entry.get()
        nova_data_nascimento = nasc_entry.get()
        novo_telefone = telefone_entry.get()
        novo_endereco = endereco_entry.get()
        novo_cep = cep_entry.get()
        novo_cpf = cpf_entry.get()
        id = idCliente_entry.get()

        # Crie um dicionário com os dados editados
        dados_editados = {
            "id": id,
            "nome": novo_nome,
            "email": novo_email,
            "dataNascimento": nova_data_nascimento,
            "telefone": novo_telefone,
            "endereco": novo_endereco,
            "cep": novo_cep,
            "cpf": novo_cpf,
        }

        # Converta o dicionário em uma representação JSON
        dados_json = json.dumps(dados_editados)
        print(dados_json)

        # Faça uma solicitação PUT para a rota apropriada com os dados JSON
        url = f"http://localhost:8080/clientes/atualizar"
        headers = {'Content-type': 'application/json'}
        response = requests.put(url, data=dados_json, headers=headers)

        if response.status_code == 200:
            # Atualize a tabela de clientes ou realize qualquer ação necessária
            print("Cliente editado com sucesso!")
            editar_cliente_dialog.destroy()  # Feche a janela de edição após a conclusão
        else:
            print("Erro ao editar cliente")

    root = tk.Tk()
    root.title("Lista de Clientes")

    resultado_label = tk.Label(root, text="")
    resultado_label.pack()

    listar_button = tk.Button(root, text="Listar Clientes", command=listar_clientes)
    listar_button.pack()

    atualizar_button = tk.Button(root, text="Atualizar Cliente", command=atualizar_cliente)
    atualizar_button.pack()

    clientes_treeview = ttk.Treeview(root, columns=("nome", "nasc", "telefone", "endereco", "cep", "cpf", "idCliente"))
    clientes_treeview.heading('#1', text='Nome')
    clientes_treeview.heading('#2', text='Data Nascimento')
    clientes_treeview.heading('#3', text='Telefone')
    clientes_treeview.heading('#4', text='Endereço')
    clientes_treeview.heading('#5', text='CEP')
    clientes_treeview.heading('#6', text='cpf')
    clientes_treeview.heading('#7', text='Id Cliente')
    clientes_treeview.pack()

    clientes_treeview.bind("<ButtonRelease-1>", mostrar_detalhes)

    root.mainloop()


def apagar_cliente():
    def apagar_cliente():
        id_cliente = id_entry.get()

        # URL da sua API Spring para apagar um cliente (concatenando o ID fornecido)
        url_da_api = f"http://localhost:8080/clientes/apagar/{id_cliente}"  # Substitua pela URL real da sua API

        try:
            # Enviar uma solicitação DELETE para a API Spring
            response = requests.delete(url_da_api)

            if response.status_code == 200:
                resultado_label.config(text=f"Cliente com ID {id_cliente} excluído com sucesso")
            else:
                resultado_label.config(text=f"Cliente com ID {id_cliente} excluído com sucesso")
        except Exception as e:
            resultado_label.config(text=f"Erro ao apagar cliente: {str(e)}")

    root = tk.Tk()
    root.title("Apagar Cliente")

    resultado_label = tk.Label(root, text="")
    resultado_label.pack()

    id_label = tk.Label(root, text="ID do Cliente:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack()

    apagar_button = tk.Button(root, text="Apagar Cliente", command=apagar_cliente)
    apagar_button.pack()

    root.mainloop()


def cadastrar_vigilante():
    def cadastrar():
        nome = nome_entry.get()
        status = status_entry.get()

        dados = {
            "nome": nome,
            "status": status
        }

        url_da_api = "http://localhost:8080/cadastrar/vigilante"  # Substitua pela URL real da sua API

        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(url_da_api, data=json.dumps(dados), headers=headers)

            if response.status_code == 200:
                resultado_label.config(text="Vigilante cadastrado com sucesso.")
            else:
                resultado_label.config(text=f"Falha ao cadastrar vigilante. Status: {response.status_code}")
        except Exception as e:
            resultado_label.config(text=f"Erro ao cadastrar vigilante: {str(e)}")

    root = tk.Tk()
    root.title("Cadastro de Vigilante")

    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10)

    nome_label = ttk.Label(frame, text="Nome:")
    nome_label.grid(row=0, column=0)
    nome_entry = ttk.Entry(frame)
    nome_entry.grid(row=0, column=1)

    status_label = ttk.Label(frame, text="Status:")
    status_label.grid(row=1, column=0)
    status_entry = ttk.Entry(frame)
    status_entry.grid(row=1, column=1)

    cadastrar_button = ttk.Button(frame, text="Cadastrar", command=cadastrar)
    cadastrar_button.grid(row=2, columnspan=2)

    resultado_label = ttk.Label(frame, text="")
    resultado_label.grid(row=3, columnspan=2)

    root.mainloop()


def listar_vigilantes():
    def listar_vigilantes():
        for row in vigilantes_treeview.get_children():
            vigilantes_treeview.delete(row)

        response = requests.get("http://localhost:8080/vigilantes")

        if response.status_code == 200:
            dados_json = response.json()

            for vigilante in dados_json:
                nome = vigilante.get("nome", "Nome não encontrado")
                status = vigilante.get("status", "Status não encontrado")
                idVigilante = vigilante.get("idVigilante", "ID Vigilante não encontrado")

                vigilantes_treeview.insert('', 'end',
                                           values=(nome, status, idVigilante,))
        else:
            resultado_label.config(text="Erro ao buscar vigilantes da API")

    def mostrar_detalhes(event):
        item = vigilantes_treeview.selection()
        if item:
            item = item[0]
            vigilante = vigilantes_treeview.item(item, 'values')
            resultado_label.config(
                text=f"Detalhes do Vigilante:\nNome: {vigilante[0]}, Status: {vigilante[1]}, ID Vigilante: {vigilante[2]}")
        else:
            resultado_label.config(text="Selecione um vigilante")

    def atualizar_vigilante():
        item = vigilantes_treeview.selection()
        if item:
            item = item[0]
            vigilante = vigilantes_treeview.item(item, 'values')
            editar_vigilante_window(vigilante)
        else:
            resultado_label.config(text="Selecione um vigilante")

    def editar_vigilante_window(vigilante):
        global editar_vigilante_dialog
        editar_vigilante_dialog = tk.Toplevel(root)
        editar_vigilante_dialog.title("Editar Vigilante")

        nome_label = tk.Label(editar_vigilante_dialog, text="Nome:")
        nome_label.pack()
        nome_entry = tk.Entry(editar_vigilante_dialog)
        nome_entry.insert(0, vigilante[0])
        nome_entry.pack()

        status_label = tk.Label(editar_vigilante_dialog, text="Status:")
        status_label.pack()
        status_entry = tk.Entry(editar_vigilante_dialog)
        status_entry.insert(0, vigilante[1])
        status_entry.pack()

        idVigilante_label = tk.Label(editar_vigilante_dialog, text="ID Vigilante:")
        idVigilante_label.pack()
        idVigilante_entry = tk.Entry(editar_vigilante_dialog)
        idVigilante_entry.insert(0, vigilante[2])
        idVigilante_entry.pack()

        salvar_button = tk.Button(editar_vigilante_dialog, text="Salvar",
                                  command=lambda: salvar_edicao_vigilante(vigilante, nome_entry, status_entry,
                                                                          idVigilante_entry))
        salvar_button.pack()

    def salvar_edicao_vigilante(vigilante, nome_entry, status_entry, idVigilante_entry):
        novo_nome = nome_entry.get()
        novo_status = status_entry.get()
        id = idVigilante_entry.get()

        dados_editados = {
            "idVigilante": id,
            "nome": novo_nome,
            "status": novo_status
        }

        dados_json = json.dumps(dados_editados)

        url = f"http://localhost:8080/vigilantes/atualizar"
        headers = {'Content-type': 'application/json'}
        response = requests.put(url, data=dados_json, headers=headers)

        if response.status_code == 200:
            print("Vigilante editado com sucesso!")
            editar_vigilante_dialog.destroy()
        else:
            print("Erro ao editar vigilante")

    root = tk.Tk()
    root.title("Lista de Vigilantes")

    resultado_label = tk.Label(root, text="")
    resultado_label.pack()

    listar_button = tk.Button(root, text="Listar Vigilantes", command=listar_vigilantes)
    listar_button.pack()

    atualizar_button = tk.Button(root, text="Atualizar Vigilante", command=atualizar_vigilante)
    atualizar_button.pack()

    vigilantes_treeview = ttk.Treeview(root, columns=("nome", "status", "idVigilante"))
    vigilantes_treeview.heading('#1', text='Nome')
    vigilantes_treeview.heading('#2', text='Status')
    vigilantes_treeview.heading('#3', text='ID Vigilante')
    vigilantes_treeview.pack()

    vigilantes_treeview.bind("<ButtonRelease-1>", mostrar_detalhes)

    root.mainloop()


def apagar_vigilante():
    def apagar_vigilante():
        id_vigilante = id_entry.get()

        url_da_api = f"http://localhost:8080/vigilantes/{id_vigilante}"

        try:
            response = requests.delete(url_da_api)

            if response.status_code == 200:
                resultado_label.config(text=f"Vigilante com ID {id_vigilante} excluído com sucesso")
            else:
                resultado_label.config(text=f"Vigilante com ID {id_vigilante} excluído com sucesso")
        except Exception as e:
            resultado_label.config(text=f"Erro ao apagar vigilante: {str(e)}")

    root = tk.Tk()
    root.title("Apagar Vigilante")

    resultado_label = tk.Label(root, text="")
    resultado_label.pack()

    id_label = tk.Label(root, text="ID do Vigilante:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack()

    apagar_button = tk.Button(root, text="Apagar Vigilante", command=apagar_vigilante)
    apagar_button.pack()

    root.mainloop()


def cadastrar_alarme():
    def cadastrar():
        locala = locala_entry.get()
        diadoalarme = diadoalarme_entry.get()
        ativo = ativo_entry.get()

        dados = {
            "id": 0,
            "locala": locala,
            "diadoalarme": diadoalarme,
            "Ativo": 0
        }

        url_da_api = "http://localhost:8080/cadastrar/alarme"
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(url_da_api, json=dados, headers=headers)

            if response.status_code == 200:
                resultado_label.config(text="Alarme cadastrado com sucesso.")
            else:
                resultado_label.config(text=f"Falha ao cadastrar alarme. Status: {response.status_code}")
        except Exception as e:
            resultado_label.config(text=f"Erro ao cadastrar alarme: {str(e)}")

    root = tk.Tk()
    root.title("Cadastro de Alarme")

    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10)

    locala_label = ttk.Label(frame, text="Locala:")
    locala_label.grid(row=0, column=0)
    locala_entry = ttk.Entry(frame)
    locala_entry.grid(row=0, column=1)

    diadoalarme_label = ttk.Label(frame, text="Data do Alarme (YYYY-MM-DD):")
    diadoalarme_label.grid(row=1, column=0)
    diadoalarme_entry = ttk.Entry(frame)
    diadoalarme_entry.grid(row=1, column=1)

    ativo_label = ttk.Label(frame, text="Ativo:")
    ativo_label.grid(row=2, column=0)
    ativo_entry = ttk.Entry(frame)
    ativo_entry.grid(row=2, column=1)

    cadastrar_button = ttk.Button(frame, text="Cadastrar", command=cadastrar)
    cadastrar_button.grid(row=3, columnspan=2)

    resultado_label = ttk.Label(frame, text="")
    resultado_label.grid(row=4, columnspan=2)

    root.mainloop()


def listar_alarmes():
    def listar():
        for row in alarmes_treeview.get_children():
            alarmes_treeview.delete(row)

        response = requests.get("http://localhost:8080/alarmes")

        if response.status_code == 200:
            dados_json = response.json()

            for alarme in dados_json:
                locala = alarme.get("locala", "Local não encontrado")
                data_alarme = alarme.get("diadoalarme", "Data do Alarme não encontrado")
                ativo = alarme.get("ativo", "Ativo não encontrado")
                id_alarme = alarme.get("id", "ID do Alarme não encontrado")


                alarmes_treeview.insert('', 'end',
                                        values=(locala, data_alarme, ativo, id_alarme))
        else:
            resultado_label.config(text="Erro ao buscar alarmes da API")

    def mostrar_detalhes(event):
        item = alarmes_treeview.selection()
        if item:
            item = item[0]
            alarme = alarmes_treeview.item(item, 'values')
            resultado_label.config(
                text=f"Detalhes do Alarme:\nLocal: {alarme[0]}, Data do Alarme: {alarme[1]}, Ativo: {alarme[2]}, ID: {alarme[3]}")
        else:
            resultado_label.config(text="Selecione um alarme")

    def atualizar_alarme():
        item = alarmes_treeview.selection()
        if item:
            item = item[0]
            alarme = alarmes_treeview.item(item, 'values')
            editar_alarme_window(alarme)
        else:
            resultado_label.config(text="Selecione um alarme")

    def editar_alarme_window(alarme):
        global editar_alarme_dialog
        editar_alarme_dialog = tk.Toplevel(root)
        editar_alarme_dialog.title("Editar Alarme")

        local_label = tk.Label(editar_alarme_dialog, text="Local:")
        local_label.pack()
        local_entry = tk.Entry(editar_alarme_dialog)
        local_entry.insert(0, alarme[0])
        local_entry.pack()

        data_alarme_label = tk.Label(editar_alarme_dialog, text="Data do Alarme:")
        data_alarme_label.pack()
        data_alarme_entry = tk.Entry(editar_alarme_dialog)
        data_alarme_entry.insert(0, alarme[1])
        data_alarme_entry.pack()

        ativo_label = tk.Label(editar_alarme_dialog, text="Ativo:")
        ativo_label.pack()
        ativo_entry = tk.Entry(editar_alarme_dialog)
        ativo_entry.insert(0, alarme[2])
        ativo_entry.pack()

        id_alarme_label = tk.Label(editar_alarme_dialog, text="ID Alarme:")
        id_alarme_label.pack()
        id_alarme_entry = tk.Entry(editar_alarme_dialog)
        id_alarme_entry.insert(0, alarme[3])
        id_alarme_entry.pack()

        salvar_button = tk.Button(editar_alarme_dialog, text="Salvar",
                                  command=lambda: salvar_edicao_alarme(alarme, local_entry, data_alarme_entry,
                                                                       ativo_entry, id_alarme_entry))
        salvar_button.pack()

    def salvar_edicao_alarme(alarme, local_entry, data_alarme_entry, ativo_entry, id_alarme_entry):
        novo_local = local_entry.get()
        nova_data_alarme = data_alarme_entry.get()
        novo_ativo = ativo_entry.get()
        id = id_alarme_entry.get()

        dados_editados = {
            "id": id,
            "locala": novo_local,
            "diadoalarme": nova_data_alarme,
            "ativo": novo_ativo,
        }

        dados_json = json.dumps(dados_editados)

        print(dados_editados)

        url = f"http://localhost:8080/alarmes/atualizar"
        headers = {'Content-type': 'application/json'}
        response = requests.put(url, data=dados_json, headers=headers)

        if response.status_code == 200:
            print("Alarme editado com sucesso!")
            editar_alarme_dialog.destroy()
        else:
            print("Erro ao editar alarme")

    root = tk.Tk()
    root.title("Lista de Alarmes")

    resultado_label = tk.Label(root, text="")
    resultado_label.pack()

    listar_button = tk.Button(root, text="Listar Alarmes", command=listar)
    listar_button.pack()

    atualizar_button = tk.Button(root, text="Atualizar Alarme", command=atualizar_alarme)
    atualizar_button.pack()

    alarmes_treeview = ttk.Treeview(root, columns=("local", "data_alarme", "ativo", "id_alarme"))
    alarmes_treeview.heading('#1', text='Local')
    alarmes_treeview.heading('#2', text='Data do Alarme')
    alarmes_treeview.heading('#3', text='Ativo')
    alarmes_treeview.heading('#4', text='ID Alarme')
    alarmes_treeview.pack()

    alarmes_treeview.bind("<ButtonRelease-1>", mostrar_detalhes)

    root.mainloop()


def apagar_alarme():
    def apagar_alarme():
        id_alarme = id_entry.get()

        url_da_api = f"http://localhost:8080/alarmes/{id_alarme}"

        try:
            response = requests.delete(url_da_api)

            if response.status_code == 200:
                resultado_label.config(text=f"Alarme com ID {id_alarme} excluído com sucesso")
            else:
                resultado_label.config(text=f"Erro ao apagar alarme com ID {id_alarme}. Status: {response.status_code}")
        except Exception as e:
            resultado_label.config(text=f"Alarme com ID {id_alarme} excluído com sucesso")

    root = tk.Tk()
    root.title("Apagar Alarme")

    resultado_label = tk.Label(root, text="")
    resultado_label.pack()

    id_label = tk.Label(root, text="ID do Alarme:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack()

    apagar_button = tk.Button(root, text="Apagar Alarme", command=apagar_alarme)
    apagar_button.pack()

    root.mainloop()


def acionar_alarme():
    def listar_alarmes_disponiveis():
        try:
            response = requests.get("http://localhost:8080/alarmes")
            response.raise_for_status()
            alarmes = response.json()
            alarmes_disponiveis.delete(0, tk.END)
            for alarme in alarmes:
                alarmes_disponiveis.insert(tk.END, f"ID: {alarme['id']}, local: {alarme['locala']}")
        except requests.exceptions.RequestException as e:
            resultado_label.config(text=f"Erro na solicitação: {e}")
        except Exception as ex:
            resultado_label.config(text=f"Erro desconhecido: {ex}")

    def acionar():
        id_alarme = id_alarme_entry.get()
        novo_status = novo_status_entry.get()

        data = {"novoStatus": novo_status}

        try:
            url = f"http://localhost:8080/alarmes/{id_alarme}/modificar-status"
            response = requests.patch(url, json=data)
            response.raise_for_status()
            resultado_label.config(text=f"Status do Alarme com ID {id_alarme} modificado com sucesso!")
        except requests.exceptions.RequestException as e:
            resultado_label.config(text=f"Erro na solicitação: {e}")
        except Exception as ex:
            resultado_label.config(text=f"Erro desconhecido: {ex}")

    root = tk.Tk()
    root.title("Acionar Alarme")

    listar_button = ttk.Button(root, text="Listar Alarmes Disponíveis", command=listar_alarmes_disponiveis)
    listar_button.pack()

    alarmes_disponiveis = tk.Listbox(root, width=40)
    alarmes_disponiveis.pack()

    id_alarme_label = ttk.Label(root, text="ID do Alarme:")
    id_alarme_label.pack()

    id_alarme_entry = ttk.Entry(root)
    id_alarme_entry.pack()

    novo_status_label = ttk.Label(root, text="Status do alarme:")
    novo_status_label.pack()

    novo_status_entry = ttk.Entry(root)
    novo_status_entry.pack()

    acionar_button = ttk.Button(root, text="Acionar Alarme", command=acionar)
    acionar_button.pack()

    resultado_label = ttk.Label(root, text="")
    resultado_label.pack()

    root.mainloop()


def acionar_vigilante():
    def listar_alarmes_disponiveis():
        try:
            url = "http://localhost:8080/alarmes"
            response = requests.get(url)
            response.raise_for_status()
            alarmes = response.json()

            alarmes_disponiveis.delete(0, tk.END)
            for alarme in alarmes:
                alarmes_disponiveis.insert(tk.END,
                                           f"ID: {alarme['id']}, Status: {alarme['status']}")
        except requests.exceptions.RequestException as e:
            print(f"Erro na solicitação: {e}")

    def listar_vigilantes_disponiveis():
        try:
            url = "http://localhost:8080/vigilantes"
            response = requests.get(url)
            response.raise_for_status()
            vigilantes = response.json()

            vigilantes_disponiveis.delete(0, tk.END)
            for vigilante in vigilantes:
                vigilantes_disponiveis.insert(tk.END,
                                              f"ID: {vigilante['idVigilante']}, Nome: {vigilante['nome']}, Status: {vigilante['status']}")
        except requests.exceptions.RequestException as e:
            print(f"Erro na solicitação: {e}")

    def acionar():
        id_vigilante = id_vigilante_entry.get()
        id_alarme = id_alarme_entry.get()

        # Crie um dicionário com os IDs do vigilante e do alarme
        data = {"idvigilante": id_vigilante, "idalarme": id_alarme}
        json_data = json.dumps(data)
        print(json_data)

        url = f"http://localhost:8080/vigilante/{id_vigilante}/acionar/{id_alarme}"

        try:
            response = requests.patch(url, data=json_data, headers={"Content-Type": "application/json"})
            response.raise_for_status()
            resultado_label.config(text=f"Vigilante com ID {id_vigilante} acionado com sucesso para o Alarme!")
        except requests.exceptions.RequestException as e:
            resultado_label.config(text=f"Erro na solicitação: {e}")

    root = tk.Tk()
    root.title("Acionar Vigilante")

    listar_alarmes_button = tk.Button(root, text="Listar Alarmes Disponíveis", command=listar_alarmes_disponiveis)
    listar_alarmes_button.pack()

    alarmes_disponiveis = tk.Listbox(root, width=40)
    alarmes_disponiveis.pack()

    listar_vigilantes_button = tk.Button(root, text="Listar Vigilantes Disponíveis",
                                         command=listar_vigilantes_disponiveis)
    listar_vigilantes_button.pack()

    vigilantes_disponiveis = tk.Listbox(root, width=40)
    vigilantes_disponiveis.pack()

    id_vigilante_label = ttk.Label(root, text="ID do Vigilante:")
    id_vigilante_label.pack()

    id_vigilante_entry = ttk.Entry(root)
    id_vigilante_entry.pack()

    id_alarme_label = ttk.Label(root, text="ID do Alarme:")
    id_alarme_label.pack()

    id_alarme_entry = ttk.Entry(root)
    id_alarme_entry.pack()

    acionar_button = ttk.Button(root, text="Acionar Vigilante", command=acionar)
    acionar_button.pack()

    resultado_label = ttk.Label(root, text="")
    resultado_label.pack()

    root.mainloop()


def descrever_ocorrencias():
    def listar_registros(tree, resultado_label_ocorrencias):
        url = "http://localhost:8080/listarAndamento"  # Substitua pela URL correta da sua API Spring
        try:
            response = requests.get(url)
            response.raise_for_status()
            registros = response.json()

            # Limpar a tabela anterior
            for i in tree.get_children():
                tree.delete(i)

            # Preencher a tabela com os novos registros
            for registro in registros:
                tree.insert('', 'end', values=tuple(registro.values()))
        except requests.exceptions.RequestException as e:
            resultado_label_ocorrencias.config(text=f"Erro na solicitação: {e}")

    def criar_interface():
        root = tk.Tk()
        root.title("Listar Registros")

        # Configurar a tabela para exibir registros
        columns = ("ID do Alarme", "ID do Vigilante", "Descrição")
        tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        tree.pack()

        resultado_label_ocorrencias = ttk.Label(root, text="")
        resultado_label_ocorrencias.pack()

        listar_button = ttk.Button(root, text="Listar Registros",
                                   command=lambda: listar_registros(tree, resultado_label_ocorrencias))
        listar_button.pack()

        root.mainloop()

    def descrever_ocorrencias():
        root_ocorrencias = tk.Toplevel(root)
        root_ocorrencias.title("Descrever Ocorrências")

        descricao_ocorrencia_label = ttk.Label(root_ocorrencias, text="Descrição da Ocorrência:")
        descricao_ocorrencia_label.pack()

        ocorrencia_entry = ttk.Entry(root_ocorrencias)
        ocorrencia_entry.pack()

        id_alarme_label = ttk.Label(root_ocorrencias, text="ID do Alarme:")
        id_alarme_label.pack()

        id_alarme_entry = ttk.Entry(root_ocorrencias)
        id_alarme_entry.pack()

        id_vigilante_label = ttk.Label(root_ocorrencias, text="ID do Vigilante:")
        id_vigilante_label.pack()

        id_vigilante_entry = ttk.Entry(root_ocorrencias)
        id_vigilante_entry.pack()

        resultado_label_ocorrencias = ttk.Label(root_ocorrencias, text="")
        resultado_label_ocorrencias.pack()

        def salvar_ocorrencia():
            descricao_ocorrencia = ocorrencia_entry.get()
            id_alarme = id_alarme_entry.get()
            id_vigilante = id_vigilante_entry.get()

            data = {
                "motivo_acionamento": descricao_ocorrencia,
                "id_alarme": id_alarme,
                "id_vigilante": id_vigilante
            }

            url = f"http://localhost:8080/vigilante/{id_vigilante}/terminar/{id_alarme}"

            try:
                response = requests.patch(url, json=data, headers={"Content-Type": "application/json"})
                response.raise_for_status()
                resultado_label_ocorrencias.config(text=f"Ocorrência salva com sucesso: {descricao_ocorrencia}")
            except requests.exceptions.RequestException as e:
                resultado_label_ocorrencias.config(text=f"Erro na solicitação: {e}")

        salvar_ocorrencia_button = ttk.Button(root_ocorrencias, text="Salvar Ocorrência", command=salvar_ocorrencia)
        salvar_ocorrencia_button.pack()

        listar_registros_button = ttk.Button(root_ocorrencias, text="Listar Registros",
                                             command=lambda: listar_registros(tree, resultado_label_ocorrencias))
        listar_registros_button.pack()

        # Configurar a tabela para exibir registros
        columns = ("Descrição", "ID do Alarme", "ID do Vigilante")
        tree = ttk.Treeview(root_ocorrencias, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        tree.pack()

    descrever_ocorrencias()
    root.mainloop()


def registro_listar():
    def registro_listar():
        def listar_registros():
            # Substitua a URL abaixo pela URL real da sua API Spring
            api_url = 'http://localhost:8080/listarTodos'

            try:
                # Faça uma solicitação à API para obter os registros
                response = requests.get(api_url)

                # Verifique se a solicitação foi bem-sucedida (código de status 200)
                if response.status_code == 200:
                    # Os dados da resposta da API estão em formato JSON
                    registros = response.json()

                    # Crie uma nova janela para exibir os registros
                    nova_janela = tk.Toplevel(root)
                    nova_janela.title('Registros da API Spring')

                    # Crie a tabela usando o widget Treeview
                    tabela = ttk.Treeview(nova_janela, columns=list(registros[0].keys()), show='headings')

                    # Configurar os cabeçalhos da tabela
                    for coluna in registros[0].keys():
                        tabela.heading(coluna, text=coluna)
                        tabela.column(coluna, width=100)  # Ajuste a largura conforme necessário

                    # Preencher a tabela com os dados
                    for registro in registros:
                        tabela.insert('', 'end', values=list(registro.values()))

                    tabela.pack(padx=10, pady=10)
                else:
                    print('Erro ao acessar a API:', response.status_code)
            except requests.RequestException as e:
                print('Erro ao fazer solicitação à API:', str(e))

        # Crie a janela principal
        root = tk.Tk()
        root.title('Interface para API Spring')

        # Crie um botão para chamar a função de listar registros
        botao_listar = tk.Button(root, text='Listar Registros', command=listar_registros)
        botao_listar.pack(pady=20)

        # Inicie o loop principal da interface gráfica
        root.mainloop()

    # Chame a função para exibir a janela
    registro_listar()

    # Chame a função para exibir a janela
    registro_listar()


def criar_aba(titulo, comando):
    aba = ttk.Frame(notebook)
    notebook.add(aba, text=titulo)

    for i, (acao, texto) in enumerate(comando):
        ttk.Button(aba, text=texto, command=acao, style='EstiloBotoes.TButton').grid(row=i, column=0, pady=10, padx=10)


def mostrar_resultado(mensagem):
    resultado_label.config(text=mensagem)


root = tk.Tk()
root.title("Sistemas de Alarmes")

titulo_label = ttk.Label(root, text="Selecione a opção desejada:", font=("Helvetica", 16))
titulo_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

style = ttk.Style()
style.configure('EstiloBotoes.TButton', foreground='black', background='cyan', font=('Helvetica', 12), width=15,
                height=3)

notebook = ttk.Notebook(root)
notebook.grid(row=1, column=1, rowspan=4, padx=5, sticky='nsew')

root.grid_columnconfigure((0, 1), weight=1)
root.grid_rowconfigure((1, 2, 3, 4), weight=1)

criar_aba("Clientes", [(cadastrar_cliente, "Cadastrar"), (listar_clientes, "Listar"), (apagar_cliente, "Apagar")])
criar_aba("Vigilantes",
          [(cadastrar_vigilante, "Cadastrar"), (listar_vigilantes, "Listar"), (apagar_vigilante, "Apagar"),
           (acionar_vigilante, "Acionar Vigilante")])
criar_aba("Alarmes", [(cadastrar_alarme, "Cadastrar"), (listar_alarmes, "Listar"), (apagar_alarme, "Apagar")])
criar_aba("Acionamentos ", [(descrever_ocorrencias, "Descrever Ocorrência"), (acionar_alarme, "Acionar Alarme"),
                            (registro_listar, "Listar Registros")])

resultado_label = ttk.Label(root, text="", font=("Helvetica", 16))
resultado_label.grid(row=4, column=0, pady=5)
root.mainloop()
