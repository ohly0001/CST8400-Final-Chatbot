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
        self.RESERVED_TOKENS = None
        self.AI_TAG = None
        self.USER_TAG = None
        self.MAX_OUT_TOKENS = None
        self.MAX_CTX_TOKENS = None
        self.AI_TAG_TOKENS = None
    
    def setup(self) -> None: 
        os.makedirs(self.MODEL_PATH, exist_ok=True)
        
        with open(self.META_PATH, 'r') as f:
            data = json.load(f)
            
        self.AI_TAG = data['transformer']['ai-tag']
        self.USER_TAG = data['transformer']['user-tag']
        self.MAX_OUT_TOKENS = int(data['transformer']['max-out-tokens'])
        self.MAX_CTX_TOKENS = int(data['transformer']['max-ctx-tokens'])

        self.transformer = Llama.from_pretrained(
            repo_id=data['import']['repo_id'],
            filename=data['import']['filename'],
            local_dir=self.MODEL_PATH
        )
        self.tokenizer = LlamaTokenizer(self.transformer)
        
        self.AI_TAG_TOKENS = self._count_tokens(self.AI_TAG)
        self.RESERVED_TOKENS = self.MAX_OUT_TOKENS + self.AI_TAG_TOKENS
        
    def _count_tokens(self, text: str) -> int:
        return len(self.tokenizer.encode(text))
    
    def __call__(self, history: list[str]) -> list[str]:
        # Reserve token overhead for full output
        token_count = self.MAX_OUT_TOKENS
        
        # Filter sequentially by cumalative token cost
        prompt_stack = []
        for entry in reversed(history):
            token_count += self._count_tokens()
            
            if token_count <= self.MAX_CTX_TOKENS:
                prompt_stack.append(entry)
            else:
                break
        
        prompt_stack.insert(0, self.AI_TAG)
        prompt_str = '\n'.join(prompt_stack)
        
        # Generate response
        response = self.transformer(
            prompt=prompt_str, 
            max_tokens=self.MAX_OUT_TOKENS
        )
        
        # Excise unwanted conversational chaining
        if self.USER_TAG in response:
            response = response.split(self.USER_TAG, 1)[0]
            
        history.append(response)
        return history