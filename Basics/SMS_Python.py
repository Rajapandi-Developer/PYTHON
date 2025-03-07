import requests
requests.post("https://ntfy.sh/HereWeAre",
    data="Looks like we done".encode(encoding='utf-8'))

# import tkinter as tk
# import pyjokes
# # Create the main window
# root = tk.Tk()
# root.title("My First Tkinter GUI")
# # Add a label to the window
# label = tk.Label(root, text=pyjokes.get_jokes("en"))
# label.pack()
# # Start the Tkinter event loop
# root.mainloop()