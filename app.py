import streamlit as st
from crewai import Crew, Process
from pydantic import BaseModel
from agents import News_Researcher, News_Writer
from tasks import Research_task, Write_task
from tools import tool
import os

st.set_page_config(page_title="CrewAI Article Generator", page_icon="📝", layout="wide")

st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .main {
        background: #00000;
        padding: 3rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #0000;
        color: white;
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📊 API Configuration")
st.sidebar.markdown("Enter your API keys below:")

serper_api_key = st.sidebar.text_input("Serper API Key", type="password")
groq_api_key = st.sidebar.text_input("Groq API Key", type="password")

if st.sidebar.button("Save API Keys"):
    if serper_api_key and groq_api_key:
        os.environ['SERPER_API_KEY'] = serper_api_key
        os.environ['GROQ_API_KEY'] = groq_api_key
        st.sidebar.success("API keys saved successfully!")
    else:
        st.sidebar.error("Please enter both API keys.")

st.title("📝 Culprit ")
st.markdown("This is an Agent which can write articles for your blog on any Topic - Have a Try")

topic = st.text_input("Enter a topic for your article:", placeholder="e.g., Space exploration, Climate change, Artificial intelligence")

if st.button("Generate Article"):
    if not serper_api_key or not groq_api_key:
        st.error("Please enter both API keys in the sidebar before generating an article.")
    elif not topic:
        st.warning("Please enter a topic before generating the article.")
    else:
        progress_bar = st.progress(0)
        crew = Crew(
            agents=[News_Researcher, News_Writer],
            tasks=[Research_task, Write_task],
            process=Process.sequential,
        )

        with st.spinner(f"Researching and writing the article about '{topic}'..."):
            progress_bar.progress(50)
            result = crew.kickoff(inputs={'topic': topic})
        
        progress_bar.progress(100)

        st.subheader("Generated Article:")
        
        if isinstance(result, str):
            article_text = result
        elif isinstance(result, dict) and 'article' in result:
            article_text = result['article']
        else:
            article_text = str(result)  
        
        st.markdown(article_text)

        st.download_button(
            label="Download Article",
            data=article_text,
            file_name=f"{topic.replace(' ', '_').lower()}_article.txt",
            mime="text/plain"
        )

st.markdown("---------")
st.markdown("Created using CrewAI with ❤️ by BLJP ")
