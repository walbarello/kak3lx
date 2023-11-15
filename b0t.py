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
        progress_text.config(state=tk.NORMAL)
        progress_text.delete(1.0, tk.END)

        start_time = time.time()
        while not stop_script_flag:
            press_keys_once(letters, delay_letter)
            update_progress_bar(inter_cycle_delay, start_time)

            inner_start_time = time.time()
            while time.time() - inner_start_time < x_press_duration and not stop_script_flag:
                keyboard_ctrl.press('x')
                time.sleep(delay_x)
                keyboard_ctrl.release('x')

    except KeyboardInterrupt:
        print("Script interrompido pelo usuário.")

    finally:
        stop_script_button.config(state=tk.DISABLED)
        start_script_button.config(state=tk.NORMAL)

def update_progress_bar(duration, start_time):
    current_time = time.time() - start_time
    progress_percent = min(current_time / duration, 1.0)
    progress_width = int(progress_percent * 40)  # Ajuste conforme necessário
    progress_text.delete(1.0, tk.END)
    progress_text.insert(tk.END, "[" + "#" * progress_width + "-" * (40 - progress_width) + "]")
    progress_text.config(state=tk.DISABLED)
    root.update_idletasks()

def stop_script():
    global stop_script_flag
    stop_script_flag = True

    stop_script_button.config(state=tk.DISABLED)
    start_script_button.config(state=tk.NORMAL)

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

progress_text = tk.Text(root, height=1, width=40, state=tk.DISABLED)
progress_text.pack(pady=10)

start_script_button = tk.Button(root, text="Iniciar", command=start_script)
start_script_button.pack(pady=20)

stop_script_button = tk.Button(root, text="Parar", command=stop_script, state=tk.DISABLED)
stop_script_button.pack(pady=20)

root.mainloop()
