import abc
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


class Singleton(abc.ABCMeta, type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method for the singleton metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class AbstractSingleton(abc.ABC, metaclass=Singleton):
    pass


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self):
        """Initialize the Config class"""
        self.debug = True
        self.continuous_mode = False
        self.speak_mode = False

        self.ai_settings_file = os.getenv("AI_SETTINGS_FILE")
        self.fast_llm_model = os.getenv("FAST_LLM_MODEL")
        self.smart_llm_model = os.getenv("SMART_LLM_MODEL")
        self.fast_token_limit = int(os.getenv("FAST_TOKEN_LIMIT", 1500))
        self.smart_token_limit = int(os.getenv("SMART_TOKEN_LIMIT", 2000))

        self.gpu_layers = int(os.getenv("GPU_LAYERS"))

        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

        self.use_mac_os_tts = False
        self.use_mac_os_tts = os.getenv("USE_MAC_OS_TTS")
        
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.custom_search_engine_id = os.getenv("CUSTOM_SEARCH_ENGINE_ID")

        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_region = os.getenv("PINECONE_ENV")

        self.image_provider = os.getenv("IMAGE_PROVIDER")
        self.huggingface_api_token = os.getenv("HUGGINGFACE_API_TOKEN")

        # User agent headers to use when browsing web
        # Some websites might just completely deny request with an error code if no user agent was found.
        self.user_agent_header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        self.redis_host = os.getenv("REDIS_HOST", "localhost")
        self.redis_port = os.getenv("REDIS_PORT", "6379")
        self.redis_password = os.getenv("REDIS_PASSWORD", "")
        self.wipe_redis_on_start = os.getenv("WIPE_REDIS_ON_START", "True") == 'True'
        self.memory_index = os.getenv("MEMORY_INDEX", 'auto-gpt')
        # Note that indexes must be created on db 0 in redis, this is not configureable.
        self.memory_backend = os.getenv("MEMORY_BACKEND", 'local')

        self.EMBED_DIM = int(os.getenv("EMBED_DIM"))
        
        self.temperature = float(os.getenv("TEMPERATURE"))

    def set_ai_settings_file(self, value: str):
        self.ai_settings_file = value

    def set_temperature(self, value: float):
        self.temperature = value

    def set_continuous_mode(self, value: bool):
        """Set the continuous mode value."""
        self.continuous_mode = value

    def set_speak_mode(self, value: bool):
        """Set the speak mode value."""
        self.speak_mode = value

    def set_debug_mode(self, value: bool):
        self.debug_mode = value

    def set_fast_llm_model(self, value: str):
        """Set the fast LLM model value."""
        self.fast_llm_model = value

    def set_smart_llm_model(self, value: str):
        """Set the smart LLM model value."""
        self.smart_llm_model = value

    def set_fast_token_limit(self, value: int):
        """Set the fast token limit value."""
        self.fast_token_limit = value

    def set_smart_token_limit(self, value: int):
        """Set the smart token limit value."""
        self.smart_token_limit = value

    def set_elevenlabs_api_key(self, value: str):
        """Set the ElevenLabs API key value."""
        self.elevenlabs_api_key = value

    def set_google_api_key(self, value: str):
        """Set the Google API key value."""
        self.google_api_key = value

    def set_custom_search_engine_id(self, value: str):
        """Set the custom search engine id value."""
        self.custom_search_engine_id = value

    def set_pinecone_api_key(self, value: str):
        """Set the Pinecone API key value."""
        self.pinecone_api_key = value

    def set_pinecone_region(self, value: str):
        """Set the Pinecone region value."""
        self.pinecone_region = value

    def set_debug_mode(self, value: bool):
        """Set the debug mode value."""
        self.debug = value
