import tkinter as tk
from tkinter import ttk

# Función para convertir un número de una base a otra
def convertir_base(numero, base_origen, base_destino):
    try:
        partes = numero.split('.')  # Dividir el número en su parte entera y decimal
        parte_entera = int(partes[0], base_origen)

        # Convertir la parte entera a la base de destino
        resultado_entero = ""
        digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while parte_entera > 0:
            residuo = parte_entera % base_destino
            resultado_entero = digitos[residuo] + resultado_entero
            parte_entera = parte_entera // base_destino

        resultado_decimal = ""
        if len(partes) == 2:
            longitud_decimal = len(partes[1])
            parte_decimal = sum(int(partes[1][i], base_origen) * (base_origen ** -(i + 1)) for i in range(longitud_decimal))

            # Convertir la parte decimal a la base de destino
            for _ in range(4):  # Aquí puedes ajustar la precisión de la parte decimal
                parte_decimal *= base_destino
                digito = int(parte_decimal)
                resultado_decimal += digitos[digito]
                parte_decimal -= digito

        resultado = resultado_entero
        if resultado_decimal:  # Agregar la parte decimal si existe
            resultado += "." + resultado_decimal

        return resultado
    except (ValueError, IndexError):
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
