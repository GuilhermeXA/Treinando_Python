import PySimpleGUI as sg
import pyodbc

# Conecte-se ao banco de dados SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=seu_servidor;'
                      'Database=LojaDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# Layout da interface
layout = [
    [sg.Text('ID:'), sg.InputText(key='id')],
    [sg.Text('Nome:'), sg.InputText(key='nome')],
    [sg.Text('Marca:'), sg.InputText(key='marca')],
    [sg.Text('Preço:'), sg.InputText(key='preco')],
    [sg.Text('Quantidade:'), sg.InputText(key='quantidade')],
    [sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir')],
    [sg.Table(values=[], headings=['ID', 'Nome', 'Marca', 'Preço', 'Quantidade'], auto_size_columns=False, justification='right', num_rows=10, key='table')]
]

window = sg.Window('Loja', layout, finalize=True)

# Função para limpar campos de entrada
def limpar_campos():
    window['id'].update('')
    window['nome'].update('')
    window['marca'].update('')
    window['preco'].update('')
    window['quantidade'].update('')

# Função para atualizar a tabela
def atualizar_tabela():
    cursor.execute('SELECT * FROM Produtos')
    produtos = cursor.fetchall()
    window['table'].update(values=produtos)

# Loop principal da interface
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Cadastrar':
        nome = values['nome']
        marca = values['marca']
        preco = values['preco']
        quantidade = values['quantidade']
        cursor.execute('INSERT INTO Produtos (Nome, Marca, Preco, Quantidade) VALUES (?, ?, ?, ?)', (nome, marca, preco, quantidade))
        conn.commit()
        limpar_campos()
        atualizar_tabela()
    elif event == 'Editar':
        id_produto = values['id']
        nome = values['nome']
        marca = values['marca']
        preco = values['preco']
        quantidade = values['quantidade']
        cursor.execute('UPDATE Produtos SET Nome = ?, Marca = ?, Preco = ?, Quantidade = ? WHERE ID = ?', (nome, marca, preco, quantidade, id_produto))
        conn.commit()
        limpar_campos()
        atualizar_tabela()
    elif event == 'Excluir':
        id_produto = values['id']
        cursor.execute('DELETE FROM Produtos WHERE ID = ?', (id_produto,))
        conn.commit()
        limpar_campos()
        atualizar_tabela()

window.close()
conn.close()
