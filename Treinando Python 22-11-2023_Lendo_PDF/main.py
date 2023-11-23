import PyPDF2

def ler_pdf(nome_arquivo):
    with open(nome_arquivo, 'rb') as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)
        numero_paginas = len(leitor.pages)

        texto_completo = ''
        for pagina_numero in range(numero_paginas):
            pagina = leitor.pages[pagina_numero]
            texto_completo += pagina.extract_text()

    return texto_completo

# Substitua 'seu_arquivo.pdf' pelo nome do seu arquivo PDF
nome_arquivo = 'seu_arquivo.pdf'
conteudo = ler_pdf(nome_arquivo)

print(conteudo)
