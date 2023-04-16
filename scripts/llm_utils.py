import openai
from config import Config
from llama_cpp import Llama

cfg = Config()

model_path = cfg.model_path

llm = Llama(model_path, n_ctx=2048, embedding=True)


def create_chat_completion(messages, model=None, temperature=0.36, max_tokens=None)->str:
    response = llm(messages[0]["content"], stop=["Q:", "### Human:"], echo=False, temperature=temperature, max_tokens=max_tokens)
    return response["choices"][0]["text"]
