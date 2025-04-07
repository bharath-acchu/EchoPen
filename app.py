import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

import streamlit as st # type: ignore


## Function to get response from LLAMA 2 Model
def getLlamaResponse(input_text, no_words, category):
    llm = CTransformers(model = 'models/llama-2-7b-chat.Q4_K_M.gguf',
                        model_type = 'llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})
    print('llm loaded')
    ## PromptTemplate
    template = """Write a  {category} on {input_text} in less than {no_words} words as a helpful, respectful and honest assistantas """

    prompt = PromptTemplate(input_variables = ["input_text", "no_words", "category"],
                            template = template)
    
    print('promt is ready')

    print('waiting to genrate resp')
    ## Generate the reponse from the LLama 2 Model
    respone = llm(prompt.format(category=category,input_text=input_text,no_words=no_words))

    print(respone)
    return respone



st.set_page_config(page_title = "EchoPen",
                    layout='centered',
                    initial_sidebar_state = "collapsed")

st.header("Create your creative writing ✍️")

input_text = st.text_input("Enter the topic you want to write about")

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of words')
with col2:
    category = st.selectbox("category",
                              ('Essays', 'Poem', 'Joke', 'Blog'),
                              index=0)
    
submit = st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, no_words, category))
