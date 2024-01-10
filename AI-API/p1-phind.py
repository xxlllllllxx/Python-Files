import customtkinter as ctk
from tkinter import END
import requests


class ChatWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x500")
        self.title("Chat Window")

        # Create a scrollable text area for displaying messages
        self.messages = ctk.CTkScrollableFrame(self)
        self.messages.pack(expand=True, fill='both')

        # Create a text entry field for entering new messages
        self.message_entry = ctk.CTkEntry(self)
        self.message_entry.pack(fill='x', side='bottom')

        # Create a button for sending messages
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.send_button.pack(side='bottom')

    def send_message(self):
        # Get the message from the entry field
        message = self.message_entry.get()

        # Send the message to the Phind API
        headers = {'Authorization': 'Bearer your_api_key'}
        data = {'message': message}
        response = requests.post('https://api.phind.io/v1/endpoint', headers=headers, data=data)

        if response.status_code == 200:
            # Add the response from the Phind API to the text area
            self.messages.insert(END, f"> {response.text}\n")
        else:
            # Add an error message to the text area
            self.messages.insert(END, f"> Error: {response.status_code}\n")

        # Clear the entry field
        self.message_entry.delete(0, END)


app = ChatWindow()
app.mainloop()
