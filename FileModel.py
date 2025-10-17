import os
import json

class FileModel():
    def __init__(self) -> None:
        self.CHATS_PATH = r'.\chats'
        self.META_PATH = r'.\metadata\chats.json'
        self.chat_filenames = []
        self.previous_chat_name = None
        self.user_name = None
        
    def setup(self) -> None:
        os.makedirs(self.CHATS_PATH, exist_ok=True)
        
        try:
            if not os.path.exists(self.META_PATH):
                with open(self.META_PATH, 'x') as f:
                    json.dump({
                        'previous_chat_name':None, 
                        'user_name':None
                    }, f, ensure_ascii=False, indent=4)
            else:
                with open(self.META_PATH, 'r') as f:
                    data = json.load(f)
                    self.previous_chat_name = data.get('previous_chat_name', None)
                    self.user_name = data.get('user_name', None)
            
        except OSError:
            print(f"Chat setup failed: {self.META_PATH} failed to open")
            exit(1)
            
        except json.JSONDecodeError as e:
            print(f"Chat setup failed: {self.META_PATH} failed to decode")
            exit(1)
    
    def load_chat(self, filename: str = None) -> list[dict[str,str]] | None:
        if not filename: # default to previous chat
            self.previous_chat_name = filename
        if filename not in self.chat_filenames:
            return None
        filepath = os.path.join(self.CHATS_PATH, filename)
        with open(filepath, 'r') as f:
            return json.load(f)
        
    def dump_chat(self, data: list[dict[str, str]]) -> bool:
        if self.previous_chat_name and data:
            filepath = os.path.join(self.CHATS_PATH, self.previous_chat_name)
            with open(filepath, 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        return False
            
    def new_chat(self, chat_name: str) -> bool:
        filename = chat_name + '.json'
        if filename not in self.chat_filenames:
            self.previous_chat_name = chat_name
            self.chat_filenames.append(filename)
            filepath = os.path.join(self.CHATS_PATH, filename)
            with open(filepath, 'x') as f:
                f.write('{}')
            return True
        return False
            
    def delete_chat(self, chat_name: str) -> bool:
        filename = chat_name + '.json'
        if filename in self.chat_filenames:
            self.chat_filenames.remove(filename)
            filepath = os.path.join(self.CHATS_PATH, filename)
            os.remove(filepath)
            return True
        return False