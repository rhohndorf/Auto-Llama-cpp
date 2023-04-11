import openai
from config import Config
from llama_cpp import Llama

cfg = Config()
llm = Llama(model_path="ggml-vicuna-13b-4bit.bin", n_ctx=2048, embedding=True)
# openai.api_key = cfg.openai_api_key

# # Overly simple abstraction until we create something better
# def create_chat_completion(messages, model=None, temperature=None, max_tokens=None)->str:
#     """Create a chat completion using the OpenAI API"""
#     if cfg.use_azure:
#         response = openai.ChatCompletion.create(
#             deployment_id=cfg.openai_deployment_id,
#             model=model,
#             messages=messages,
#             temperature=temperature,
#             max_tokens=max_tokens
#         )
#     else:
#         response = openai.ChatCompletion.create(
#             model=model,
#             messages=messages,
#             temperature=temperature,
#             max_tokens=max_tokens
#         )

#     return response.choices[0].message["content"]

def create_chat_completion(messages, model=None, temperature=0.36, max_tokens=None)->str:
    print("Message Content", messages[0]["content"])
    response = llm(messages[0]["content"], stop=["Q:", "User:"], echo=False, temperature=temperature, max_tokens=max_tokens)

    print("Response", response)
    return response["choices"][0]["text"]
