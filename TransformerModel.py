from llama_cpp import Llama, LlamaTokenizer

class TransformerModel():
    def __init__(self, max_tokens) -> None:
        self.max_tokens = max_tokens
        self.transformer = Llama()
        self.tokenizer = LlamaTokenizer(self.transformer)
    
    def __call__(self, *args, **kwds):
        pass