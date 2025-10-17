import tkinter as tk

class View():
    def __init__(self) -> None:
        self.controller = None # Delayed Assignment
        self.root = None
        
    def setup(self):
        self.root = tk.Tk()
        self.root.title("Chatbot")
        
        self.chatHistoryContent = ""
        self.chatHistory = tk.Label(self.root, textvariable=self.chatHistoryContent)
        self.promptTF = tk.Text(self.root, height=3, width=15)
        promptButton = tk.Button(self.root, text="Send", command=self.send_prompt_cmd)
        
        self.chatHistory.pack()
        self.promptTF.pack()
        promptButton.pack()
        
        self.root.mainloop()
        
    def send_prompt_cmd(self):
        prompt_text = self.promptTF.get("1.0", "end-1c")
        
        self.controller.send_prompt_cmd(prompt_text)
        
    def set_history(self, username: str, history: list[dict[str,str]]):
        self.chatHistory = ""
        
        lines = []
        for entry in history:
            if entry['actor'] == 'AI':
                lines.append(f'Bot: {entry['text']}')
                
            elif entry['actor'] == 'User':
                lines.append(f'{entry['text']:>15} :{username}')
        
        self.chatHistoryContent = '\n'.join(lines)