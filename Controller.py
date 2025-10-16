from MistralModel import MistralModel
from MySQLModel import MySQLModel
from View import View

class Controller():
    def __init__(self, view: View, AI_model: MistralModel, DB_model: MySQLModel) -> None:
        # Assign own links to components
        self.view = view
        self.AI_model = AI_model
        self.DB_model = DB_model
        
        # Link to view to receive allow calls from UI
        self.view.controller = self
        
    def startup(self):
        # TODO, 
        # connect DB Model to DB server
        # load previous_chat labels + ids from DB model
        # load last accessed chat
        # load data from DB Model for last accessed chat if any
        # populate view chat history with data
        pass
    
    def shutdown(self):
        pass