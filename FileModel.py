import os
import json

class FileModel():
    def __init__(self) -> None:
        self.chats_filepath = r'.\chats'
        self.chat_filenames = []
        
        self.metadata_filename= 'meta.json'
        
        self.previous_chat_name = None
        self.user_name = None
        
    def setup(self) -> None:
        os.makedirs(self.chats_filepath, exist_ok=True)
        self.chat_filenames = os.listdir(self.chats_filepath)
        
        metadata_filepath = os.path.join(self.chats_filepath, self.metadata_filename)
        if self.metadata_filename in self.chat_filenames:
            self.chat_filenames.remove(self.metadata_filename)
            
            with open(metadata_filepath, 'r') as f:
                data = json.load(f)
                self.previous_chat_name = data.get('previous_chat_name', None)
                self.user_name = data.get('user_name', None)
                
                if self.previous_chat_name is not None:
                    file_index = self.chat_filenames.index(self.previous_chat_name) 
                    self.load_chat(file_index)
        
        else:
            with open(metadata_filepath, 'x') as f:
                f.write('{}')
    
    def load_chat(self, filename: str):
        if filename not in self.chat_filenames:
            return {}
        self.previous_chat_name = filename
        filepath = os.path.join(self.chats_filepath, filename)
        with open(filepath, 'r') as f:
            return json.load(f)
        
    def dump_chat(self, data: dict[str, str]):
        if self.previous_chat_name and data:
            filepath = os.path.join(self.chats_filepath, self.previous_chat_name)
            with open(filepath, 'w') as f:
                return json.dump(data, f, ensure_ascii=False, indent=4)
            
    def new_chat(self, chat_name: str):
        filename = chat_name + '.json'
        if filename not in self.chat_filenames:
            self.chat_filenames.append(filename)
            filepath = os.path.join(self.chats_filepath, filename)
            with open(filepath, 'x') as f:
                f.write('{}')
            
    def delete_chat(self, chat_name: str):
        filename = chat_name + '.json'
        if filename in self.chat_filenames:
            self.chat_filenames.remove(filename)
            filepath = os.path.join(self.chats_filepath, filename)
            os.remove(filepath)