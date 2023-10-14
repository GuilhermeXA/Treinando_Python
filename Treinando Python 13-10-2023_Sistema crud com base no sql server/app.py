import tkinter as tk
from tkinter import messagebox
import pyodbc

class CrudApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD App")

        self.id_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.endereco_var = tk.StringVar()
        self.telefone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        # Frames
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=20)

        frame_listbox = tk.Frame(self.root)
        frame_listbox.pack()

        # Labels e Entry para o formulário
        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.id_var, state="readonly").grid(row=0, column=1)

        tk.Label(frame_form, text="Nome:").grid(row=1, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.nome_var).grid(row=1, column=1)

        tk.Label(frame_form, text="Endereço:").grid(row=2, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.endereco_var).grid(row=2, column=1)

        tk.Label(frame_form, text="Telefone:").grid(row=3, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.telefone_var).grid(row=3, column=1)

        tk.Label(frame_form, text="Email:").grid(row=4, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.email_var).grid(row=4, column=1)

        # Botões
        tk.Button(frame_form, text="Novo", command=self.novo_registro).grid(row=5, column=0, pady=10)
        tk.Button(frame_form, text="Salvar", command=self.salvar_registro).grid(row=5, column=1, pady=10)
        tk.Button(frame_form, text="Excluir", command=self.excluir_registro).grid(row=5, column=2, pady=10)

        # Listbox para mostrar os registros
        self.listbox = tk.Listbox(frame_listbox, width=50, height=10)
        self.listbox.pack(pady=20)
        self.listbox.bind("<<ListboxSelect>>", self.preencher_campos)

        # Conectar ao SQL Server
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-5M9EP0AR\SQLEXPRESS;'
                                   'Database=PythonSQL;'
                                   'Trusted_Connection=yes;')

        # Carregar dados na Listbox
        self.carregar_dados()

    def carregar_dados(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM TblClientes")
        rows = cursor.fetchall()

        self.listbox.delete(0, tk.END)

        for row in rows:
            self.listbox.insert(tk.END, f"{row.Nome} - {row.Telefone}")

    def preencher_campos(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_data = self.listbox.get(selected_index[0])
            # Você precisará implementar a lógica para obter o ID do registro selecionado
            # e buscar os detalhes desse registro no banco de dados.

            # Exemplo:
            # id_selecionado = obter_id_do_registro(selected_data)
            # dados_registro = obter_dados_do_banco(id_selecionado)
            # self.id_var.set(dados_registro['id'])
            # self.nome_var.set(dados_registro['nome'])
            # ... e assim por diante.

    def novo_registro(self):
        self.limpar_campos()

    def salvar_registro(self):
        # Lógica para validar os campos (por exemplo, verificar se todos estão preenchidos)
        if not self.campos_validos():
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        # Lógica para inserir ou atualizar no banco de dados
        # ...

        # Após salvar, carregue os dados novamente na Listbox
        self.carregar_dados()

        messagebox.showinfo("Sucesso", "Registro salvo com sucesso.")

    def excluir_registro(self):
        # Verificar se o usuário realmente deseja excluir
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir este registro?")
        if resposta == tk.YES:
            # Lógica para excluir no banco de dados
            # ...

            # Após excluir, carregue os dados novamente na Listbox
            self.carregar_dados()

            messagebox.showinfo("Sucesso", "Registro excluído com sucesso.")

    def campos_validos(self):
        # Lógica para validar campos (por exemplo, verificar se estão preenchidos)
        return bool(self.nome_var.get() and self.endereco_var.get() and
                    self.telefone_var.get() and self.email_var.get())

    def limpar_campos(self):
        self.id_var.set("")
        self.nome_var.set("")
        self.endereco_var.set("")
        self.telefone_var.set("")
        self.email_var.set("")


root = tk.Tk()
app = CrudApp(root)
root.mainloop()
