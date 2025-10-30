from FileModel import FileModel
from TransformerModel import TransformerModel
from View import View
from Controller import Controller

if __name__ == '__main__':
    view = View()
    f_model = FileModel()
    AI_model = TransformerModel()
    controller = Controller(view, f_model, AI_model) 
    controller.setup()