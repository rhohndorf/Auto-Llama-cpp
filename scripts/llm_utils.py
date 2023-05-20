from config import Config
from llama_cpp import Llama

cfg = Config()
llm = Llama(model_path=cfg.smart_llm_model, n_ctx=2048, embedding=True)



def create_chat_completion(messages, model=None, temperature=cfg.temperature, max_tokens=0)->str:
    query = "".join([msg.get("content") for msg in messages])
    print(query)
    response = llm(query, stop=["Q:", "### Human:"], echo=False, temperature=temperature, max_tokens=max_tokens)
    return response["choices"][0]["text"]
