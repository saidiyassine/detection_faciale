import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

login = ctk.CTk()
login.geometry("500x350")

def def_connexion():
    print("Bienvenue avec Nous")
    
frame = ctk.CTkFrame(master=login)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Se Connecter")
label.pack(pady=12, padx=10)

champ1 = ctk.CTkEntry(master=frame, placeholder_text="User")
champ1.pack(pady=12)

champ2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
champ2.pack(pady=12)

button = ctk.CTkButton(master=frame, text="Connexion", command=def_connexion)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)



login.mainloop()