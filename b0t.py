import tkinter as tk
from tkinter import ttk
import math
import time
from pynput import keyboard
from pynput.keyboard import Controller

def press_keys_once(keys, delay):
    # Pressiona as teclas da lista uma vez cada
    for key in keys:
        keyboard_ctrl.press(key)
        keyboard_ctrl.release(key)
        time.sleep(delay)
        update_progress_bar()

def start_script():
    try:
        # Obtém os valores dos campos de entrada
        letters = letter_entry.get().lower().split(',')
        delay_letter = float(delay_letter_entry.get())
        delay_x = float(delay_x_entry.get())
        x_press_duration = float(x_duration_entry.get())
        inter_cycle_delay = float(inter_cycle_delay_entry.get())

        # Exibe as letras pré-definidas
        current_config_label.config(text=f"Letras pré-definidas: {', '.join(letters)}")

        while not stop_script_flag:
            # Executa a primeira parte do ciclo
            press_keys_once(letters, delay_letter)

            # Loop de duração definida pressionando apenas 'X'
            start_time = time.time()
            while time.time() - start_time < x_press_duration and not stop_script_flag:
                keyboard_ctrl.press('x')
                time.sleep(delay_x)
                keyboard_ctrl.release('x')
                update_progress_bar()

            # Aguarda o tempo definido antes de reiniciar o ciclo
            sleep_with_progress_bar(inter_cycle_delay)

    except KeyboardInterrupt:
        print("Script interrompido pelo usuário.")

    finally:
        # Reativar botão de iniciar
        start_script_button.config(state=tk.NORMAL)
        stop_script_button.config(state=tk.DISABLED)

def sleep_with_progress_bar(duration):
    for _ in range(int(duration)):
        time.sleep(1)
        update_progress_bar()

def update_progress_bar():
    current_time = time.time() - start_script_time
    progress_value = min(current_time / script_duration, 1.0) * 100
    progress_bar_var.set(progress_value)
    root.update_idletasks()

# Cria a janela principal
root = tk.Tk()
root.title("Script Automático")
root.geometry("400x500")
root.configure(bg="#f5f5f5")

# Criar um controlador de teclado global
keyboard_ctrl = Controller()

# Labels e campos de entrada
tk.Label(root, text="Letras (separadas por vírgula):", bg="#f5f5f5").pack()
letter_entry = tk.Entry(root)
letter_entry.insert(0, 'e,4,2,5,L,K,J,H')  # Valores iniciais
letter_entry.pack(pady=5)

tk.Label(root, text="Atraso entre letras (segundos):", bg="#f5f5f5").pack()
delay_letter_entry = tk.Entry(root)
delay_letter_entry.insert(0, '1.6')  # Valor inicial
delay_letter_entry.pack(pady=5)

tk.Label(root, text="Atraso para 'X' (segundos):", bg="#f5f5f5").pack()
delay_x_entry = tk.Entry(root)
delay_x_entry.insert(0, '1.6')  # Valor inicial
delay_x_entry.pack(pady=5)

tk.Label(root, text="Duração do pressionamento de 'X' (segundos):", bg="#f5f5f5").pack()
x_duration_entry = tk.Entry(root)
x_duration_entry.insert(0, '10')  # Valor inicial
x_duration_entry.pack(pady=5)

tk.Label(root, text="Atraso entre ciclos (segundos):", bg="#f5f5f5").pack()
inter_cycle_delay_entry = tk.Entry(root)
inter_cycle_delay_entry.insert(0, '120')  # Valor inicial
inter_cycle_delay_entry.pack(pady=5)

# Caixa de texto para exibir as letras pré-definidas
current_config_label = tk.Label(root, text="Letras pré-definidas: e, 4, 2, 5, L, K, J, H", bg="#f5f5f5")
current_config_label.pack(pady=10)

# Barra de progresso
progress_bar_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_bar_var, maximum=100)
progress_bar.pack(fill=tk.X, pady=10)

# Botões de iniciar e parar com efeitos visuais
start_script_button_style = ttk.Style()
start_script_button_style.configure('TButton', foreground='white')
start_script_button = ttk.Button(root, text="Iniciar", command=start_script, style='TButton')
start_script_button.pack(pady=20)

stop_script_button_style = ttk.Style()
stop_script_button_style.configure('TButton', foreground='white')
stop_script_button = ttk.Button(root, text="Parar", command=lambda: stop_script_button.config(state=tk.DISABLED), style='TButton')
stop_script_button.pack(pady=20)

# Flag para controlar o script
stop_script_flag = False

# Variáveis para controle de tempo e duração do script
start_script_time = time.time()
script_duration = float("inf")  # Definido como infinito

# Atualiza os efeitos visuais
root.after(50, update_progress_bar)

# Executa a aplicação
root.mainloop()
e
