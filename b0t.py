import tkinter as tk
from tkinter import ttk
import threading
import time
from pynput import keyboard
from pynput.keyboard import Controller

def press_keys_once(keys, delay):
    for key in keys:
        keyboard_ctrl.press(key)
        keyboard_ctrl.release(key)
        time.sleep(delay)

def start_script():
    global stop_script_flag
    stop_script_flag = False

    # Desativa os campos de entrada
    set_entry_state("disable")

    script_thread = threading.Thread(target=run_script)
    script_thread.start()

def run_script():
    global stop_script_flag
    try:
        letters = letter_entry.get().lower().split(',')
        delay_letter = float(delay_letter_entry.get())
        delay_x = float(delay_x_entry.get())
        x_press_duration = float(x_duration_entry.get())
        inter_cycle_delay = float(inter_cycle_delay_entry.get())

        current_config_label.config(text=f"Letras pré-definidas: {', '.join(letters)}")

        # Configuração da barra de progresso
        progress_bar_var.set(0)
        progress_bar.config(mode="determinate", maximum=inter_cycle_delay * 1000)  # em milissegundos

        while not stop_script_flag:
            start_time = time.time()
            cycle_start_time = start_time

            while time.time() - cycle_start_time < inter_cycle_delay and not stop_script_flag:
                press_keys_once(letters, delay_letter)
                root.update_idletasks()

                inner_start_time = time.time()
                while time.time() - inner_start_time < x_press_duration and not stop_script_flag:
                    keyboard_ctrl.press('x')
                    time.sleep(delay_x)
                    keyboard_ctrl.release('x')
                    root.update_idletasks()

                # Atualiza a barra de progresso
                elapsed_time = time.time() - cycle_start_time
                progress_bar_var.set(elapsed_time * 1000)  # em milissegundos
                root.update_idletasks()

            # Se o script não foi interrompido, reinicia a barra de progresso
            if not stop_script_flag:
                progress_bar_var.set(0)

    except KeyboardInterrupt:
        print("Script interrompido pelo usuário.")

    finally:
        stop_script_button.config(state=tk.DISABLED)
        start_script_button.config(state=tk.NORMAL)
        # Ativa os campos de entrada após a conclusão do script
        set_entry_state("normal")

def stop_script():
    global stop_script_flag
    stop_script_flag = True

    stop_script_button.config(state=tk.DISABLED)
    start_script_button.config(state=tk.NORMAL)
    # Ativa os campos de entrada ao parar o script
    set_entry_state("normal")

def set_entry_state(state):
    letter_entry.config(state=state)
    delay_letter_entry.config(state=state)
    delay_x_entry.config(state=state)
    x_duration_entry.config(state=state)
    inter_cycle_delay_entry.config(state=state)

root = tk.Tk()
root.title("Script Automático")
root.geometry("400x500")
root.configure(bg="#f5f5f5")

keyboard_ctrl = Controller()

tk.Label(root, text="Letras (separadas por vírgula):", bg="#f5f5f5").pack()
letter_entry = tk.Entry(root)
letter_entry.insert(0, 'e,4,2,5,L,K,J,H')
letter_entry.pack(pady=5)

tk.Label(root, text="Atraso entre letras (segundos):", bg="#f5f5f5").pack()
delay_letter_entry = tk.Entry(root)
delay_letter_entry.insert(0, '1.6')
delay_letter_entry.pack(pady=5)

tk.Label(root, text="Atraso para 'X' (segundos):", bg="#f5f5f5").pack()
delay_x_entry = tk.Entry(root)
delay_x_entry.insert(0, '1.6')
delay_x_entry.pack(pady=5)

tk.Label(root, text="Duração do pressionamento de 'X' (segundos):", bg="#f5f5f5").pack()
x_duration_entry = tk.Entry(root)
x_duration_entry.insert(0, '10')
x_duration_entry.pack(pady=5)

tk.Label(root, text="Atraso entre ciclos (segundos):", bg="#f5f5f5").pack()
inter_cycle_delay_entry = tk.Entry(root)
inter_cycle_delay_entry.insert(0, '120')
inter_cycle_delay_entry.pack(pady=5)

current_config_label = tk.Label(root, text="Letras pré-definidas: e, 4, 2, 5, L, K, J, H", bg="#f5f5f5")
current_config_label.pack(pady=10)

# Barra de progresso
progress_bar_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, variable=progress_bar_var, mode='determinate')
progress_bar.pack(pady=10)

start_script_button = tk.Button(root, text="Iniciar", command=start_script)
start_script_button.pack(pady=20)

stop_script_button = tk.Button(root, text="Parar", command=stop_script, state=tk.DISABLED)
stop_script_button.pack(pady=20)

root.mainloop()
