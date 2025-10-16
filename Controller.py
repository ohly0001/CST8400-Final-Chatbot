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
        
    def setup(self):
        self.f_model.setup()
        # load previous_chat labels + ids from DB model
        # load last accessed chat
        # load data from DB Model for last accessed chat if any
        # populate view chat history with data
        pass
    
    def cleanup(self):
        pass