from config import Config
from llama_cpp import Llama
from llama_cpp.llama_grammar import LlamaGrammar

cfg = Config()
grammar = LlamaGrammar.from_file("/home/ruben/Code/Auto-Llama-cpp/grammars/json.gbnf")
llm = Llama(model_path=cfg.smart_llm_model, n_ctx=2048, embedding=True, n_gpu_layers=40)



def create_chat_completion(messages, model=None, temperature=cfg.temperature, max_tokens=0)->str:
    query = "".join([msg.get("content") for msg in messages])
    print(query)
    response = llm(query, stop=["Q:", "### Human:"], echo=False, temperature=temperature, max_tokens=max_tokens, grammar=grammar)
    return response["choices"][0]["text"]
