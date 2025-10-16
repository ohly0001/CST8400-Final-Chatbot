from llama_cpp import Llama, LlamaTokenizer

class TransformerModel():
    def __init__(self, max_tokens) -> None:
        self.max_tokens = max_tokens
        self.transformer = Llama.from_pretrained(
            repo_id="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
            filename="mistral-7b-instruct-v0.1.Q2_K.gguf",
        )
        self.tokenizer = LlamaTokenizer(self.transformer)
    
    def __call__(self, *args, **kwds):
        pass