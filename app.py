import tkinter as tk
import sqlite3

class ExercitoFicticio:
    def __init__(self, nome):
        self.nome = nome
        self.conn = sqlite3.connect("exercito.db")
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS soldados (
                nome TEXT,
                patente TEXT
            )
        ''')
        self.conn.commit()

    def recrutar_soldado(self, nome, patente):
        self.c.execute("INSERT INTO soldados VALUES (?, ?)", (nome, patente))
        self.conn.commit()
        return f"{nome} foi recrutado no exército {self.nome} como {patente}."

    def listar_soldados(self):
        self.c.execute("SELECT nome, patente FROM soldados")
        soldados = self.c.fetchall()
        return soldados

# Função para recrutar soldado
def recrutar_soldado():
    nome = entry_nome.get()
    patente = entry_patente.get()
    resultado = exercito.recrutar_soldado(nome, patente)
    lbl_resultado.config(text=resultado)

# Função para listar soldados
def listar_soldados():
    soldados = exercito.listar_soldados()
    soldados_text = "\n".join([f"Nome: {nome}, Patente: {patente}" for nome, patente in soldados])
    lbl_resultado.config(text=soldados_text)

# Criando uma instância do Exército fictício
exercito = ExercitoFicticio("Exército da Imaginação")

# Configurando a interface gráfica com tkinter
app = tk.Tk()
app.title("Warhub do Exército Fictício")

frame_recrutamento = tk.Frame(app)
frame_recrutamento.pack()

frame_listagem = tk.Frame(app)
frame_listagem.pack()

lbl_nome = tk.Label(frame_recrutamento, text="Nome do Soldado:")
lbl_nome.pack()
entry_nome = tk.Entry(frame_recrutamento)
entry_nome.pack()

lbl_patente = tk.Label(frame_recrutamento, text="Patente do Soldado:")
lbl_patente.pack()
entry_patente = tk.Entry(frame_recrutamento)
entry_patente.pack()

btn_recrutar = tk.Button(frame_recrutamento, text="Recrutar Soldado", command=recrutar_soldado)
btn_recrutar.pack()

btn_listar = tk.Button(frame_listagem, text="Listar Soldados", command=listar_soldados)
btn_listar.pack()

lbl_resultado = tk.Label(frame_listagem, text="", wraplength=300)
lbl_resultado.pack()

app.mainloop()
