import tkinter as tk
from tkinter import ttk

def convertir_base(numero, base_origen, base_destino):
    try:
        partes = numero.split('.')  
        decimal_parte_entera = int(partes[0], base_origen)

        decimal_parte_decimal = 0
        if len(partes) == 2:
            longitud_decimal = len(partes[1])
            for i in range(longitud_decimal):
                decimal_parte_decimal += int(partes[1][i], base_origen) * (base_origen ** -(i + 1))

        decimal_numero = decimal_parte_entera + decimal_parte_decimal

        parte_entera_destino = ""
        parte_decimal_destino = ""
        parte_entera_decimal = int(decimal_numero)
        parte_decimal_decimal = decimal_numero - parte_entera_decimal

        while parte_entera_decimal > 0:
            residuo = parte_entera_decimal % base_destino
            parte_entera_destino = str(residuo) + parte_entera_destino
            parte_entera_decimal = parte_entera_decimal // base_destino

        if parte_decimal_decimal > 0:
            parte_decimal_destino += "."

        for _ in range(4):  
            parte_decimal_decimal *= base_destino
            digito = int(parte_decimal_decimal)
            parte_decimal_destino += str(digito)
            parte_decimal_decimal -= digito

        resultado = parte_entera_destino + parte_decimal_destino
        return resultado
    except ValueError:
        return "Error: Verifique que los números ingresados y la base sean correctos."

def realizar_conversion():
    numero = entrada_numero.get()
    base_origen = entrada_base_origen.get()
    base_destino = entrada_base_destino.get()

    # Verificar si el número ingresado es un número válido
    if not numero.replace('.', '').isdigit():
        etiqueta_resultado.config(text="Error: Ingrese un número válido.")
        return

    try:
        base_origen = int(base_origen)
        base_destino = int(base_destino)
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese bases válidas.")
        return
    
    resultado_conversion = convertir_base(numero, base_origen, base_destino)
    etiqueta_resultado.config(text=f"Resultado: {resultado_conversion}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Conversor de Bases")

# Cambiar el color de fondo de la ventana a verde
ventana.configure(bg='#1ABC9C')

# Crear y colocar widgets en la ventana
etiqueta_numero = ttk.Label(ventana, text="Número:", background='#0B5345', foreground='white')
etiqueta_base_origen = ttk.Label(ventana, text="Base de origen:", background='#0B5345', foreground='white')
etiqueta_base_destino = ttk.Label(ventana, text="Base de destino:", background='#0B5345', foreground='white')
etiqueta_resultado = ttk.Label(ventana, text="Resultado:", background='#0B5345', foreground='white')

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
