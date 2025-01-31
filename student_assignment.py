from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_overlap=0)
    chunks = splitter.split_documents(docs)
    return chunks[-1]


def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    full_text = "\n".join([doc.page_content for doc in docs])
    splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=0,
        chunk_size=10,
        is_separator_regex=True,
        separators=[
            r"\n\s*第\s*[一二三四五六七八九十]{1,3}\s*章",
            r"\n第\s*\d+-?\d*\s*條"
        ]
    )
    chunks = splitter.split_text(full_text)
    return len(chunks)
