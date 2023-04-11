"""Base class for memory providers."""
import abc
from config import AbstractSingleton
# import openai
from llm_utils import llm

def get_ada_embedding(text):
    text = text.replace("\n", " ")
    # return openai.Embedding.create(input=[text], model="text-embedding-ada-002")["data"][0]["embedding"]
    return llm.create_embedding(text)

class MemoryProviderSingleton(AbstractSingleton):
    @abc.abstractmethod
    def add(self, data):
        pass

    @abc.abstractmethod
    def get(self, data):
        pass

    @abc.abstractmethod
    def clear(self):
        pass

    @abc.abstractmethod
    def get_relevant(self, data, num_relevant=5):
        pass

    @abc.abstractmethod
    def get_stats(self):
        pass
