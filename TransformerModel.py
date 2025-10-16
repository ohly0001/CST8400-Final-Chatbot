import json
import os
from llama_cpp import Llama, LlamaTokenizer

class TransformerModel():
    def __init__(self) -> None:
        self.MODEL_PATH = r".\model"
        self.META_PATH = r'.\metadata\model.json'
        self.transformer = None
        self.tokenizer = None
        self.metadata = None     
    
    def setup(self) -> None: 
        os.makedirs(self.MODEL_PATH, exist_ok=True)
        
        try:
            with open(self.META_PATH, 'r') as f:
                self.metadata = json.load(f)
                
        except OSError as e:
            print(f"Transformer setup failed: {self.META_PATH} failed to open")
            exit(1)   
            
        except json.JSONDecodeError as e:
            print(f"Transformer setup failed: {self.META_PATH} failed to decode")
            exit(1)       

        self.transformer = Llama.from_pretrained(
            repo_id=self.metadata['Llama']['repo_id'],
            filename=self.metadata['Llama']['filename'],
            local_dir=self.MODEL_PATH
        )
        self.tokenizer = LlamaTokenizer(self.transformer)
    
    def __call__(self, *args, **kwds):
        pass