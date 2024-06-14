import streamlit as st
import Rag

# Set the page configuration
st.set_page_config(
    page_title="Python FAQs Q&A App",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add a title and description
st.title("Python FAQs Question Answering App")
st.markdown("""
<style>
    .stTitle {
        font-size: 3em;
        font-weight: bold;
        color: #4CAF50;
    }
    .stMarkdown {
        font-size: 1.2em;
        color: #555555;
    }
    .stTextInput > label {
        font-size: 1.2em;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)
st.markdown("Enter your question about Python and get an instant answer! the chatbot is trained on from the [python faq's](https://docs.python.org/3/faq/index.html).")

# Input for user query
query = st.text_input("Enter your question:")

# Display answer if a query is provided
if query:
    answer = Rag.rag_chain.invoke(query)
    st.markdown("### Answer")
    st.write(answer)
else:
    st.markdown("Please enter a question to get an answer.")

# Add a footer
st.markdown("""
    <style>
        footer {
            visibility: hidden;
        }
        .footer {
            visibility: visible;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 1em;
            color: #555555;
        }
    </style>
    <div class="footer">
        Made with ❤️ on python by Raghu
    </div>
""", unsafe_allow_html=True)
