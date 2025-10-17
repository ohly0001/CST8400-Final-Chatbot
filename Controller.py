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
        self.file_controller.setup()
        self.transformer.setup()
        # load previous_chat labels from directory
        # load last accessed chat (only keep active chat in memory, the rest are kept on disk only)
        # load data from json file for last accessed chat if any
        # populate view chat history with data
        pass
    
    def cleanup(self):
        pass