import os
import streamlit as st
from dotenv import load_dotenv

st.title("Language Translater")
lang=st.selectbox("Select Language",["English","French","Spanish","Portuguese","Russian","Hindi","Hinglish"])
inputtext=st.text_input("Enter the text you want to translate")


OPEN_API_KEY='sk-7swPgmf6mk37rBdEhQlVwmlk2LSW7ZoRB9WXUQoq7IT3BlbkFJjUYPvgxdvB80PAlDVbfMWSjcfQ-duJiFtGsGJou2MA'
LANGCHAIN_API_KEY='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'
LANGCHAIN_PROJECT='GENAI_APP_PROJECT1'
HF_Token='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'
GROQ_API_KEY='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'


os.environ['LANGCHAIN_API_KEY'] = LANGCHAIN_API_KEY
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT'] = LANGCHAIN_PROJECT

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













