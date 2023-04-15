import openai
from config import Config
from llama_cpp import Llama

cfg = Config()
llm = Llama(model_path="/home/ruben/Code/llama.cpp/models/13B/ggml-vicuna-13b-4bit.bin", n_ctx=2048, embedding=True)


def create_chat_completion(messages, model=None, temperature=0.36, max_tokens=None)->str:
    response = llm(messages[0]["content"], stop=["Q:", "### Human:"], echo=False, temperature=temperature, max_tokens=max_tokens)
    return response["choices"][0]["text"]
