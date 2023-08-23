import PySimpleGUI as sg

# Definindo a interface gráfica
layout = [
    [sg.Text('Conversor de Moedas')],
    [sg.Text('Nome Moeda:'), sg.InputText(key='nome_moeda')],
    [sg.Text('Valor Moeda:'), sg.InputText(key='valor_moeda')],
    [sg.Text('Quantidade:'), sg.InputText(key='quantidade')],
    [sg.Text('Resultado:'), sg.InputText(key='resultado', disabled=True)],
    [sg.Button('Converter')]
]

window = sg.Window('Conversor de Moedas', layout)

# Taxas de conversão
taxas = {'dolar': 5.23, 'euro': 6.17, 'libra': 7.12}

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Converter':
        nome_moeda = values['nome_moeda'].lower()
        valor_moeda = float(values['valor_moeda'])
        quantidade = float(values['quantidade'])

        if nome_moeda in taxas:
            taxa = taxas[nome_moeda]
            resultado = valor_moeda * quantidade * taxa
            window['resultado'].update(resultado)
        else:
            window['resultado'].update('Moeda não suportada')

window.close()
