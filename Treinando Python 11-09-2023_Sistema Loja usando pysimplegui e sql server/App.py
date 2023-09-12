import PySimpleGUI as sg
import sqlite3

# Função para criar a tabela de produtos no banco de dados
def criar_tabela():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            marca TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir um novo produto no banco de dados
def cadastrar_produto(nome, marca, preco, quantidade):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, marca, preco, quantidade) VALUES (?, ?, ?, ?)',
                   (nome, marca, preco, quantidade))
    conn.commit()
    conn.close()

# Função para listar todos os produtos cadastrados
def listar_produtos():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

# Função para atualizar um produto no banco de dados
def atualizar_produto(id, nome, marca, preco, quantidade):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE produtos SET nome=?, marca=?, preco=?, quantidade=? WHERE id=?',
                   (nome, marca, preco, quantidade, id))
    conn.commit()
    conn.close()

# Função para excluir um produto do banco de dados
def excluir_produto(id):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id=?', (id,))
    conn.commit()
    conn.close()

# Layout da janela
layout = [
    [sg.Text('Nome:'), sg.InputText(key='nome')],
    [sg.Text('Marca:'), sg.InputText(key='marca')],
    [sg.Text('Preço:'), sg.InputText(key='preco')],
    [sg.Text('Quantidade:'), sg.InputText(key='quantidade')],
    [sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir')],
    [sg.Listbox(values=[], size=(50, 10), key='produtos')],
]

# Janela principal
janela = sg.Window('Loja').Layout(layout)

# Criar a tabela no banco de dados
criar_tabela()

while True:
    evento, valores = janela.Read()

    if evento == sg.WINDOW_CLOSED:
        break

    if evento == 'Cadastrar':
        nome = valores['nome']
        marca = valores['marca']
        preco = valores['preco']
        quantidade = valores['quantidade']

        if nome and marca and preco and quantidade:
            cadastrar_produto(nome, marca, float(preco), int(quantidade))
            sg.popup('Produto cadastrado com sucesso!')
        else:
            sg.popup('Preencha todos os campos.')

    if evento == 'Editar':
        produtos = listar_produtos()
        if not produtos:
            sg.popup('Nenhum produto cadastrado.')
        else:
            selected_product = valores['produtos']
            if selected_product:
                selected_product_id = selected_product[0].split('-')[0].strip()
                nome = valores['nome']
                marca = valores['marca']
                preco = valores['preco']
                quantidade = valores['quantidade']

                if nome and marca and preco and quantidade:
                    atualizar_produto(int(selected_product_id), nome, marca, float(preco), int(quantidade))
                    sg.popup('Produto atualizado com sucesso!')
                else:
                    sg.popup('Preencha todos os campos.')

    if evento == 'Excluir':
        produtos = listar_produtos()
        if not produtos:
            sg.popup('Nenhum produto cadastrado.')
        else:
            selected_product = valores['produtos']
            if selected_product:
                selected_product_id = selected_product[0].split('-')[0].strip()
                excluir_produto(int(selected_product_id))
                sg.popup('Produto excluído com sucesso!')

    # Atualizar a lista de produtos na interface
    produtos = listar_produtos()
    janela['produtos'].Update([f'{produto[0]} - {produto[1]} ({produto[2]} - {produto[3]})' for produto in produtos])

# Fechar a janela
janela.Close()
