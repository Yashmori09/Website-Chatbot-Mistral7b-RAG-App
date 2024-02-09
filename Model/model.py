import logging
import sys
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
import torch
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import ServiceContext, set_global_service_context




class Model:
    def __init__(self):
        pass

    def load_model(self):

        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
        documents = SimpleDirectoryReader(r"D:\Website-Chatbot-Mistral7b-RAG-App\artifacts/").load_data()


        llm = LlamaCPP(
            # You can pass in the URL to a GGML model to download it automatically
            model_url='https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf',
            # optionally, you can set the path to a pre-downloaded model instead of model_url
            model_path=None,
            temperature=0.1,
            max_new_tokens=256,
            
            context_window=3900,
            # kwargs to pass to __call__()
            generate_kwargs={},
            # kwargs to pass to __init__()
            # set to at least 1 to use GPU
            model_kwargs={"n_gpu_layers": -1},

            messages_to_prompt=messages_to_prompt,
            completion_to_prompt=completion_to_prompt,
            verbose=True,
        )
        embed_model = HuggingFaceEmbeddings(
        model_name="thenlper/gte-large")

        service_context = ServiceContext.from_defaults(
            chunk_size=256,
            llm=llm,
            embed_model=embed_model
        )

        index = VectorStoreIndex.from_documents(documents, service_context=service_context)
        query_engine = index.as_query_engine()

        return query_engine
    

    def query_generation(self,prompt,query_engine):
        response=query_engine.query(prompt)
        return response


if __name__ == "__main__":
    model=Model()
    query_engine=model.load_model()
    response=model.query_generation("tell me about the team",query_engine)
    print(response)