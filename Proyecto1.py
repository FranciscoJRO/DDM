import tkinter as tk
from tkinter import ttk

def convertir_base(numero, base_origen, base_destino):
    try:
        # Convertir el número a base 10
        decimal_numero = int(numero, base_origen)
        
        # Convertir el número de base 10 a la base de destino
        digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Dígitos permitidos en bases hasta la base 36
        resultado = ""
        while decimal_numero > 0:
            residuo = decimal_numero % base_destino
            resultado = digitos[residuo] + resultado
            decimal_numero = decimal_numero // base_destino

        return resultado
    except ValueError:
        return "Error: Verifique que los números ingresados y la base sean correctos."


def realizar_conversion():
    numero = entrada_numero.get()
    base_origen = int(entrada_base_origen.get())
    base_destino = int(entrada_base_destino.get())
    
    resultado_conversion = convertir_base(numero, base_origen, base_destino)
    
    etiqueta_resultado.config(text=f"Resultado: {resultado_conversion}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Conversor de Bases")

# Cambiar el color de fondo de la ventana a verde
ventana.configure(bg='#1ABC9C')

# Crear y colocar widgets en la ventana
etiqueta_numero = ttk.Label(ventana, text="Número:", background='#1ABC9C', foreground='white')
etiqueta_base_origen = ttk.Label(ventana, text="Base de origen:", background='#1ABC9C', foreground='white')
etiqueta_base_destino = ttk.Label(ventana, text="Base de destino:", background='#1ABC9C', foreground='white')
etiqueta_resultado = ttk.Label(ventana, text="Resultado:", background='#1ABC9C', foreground='white')

entrada_numero = ttk.Entry(ventana, foreground='white')
entrada_base_origen = ttk.Entry(ventana, foreground='white')
entrada_base_destino = ttk.Entry(ventana, foreground='white')

boton_convertir = ttk.Button(ventana, text="Convertir", command=realizar_conversion, style='TButton')

# Colocar widgets usando grid
etiqueta_numero.grid(column=0, row=0, padx=5, pady=5, sticky='E')
etiqueta_base_origen.grid(column=0, row=1, padx=5, pady=5, sticky='E')
etiqueta_base_destino.grid(column=0, row=2, padx=5, pady=5, sticky='E')
etiqueta_resultado.grid(column=0, row=4, columnspan=2, padx=5, pady=5, sticky='W')

entrada_numero.grid(column=1, row=0, padx=5, pady=5, sticky='W')
entrada_base_origen.grid(column=1, row=1, padx=5, pady=5, sticky='W')
entrada_base_destino.grid(column=1, row=2, padx=5, pady=5, sticky='W')

boton_convertir.grid(column=0, row=3, columnspan=2, pady=10)

# Establecer un estilo para el botón
ttk.Style().configure('TButton', background='#7D3C98', foreground='white')

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()
