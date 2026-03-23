import random
import string
import customtkinter

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x500")
root.title("Passwort Generator")

var_upper  = customtkinter.BooleanVar(value=True)
var_lower  = customtkinter.BooleanVar(value=True)
var_digits = customtkinter.BooleanVar(value=True)
var_special = customtkinter.BooleanVar(value=True)

def toggle_appearance():
    if appearance_switch.get() == 1:
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

def generate_password():
    length = entry.get()
    characters = ""
    if var_upper.get():   characters += string.ascii_uppercase
    if var_lower.get():   characters += string.ascii_lowercase
    if var_digits.get():  characters += string.digits
    if var_special.get(): characters += string.punctuation

    if not characters:
        done_label.configure(text="Mindestens eine Zeichenart wählen!")
        return
    if not length.isdigit():
        done_label.configure(text="Bitte eine Zahl eingeben!")
        return

    done_label.configure(text="")
    password = "".join(random.choice(characters) for _ in range(int(length)))
    password_label.configure(text=password)

def copy_password():
    password = password_label.cget("text")
    frame.clipboard_clear()
    frame.clipboard_append(password)
    done_label.configure(text="kopiert!")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(frame, text="Passwort Generator", font=("Roboto", 24))
label.pack(pady=12, padx=10)

appearance_switch = customtkinter.CTkSwitch(frame, text="Dark Mode", command=toggle_appearance)
appearance_switch.select()
appearance_switch.pack(pady=8, padx=10)

checkbox_frame = customtkinter.CTkFrame(frame)
checkbox_frame.pack(pady=8, padx=10)

customtkinter.CTkCheckBox(checkbox_frame, text="A–Z",  variable=var_upper).grid(row=0, column=0, padx=10, pady=6)
customtkinter.CTkCheckBox(checkbox_frame, text="a–z",  variable=var_lower).grid(row=0, column=1, padx=10, pady=6)
customtkinter.CTkCheckBox(checkbox_frame, text="0–9",  variable=var_digits).grid(row=0, column=2, padx=10, pady=6)
customtkinter.CTkCheckBox(checkbox_frame, text="!@#…", variable=var_special).grid(row=0, column=3, padx=10, pady=6)

entry = customtkinter.CTkEntry(frame, width=100, placeholder_text="Anzahl Zeichen", placeholder_text_color=("gray40", "gray60"))
entry.pack(pady=12, padx=10)

generate_button = customtkinter.CTkButton(frame, text="Passwort generieren", command=generate_password)
generate_button.pack(pady=12, padx=10)

copy_button = customtkinter.CTkButton(frame, text="Passwort kopieren", command=copy_password)
copy_button.pack(pady=12, padx=10)

password_label = customtkinter.CTkLabel(frame, text="", font=("Roboto", 24))
password_label.pack(pady=12, padx=10)

done_label = customtkinter.CTkLabel(frame, text="", font=("Roboto", 20))
done_label.pack(pady=12, padx=10)

root.mainloop()
