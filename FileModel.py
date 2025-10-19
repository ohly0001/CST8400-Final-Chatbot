import os
import json

class FileModel():
    def __init__(self) -> None:
        self.CHATS_PATH = r'.\chats'
        self.META_PATH = r'.\metadata\chats.json'
        self.chat_filenames = []
        self.current_chat = None
        self.current_history = []
       
    def setup(self) -> None:  
        if not os.path.exists(self.META_PATH):
            # Builds / Repairs application by regenerating
            with open(self.META_PATH, 'x') as f:
                json.dump({
                    'current_chat': None
                }, f, ensure_ascii=False, indent=4)
                
        else:
             with open(self.META_PATH, 'r') as f:
                metadata = json.load(f)
                self.current_chat = metadata.get('current_chat', None)          
         
        os.makedirs(self.CHATS_PATH, exist_ok=True)    
        self.chat_filenames = os.listdir(self.CHATS_PATH)
        
        self.load_chat()
    
    def load_chat(self, filename: str = None) -> list[dict[str,str]] | None:  
        if filename not in self.chat_filenames:
            return
        
        self.current_chat = filename
        filepath = os.path.join(self.CHATS_PATH, self.current_chat)
        
        with open(filepath, 'r') as f:
            self.current_history = json.load(f)
        
    def dump_chat(self, data: list[dict[str, str]]) -> bool:
        """
        if self.current_chat and data:
            filepath = os.path.join(self.CHATS_PATH, self.current_chat)
            with open(filepath, 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        return False
        """
            
    def new_chat(self, chat_name: str) -> bool:
        """
        filename = chat_name + '.json'
        if filename not in self.chat_filenames:
            self.current_chat = chat_name
            self.chat_filenames.append(filename)
            filepath = os.path.join(self.CHATS_PATH, filename)
            with open(filepath, 'x') as f:
                f.write('{}')
            return True
        return False
        """
            
    def delete_chat(self, chat_name: str) -> bool:
        """
        filename = chat_name + '.json'
        if filename in self.chat_filenames:
            self.chat_filenames.remove(filename)
            filepath = os.path.join(self.CHATS_PATH, filename)
            os.remove(filepath)
            return True
        return False
        """