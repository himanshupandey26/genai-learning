# from dotenv import load_dotenv

# import tomllib  # Python 3.11+; if older, pip install toml and use "import toml as tomllib"


import os
import streamlit as st

# import google.generativeai as genai #pip install google-generativeai``

# Load the .env file
# load_dotenv()
# Access environment variables
# google_api_key = os.getenv("GOOGLE_API_KEY")


# # Load config.toml
# with open("config.toml", "rb") as f:
#     config = tomllib.load(f)
# google_api_key = config["google"]["GOOGLE_API_KEY"]


from google import genai
from google.genai import types


# st.title('Language Translation')
st.title('Text Summarizer & Sentiment Analyzer')


# os.environ['GOOGLE_API_KEY'] = google_api_key
# genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
# client = genai.Client(api_key=os.environ['GOOGLE_API_KEY'])

# Access secrets safely
google_api_key = st.secrets["google"]["GOOGLE_API_KEY"]
model_name = st.secrets["google"]["model"]

client = genai.Client(api_key=google_api_key)


# * Gemini API ke client.models.list() output. 😎 Yeh basically saare available Google Gemini aur allied models dikhata hai 
# models_names = ""
# for m in client.models.list():
#     models_names = models_names  + ", " + m.name
# st.write(models_names)

user_input = st.text_area("Enter your content")


# * Directly response ke time per kar lete hai
# model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-1.0-pro')
# model = genai.GenerativeModel('gemini-1.5-pro-latest')


if st.button('Start Summary') :
    # Summarize prompt
    prompt1 = f"""
        You are an expert linguist, who is good at summarizing the content.
        Help me summarizing the content into 2 lines.
        ```
        {user_input}
        ```
        """
    
    # response1 = model.generate_content(prompt1)
    resp1 = client.models.generate_content(
        # model="gemini-2.5-flash",
        # model="models/gemini-2.0-flash-001",
        model=model_name,
        contents=prompt1
    )

    # Sentiment analysis prompt : # You need to analyze the sentiment of provided text as positive/negative.
    prompt2 = f"""
        Analyse the sentiment (Positive / Negative) of the following summary:

        ```
        {resp1.text} # This is the summary
        ```
    """

    # response2 = model.generate_content(prompt2)
    resp2 = client.models.generate_content(
        # model="google-2.5-flash",
        # model="models/gemini-2.0-flash-001",
        model=model_name,
        contents=prompt2
    )


    st.success(f"Summary: {resp1.text}")
    st.success(f"Sentiment: {resp2.text}")