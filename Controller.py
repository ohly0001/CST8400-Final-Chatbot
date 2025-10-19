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
        
        self.current_history = []
        
    def setup(self):
        self.file_controller.setup()
        self.transformer.setup()

        self.current_history = self.file_controller.load_chat()
        
        self.transformer.setup()
        self.view.setup()
    
    def cleanup(self):
        self.file_controller.dump_chat(self.current_history)
        
    def send_prompt_cmd(self, prompt_text):
        prompt_text = self.transformer.USER_TAG + prompt_text
        
        self.current_history.append(prompt_text)
        self.current_history = self.transformer(self.current_history)
        
        self.view.set_history(self.file_controller.user_name, self.current_history)
    
    def new_chat_cmd(self, chat_name: str) -> bool:
        return self.file_controller.new_chat(chat_name.strip() + ".json")
    
        #TODO update UI
    
    def delete_chat_cmd(self, chat_name: str) -> bool:
        return self.file_controller.delete_chat(chat_name.strip() + ".json")
    
        #TODO update UI
    
    def open_chat_cmd(self, chat_name: str) -> bool:
        self.current_history = self.file_controller.load_chat(chat_name.strip() + ".json")
        
        #TODO update UI
        
    