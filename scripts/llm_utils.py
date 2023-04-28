from config import Config
from llama_cpp import Llama

cfg = Config()
llm = Llama(model_path=cfg.smart_llm_model, n_ctx=cfg.n_ctx, embedding=True)

def create_chat_completion(messages, model=None, temperature=cfg.temperature, max_tokens=0)->str:
    message = ""
    for i in messages:
        message += i.get("content")
    response = llm(message, stop=["Q:", "### Human:"], echo=False, temperature=temperature, max_tokens=max_tokens)
    return response["choices"][0]["text"]
