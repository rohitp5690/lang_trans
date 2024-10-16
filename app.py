import os
import streamlit as st
from dotenv import load_dotenv

st.title("Language Translater")
lang=st.selectbox("Select Language",["English","French","Spanish","Portuguese","Russian","Hindi","Hinglish"])
inputtext=st.text_input("Enter the text you want to translate")


GROQ_API_KEY=os.getenv('GROQ_API_KEY')

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

from langchain_core.prompts import ChatPromptTemplate


system_template="translate the following into {language}"
prompt=ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user","{input_text}")
    
    
])

from langchain_groq import ChatGroq
groq_model=ChatGroq(model="Gemma2-9b-It",api_key=GROQ_API_KEY)

from langchain_core.output_parsers import StrOutputParser
parser=StrOutputParser()

chain=prompt|groq_model|parser
result=chain.invoke({"input_text":inputtext,"language":lang})
st.write(result)













