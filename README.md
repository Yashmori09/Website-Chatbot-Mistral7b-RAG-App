# Website-Chatbot-Mistral7b-RAG-App
## Mistral7b
The Mistral-7B-Instruct-v0.1 Large Language Model (LLM) is a instruct fine-tuned version of the Mistral-7B-v0.1 generative text model using a variety of publicly available conversation datasets.

# How to run the Mistral-7b on Colab ?
```bash
upload the Mistral7llamai.ipynb file on your colab which is located in the <research> folder .
```
```bash
create a folder named "data" and upload your text file in that folder.
```
```bash
Thats it! Run all the cell and get your answer.
```

# How to run the Chatbot on your local system?
### STEPS:

Clone the repository

```bash
https://github.com/Yashmori09/Website-Chatbot-Mistral7b-RAG-App.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
python -m venv <folder path> <virtual env name>
```

```bash
<virtual env name>\Scripts\activate.bat
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
streamlit run app.py
```

Now,
```bash
open up you local host and port
```