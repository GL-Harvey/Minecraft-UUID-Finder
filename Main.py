import requests
import customtkinter

def get_uuid(username):
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    if response:
        r1 = response.json()["id"]
        label.configure(text=f"UUID: {r1}")
    else:
        label.configure(text="Error: player not found")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Minecraft UUID Finder")

entry = customtkinter.CTkEntry(root, width=100, height=60)
entry.pack()

button = customtkinter.CTkButton(root, text="Submit", command=lambda: get_uuid(entry.get()))
button.pack()

label = customtkinter.CTkLabel(root, text="UUID: ")
label.pack()

root.mainloop()
