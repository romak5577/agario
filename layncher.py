import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Game Menu")

# --- Змінні ---
anim_phase = 0

# --- Функція старту ---
def start_game():
    nickname = nickname_entry.get()
    ip = ip_entry.get()
    port = port_entry.get()

    if not nickname.strip():
        status_label.configure(text="Enter nickname!")
        return
    if not ip.strip():
        status_label.configure(text="Enter IP!")
        return
    if not port.isdigit():
        status_label.configure(text="Port must be a number!")
        return

    # Очищення
    for widget in app.winfo_children():
        widget.destroy()

    # "Гра"
    text = f"Connecting to {ip}:{port}\nHello, {nickname}!"
    label = ctk.CTkLabel(app, text=text, font=("Arial", 30))
    label.pack(expand=True)


# --- Анімація ---
def animate():
    global anim_phase
    anim_phase += 0.05

    # Пульсація розміру
    size = int(50 + 5 * (1 + __import__("math").sin(anim_phase)))

    # Плавний колір (синій → фіолетовий)
    r = int(100 + 100 * (1 + __import__("math").sin(anim_phase)) / 2)
    g = 150
    b = 255

    color = f"#{r:02x}{g:02x}{b:02x}"

    title.configure(font=("Arial", size), text_color=color)

    app.after(30, animate)


# --- UI ---

title = ctk.CTkLabel(app, text="GAME MENU", font=("Arial", 50))
title.pack(pady=60)

nickname_entry = ctk.CTkEntry(app, placeholder_text="Nickname", width=300)
nickname_entry.pack(pady=10)

ip_entry = ctk.CTkEntry(app, placeholder_text="Server IP (e.g. 127.0.0.1)", width=300)
ip_entry.pack(pady=10)

port_entry = ctk.CTkEntry(app, placeholder_text="Port (e.g. 7777)", width=300)
port_entry.pack(pady=10)

play_button = ctk.CTkButton(app, text="Connect", command=start_game)
play_button.pack(pady=20)

status_label = ctk.CTkLabel(app, text="", text_color="red")
status_label.pack()

# ENTER = старт
def on_enter(event):
    start_game()

app.bind("<Return>", on_enter)

# запуск анімації
animate()

app.mainloop()
