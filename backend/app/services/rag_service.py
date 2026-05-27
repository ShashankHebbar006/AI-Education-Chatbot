
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

faq_text = '''
Course enrollment opens every Monday.
Payments can be made using UPI, cards, and net banking.
Technical issues should be reported through support tickets.
Certificates are issued after successful course completion.
'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_text(faq_text)

documents = [Document(page_content=chunk) for chunk in chunks]

vector_store = FAISS.from_documents(
    documents,
    embedding_model
)

retriever = vector_store.as_retriever()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY")
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

def generate_response(user_query: str):
    result = qa_chain.invoke(user_query)
    return result["result"]
