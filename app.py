# import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from flask import Flask, request,jsonify
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()


app=Flask(__name__)

def main():
    print("this is running")
    # st.write("chat with pdf")

@app.route("/read-pdf", methods=["POST"])
def readPdf():
    print("came to api")
    pdf=request.files["file"]
    print(f"printing pdf {pdf}")
    # print(pdf["file"])
    if pdf is not None:
        pdf_reader =PdfReader(pdf[0]) 
        
        text=""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
        print(f"text splitter {text_splitter}")
if __name__== '__main__':
    print("came to main")
    app.run(host="0.0.0.0", port=5000, debug=True)
    main()