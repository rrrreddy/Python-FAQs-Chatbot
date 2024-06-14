import streamlit as st
import Rag

# Set the page configuration
st.set_page_config(
    page_title="Python FAQs Q&A App",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .description {
            font-size: 1.2em;
            color: #555555;
            text-align: center;
        }
        .stTextInput > label {
            font-size: 1.2em;
            font-weight: bold;
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
        .main-content {
            padding-bottom: 70px; /* Space for the footer */
        }
    </style>
    """, unsafe_allow_html=True)

# Main content
st.markdown('<div class="title">Python FAQs Question Answering App</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="description">
        Enter your question about Python and get an instant answer! The chatbot is trained on data from the 
        <a href="https://docs.python.org/3/faq/index.html" target="_blank">Python FAQs</a>.
    </div>
    """, unsafe_allow_html=True)

# Container for main content to avoid footer overlap
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Input for user query
query = st.text_input("Enter your question:")

# Display answer if a query is provided
if query:
    answer = Rag.rag_chain.invoke(query)
    st.markdown("### Answer")
    st.write(answer)
else:
    st.markdown("Please enter a question to get an answer.")

# Close the main content container
st.markdown('</div>', unsafe_allow_html=True)

# Add a footer
st.markdown("""
    <div class="footer">
        Made with ❤️ in Python by Raghu
    </div>
""", unsafe_allow_html=True)
