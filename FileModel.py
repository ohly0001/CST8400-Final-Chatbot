import os
import json

class FileModel():
    def __init__(self) -> None:
        self.CHATS_PATH = r'.\chats'
        self.META_PATH = r'.\metadata\chats.json'
        self.chat_filenames = []
       
    def setup(self) -> None:  
        if not os.path.exists(self.META_PATH):
            # Builds / Repairs application by regenerating
            with open(self.META_PATH, 'x') as f:
                json.dump({
                    'current_chat': None
                }, f, ensure_ascii=False, indent=4)
                
        else:
            with open(self.META_PATH, 'r') as f:
                data = json.load(f)
                
            self.current_chat = data['current_chat']          
         
        os.makedirs(self.CHATS_PATH, exist_ok=True)    
        self.chat_filenames = os.listdir(self.CHATS_PATH)
        
    def load_chat(self):
        if self.current_chat:
            filepath = os.path.join(self.CHATS_PATH, self.current_chat)
            with open(filepath, 'r') as f:
                return json.load(f)
        
        else:
            return {}