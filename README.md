# Python FAQs Question Answering App

This repository contains the implementation of a Question Answering (QA) app built using Retrieval Augmented Generation (RAG) techniques. The app leverages Large Language Model `mistralai/Mistral-7B-Instruct-v0.3` to answer questions about Python FAQs by retrieving and utilizing relevant data from `https://docs.python.org/3/faq/index.html`.

## Table of Contents
- [Introduction to RAG](#introduction-to-rag)
- [Purpose of RAG](#purpose-of-rag)
- [Components of a RAG Application](#components-of-a-rag-application)
- [Workflow of a RAG Application](#workflow-of-a-rag-application)
- [Tools and Technologies](#tools-and-technologies)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Example Application Workflow](#example-application-workflow)
- [Advanced Techniques and Resources](#advanced-techniques-and-resources)

## Introduction to RAG

**Retrieval Augmented Generation (RAG)** is a technique for building sophisticated question-answering (Q&A) applications using Large Language Models (LLMs). These applications enhance the capabilities of LLMs by augmenting them with additional, relevant data.

## Purpose of RAG
- **Enhancing LLMs**: Integrates private or recent data to improve the model's reasoning ability.
- **Application**: Used to create Q&A chatbots for specific data sources.

## Components of a RAG Application
1. **Indexing**
   - **Loading Data**: Ingesting data using DocumentLoaders.
   - **Splitting Text**: Breaking large documents into smaller chunks using text splitters.
   - **Storing Data**: Indexing and storing text chunks using a VectorStore and an Embeddings model.

2. **Retrieval and Generation**
   - **Retrieving Data**: Using a Retriever to fetch relevant data chunks based on user queries.
   - **Generating Answers**: Using a ChatModel or LLM to produce answers by combining user queries with retrieved data.

## Workflow of a RAG Application
1. **Indexing Phase**
   - **Load**: Import data using DocumentLoaders.
   - **Split**: Use text splitters to divide large documents.
   - **Store**: Index and store chunks in a VectorStore.
   ![Indexing Diagram](https://python.langchain.com/v0.2/assets/images/rag_indexing-8160f90a90a33253d0154659cf7d453f.png)

2. **Retrieval and Generation Phase**
   - **Retrieve**: Retrieve relevant chunks based on user queries.
   - **Generate**: Use retrieved data and user queries to generate answers.
   ![Retrieval and Generation Diagram](https://python.langchain.com/v0.2/assets/images/rag_retrieval_generation-1046a4668d6bb08786ef73c56d4f228a.png)

## Tools and Technologies
- **LangChain**: Components for building Q&A applications.
- **DocumentLoaders**: For loading data.
- **Text Splitters**: For breaking down documents.
- **VectorStore**: For storing and indexing data chunks.
- **Embeddings Model**: For creating searchable vector representations.
- **Retriever**: For fetching relevant data chunks.
- **ChatModel/LLM**: For generating answers.

## Installation and Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/python-faqs-qa-app.git
    cd python-faqs-qa-app
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    Create a `.env` file in the root directory and add your API keys:
    ```bash
    LANGCHAIN_API_KEY=your_langchain_api_key
    HUGGINGFACEHUB_API_TOKEN=your_huggingfacehub_api_token
    ```

## Running the Application

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to `http://localhost:8501` to use the app.

## Example Application Workflow

1. **Data Ingestion**: Load a large text document using DocumentLoaders.
2. **Data Preparation**: Split the document into smaller chunks with text splitters.
3. **Data Indexing**: Store chunks in a VectorStore.
4. **Query Processing**:
   - The Retriever searches the VectorStore for relevant data chunks based on user queries.
   - Retrieved data and user queries are used by the LLM to generate answers.

## Advanced Techniques and Resources

- **LangSmith**: Tool for tracing and understanding the application.
- **RAG over Structured Data**: Applying RAG to structured data like SQL databases using LangChain.

---

Made with ❤️ on python by Raghu
