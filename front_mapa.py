import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importa funções do back-end
from back import gerar_topojson, gerar_preview

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Format Map Generator")
app.geometry("1100x650")

main_frame = ctk.CTkFrame(app)
main_frame.pack(fill=ctk.BOTH, expand=True)

output_dir = None

def abrir_configuracoes():
    global output_dir
    pasta = filedialog.askdirectory(title="Selecione a pasta de saída")
    if pasta:
        output_dir = pasta
        messagebox.showinfo("Configurações", f"Pasta de saída definida:\n{output_dir}")

# ---------------- Left Panel ----------------
left_panel = ctk.CTkFrame(main_frame, width=300)
left_panel.pack_propagate(False)
left_panel.pack(side=ctk.LEFT, fill=ctk.Y, padx=10, pady=10)

ctk.CTkLabel(left_panel, text="🗾", font=("Arial", 56), justify="center", anchor="center").pack(pady=(28,6), fill="x")
ctk.CTkLabel(left_panel, text="Format Map Generator", font=("Arial", 20, "bold")).pack(pady=5)
ctk.CTkLabel(left_panel, text="Gere mapas para o visual de Mapas de Formato no Power BI.", justify="center", wraplength=260).pack(pady=10)
ctk.CTkButton(left_panel, text="⚙️ Configurações", command=abrir_configuracoes).pack(pady=10)
ctk.CTkButton(left_panel, text="ℹ️ Sobre", command=lambda: messagebox.showinfo(
    "Sobre",
    "Gera arquivos TopoJSON para utilização no Power BI. Eles já vêm totalmente configurados — basta carregar e usar."
)).pack(pady=10)

# ---------------- Right Panel ----------------
right_panel = ctk.CTkFrame(main_frame)
right_panel.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=(0,10), pady=10)

ctk.CTkLabel(right_panel, text="Selecionar mapa").pack(pady=5)

# Container de comboboxes
combo_container = ctk.CTkFrame(right_panel, fg_color="transparent")
combo_container.pack(pady=10, padx=15, fill="x")

combo_frame = ctk.CTkFrame(combo_container, fg_color="transparent")
combo_frame.pack(side="left", fill="x", expand=True)

# Combobox País
combo_pais = ctk.CTkComboBox(combo_frame, values=["Brasil"])
combo_pais.pack(side="left", padx=5, fill="x", expand=True)

# Combobox Tipo
combo_tipo = ctk.CTkComboBox(combo_frame, values=["Estadual", "Municipal"])
combo_tipo.pack(side="left", padx=5, fill="x", expand=True)

# Combobox Estado (não aparece inicialmente)
combo_estado = ctk.CTkComboBox(combo_frame, values=[
    "AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT",
    "PA","PB","PE","PI","PR","RJ","RN","RO","RR","RS","SC","SE","SP","TO"
])

# Preview Frame
preview_frame = ctk.CTkFrame(right_panel, fg_color="white", corner_radius=10)
preview_frame.pack(pady=10, padx=15, fill="both", expand=True)
preview_frame.pack_propagate(False)

preview_label = ctk.CTkLabel(preview_frame, text="Pré-visualização do mapa aparecerá aqui", text_color="black", font=("Arial", 14, "italic"))
preview_label.pack(expand=True)

# ---------------- Funções ----------------

def visualizar():
    tipo = combo_tipo.get()
    estado = combo_estado.get() if tipo == "Municipal" else None

    if tipo == "Estadual":
        messagebox.showinfo("Em desenvolvimento", "Pré-visualização estadual está em desenvolvimento.")
        return

    if not estado:
        messagebox.showwarning("Atenção", "Selecione um estado para pré-visualização.")
        return

    try:
        fig = gerar_preview(tipo, estado)
        for widget in preview_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=preview_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar pré-visualização:\n{e}")

btn_visualizar = ctk.CTkButton(combo_container, text="Visualizar", command=visualizar)
btn_visualizar.pack(side="right", padx=5)

def atualizar_estado(opcao):
    combo_estado.pack_forget()
    if opcao == "Municipal":
        combo_estado.pack(side="left", padx=5, fill="x", expand=True)

combo_tipo.configure(command=lambda opt: atualizar_estado(opt))

def gerar_topojson_frontend():
    tipo = combo_tipo.get()
    estado_selecionado = combo_estado.get() if tipo == "Municipal" else None

    if tipo == "Estadual":
        messagebox.showinfo("Em desenvolvimento", "Gerar TopoJSON estadual está em desenvolvimento.")
        return

    if not estado_selecionado:
        messagebox.showwarning("Atenção", "Selecione um estado antes de gerar o mapa.")
        return

    try:
        output_path = gerar_topojson(tipo, estado_selecionado, pasta_saida=output_dir)
        messagebox.showinfo("Sucesso", f"TopoJSON criado!\nArquivo salvo em:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar TopoJSON:\n{e}")

botao_gerar = ctk.CTkButton(right_panel, text="✅ Gerar TopoJson", command=gerar_topojson_frontend)
botao_gerar.pack(pady=(5,25), padx=15, fill="x")

app.mainloop()