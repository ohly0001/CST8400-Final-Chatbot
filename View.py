import tkinter as tk
from tkinter import simpledialog, messagebox

class View:
    def __init__(self) -> None:
        self.controller = None  # Delayed Assignment
        self.root = None
        
    def setup(self):
        self.root = tk.Tk()
        self.root.title("Chatbot")

        # Prompt input
        self.promptTF = tk.Text(self.root, height=3, width=40)
        promptButton = tk.Button(self.root, text="Send", command=self.send_prompt_cmd)

        # Conversation management buttons
        newConvBtn = tk.Button(self.root, text="New Conversation", command=self.new_conversation)
        renameConvBtn = tk.Button(self.root, text="Rename Conversation", command=self.rename_conversation)
        deleteConvBtn = tk.Button(self.root, text="Delete Conversation", command=self.delete_conversation)

        # Scrollable conversation list
        self.convFrame = tk.Frame(self.root)
        self.convCanvas = tk.Canvas(self.convFrame, height=150)
        self.convScrollbar = tk.Scrollbar(self.convFrame, orient="vertical", command=self.convCanvas.yview)
        self.convListFrame = tk.Frame(self.convCanvas)

        self.convListFrame.bind(
            "<Configure>",
            lambda e: self.convCanvas.configure(scrollregion=self.convCanvas.bbox("all"))
        )
        self.convCanvas.create_window((0, 0), window=self.convListFrame, anchor="nw")
        self.convCanvas.configure(yscrollcommand=self.convScrollbar.set)

        self.update_conversation_list()

        # Chat history
        self.chatHistoryCanvas = tk.Canvas(self.root)
        self.chatHistoryFrame = tk.Frame(self.chatHistoryCanvas)
        self.chatHistoryCanvas.create_window((0, 0), window=self.chatHistoryFrame, anchor="nw")
        self.chatHistoryFrame.bind(
            "<Configure>",
            lambda e: self.chatHistoryCanvas.configure(scrollregion=self.chatHistoryCanvas.bbox("all"))
        )

        self.set_history(self.controller.current_history)

        # Pack widgets
        self.convFrame.pack(fill="x")
        self.convCanvas.pack(side="left", fill="x", expand=True)
        self.convScrollbar.pack(side="right", fill="y")

        newConvBtn.pack()
        renameConvBtn.pack()
        deleteConvBtn.pack()

        self.chatHistoryCanvas.pack(fill="both", expand=True)
        self.promptTF.pack(fill="x")
        promptButton.pack()

        self.root.mainloop()

    # --- Conversation management ---
    def update_conversation_list(self):
        for widget in self.convListFrame.winfo_children():
            widget.destroy()

        # Sort conversations by lastAccessedOn descending
        sorted_convs = sorted(
            self.controller.conversations,
            key=lambda c: c['metadata']['lastAccessedOn'],
            reverse=True
        )

        for conv in sorted_convs:
            btn = tk.Button(
                self.convListFrame,
                text=conv['metadata']['name'],
                width=30,
                command=lambda c=conv: self.switch_conversation(c)
            )
            btn.pack(fill="x", pady=1)

    def new_conversation(self):
        name = simpledialog.askstring("New Conversation", "Enter conversation name:")
        if name:
            self.controller.create_conversation(name)
            self.update_conversation_list()

    def rename_conversation(self):
        conv = self.controller.current_conversation
        new_name = simpledialog.askstring("Rename Conversation", "Enter new name:", initialvalue=conv['metadata']['name'])
        if new_name:
            self.controller.rename_conversation(conv, new_name)
            self.update_conversation_list()

    def delete_conversation(self):
        conv = self.controller.current_conversation
        if messagebox.askyesno("Delete Conversation", f"Delete '{conv['metadata']['name']}'?"):
            self.controller.delete_conversation(conv)
            self.update_conversation_list()
            self.set_history(self.controller.current_history)

    def switch_conversation(self, conv):
        self.controller.switch_conversation(conv)
        self.set_history(self.controller.current_history)

    # --- Sending messages ---
    def send_prompt_cmd(self):
        prompt_text = self.promptTF.get("1.0", "end-1c")
        self.controller.send_prompt(prompt_text)
        self.set_history(self.controller.current_history)
        self.promptTF.delete("1.0", "end")

    # --- Chat history display ---
    def set_history(self, history: list[dict[str, str]]):
        for widget in self.chatHistoryFrame.winfo_children():
            widget.destroy()

        for i, entry in enumerate(history):
            if entry['speaker'] == 'AI':
                text = tk.Label(self.chatHistoryFrame, text=f'Bot: {entry["text"]}', anchor="w", justify="left")
            else:
                text = tk.Label(self.chatHistoryFrame, text=f'{entry["text"]:>25} :User', anchor="e", justify="right")

            text.pack(fill="x", pady=2)

            # Right-click popup menu for user messages
            if entry['speaker'] == 'User':
                menu = tk.Menu(self.root, tearoff=0)
                menu.add_command(label="Edit", command=lambda i=i: self.edit_message(i))
                menu.add_command(label="Delete", command=lambda i=i: self.delete_message(i))
                text.bind("<Button-3>", lambda e, m=menu: m.tk_popup(e.x_root, e.y_root))

    def edit_message(self, idx):
        history = self.controller.current_history
        current_text = history[idx]['text']
        new_text = simpledialog.askstring("Edit Message", "Edit your message:", initialvalue=current_text)
        if new_text is not None:
            self.controller.edit_message(idx, new_text)
            self.set_history(self.controller.current_history)

    def delete_message(self, idx):
        if messagebox.askyesno("Delete Message", "Delete this message and all succeeding messages?"):
            self.controller.delete_message(idx)
            self.set_history(self.controller.current_history)
