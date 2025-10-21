import time
from TransformerModel import TransformerModel
from FileModel import FileModel
from View import View

class Controller():
    def __init__(self, view: View, file_controller: FileModel, transformer: TransformerModel) -> None:
        # Assign own links to components
        self.view = view
        self.file_controller = file_controller
        self.transformer = transformer
        
        # Link to view to receive allow calls from UI
        self.view.controller = self
        
        self.current_conversation = None
        self.current_history = []
        self.conversations = []
        
    def setup(self):
        self.file_controller.setup()
        self.transformer.setup()

        self.current_history = self.file_controller.load_chat()
        
        self.transformer.setup()
        self.view.setup()
    
    def cleanup(self):
        self.file_controller.dump_chat(self.current_history)
        
    def create_conversation(self, name):
        t = time.time()
        data = {'metadata': {'createdOn': t,'lastAccessedOn': t}, 'content': []}
        
        self.file_controller.write_file(name + ".json", data)
        
        self.current_conversation = data
        self.current_history = []
        self.conversations.append(data)
        
    def switch_conversation(self, conv):
        pass
    
    def delete_conversation(self, conv):
        pass
    
    def rename_conversation(self, conv, new_name):
        pass
    
    def send_prompt(self, prompt_text):
        pass
    
    def edit_message(self, idx, new_text):
        pass
    
    def delete_message(self, idx):
        pass