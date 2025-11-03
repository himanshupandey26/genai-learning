import os
import streamlit as st
import google.generativeai as genai # <-- ✅ CORRECT IMPORT

# Access secrets safely
try:
    google_api_key = st.secrets["google"]["GOOGLE_API_KEY"]
    model_name = st.secrets["google"]["model"]
except KeyError as e:
    st.error(f"Secret not found: {e}. Please check your Streamlit secrets.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred loading secrets: {e}")
    st.stop()

# Configure the genai library
genai.configure(api_key=google_api_key)

# --- ✅ CORRECT SETUP ---
# Create the model instance once
try:
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Error creating model (check model name '{model_name}'): {e}")
    st.stop()
# -------------------------

st.title('Text Summarizer & Sentiment Analyzer')

user_input = st.text_area("Enter your content")

if st.button('Start Analysis'):
    if user_input:
        try:
            # --- ✅ CORRECT API CALL (1) ---
            # Summarize prompt
            prompt1 = f"""
                You are an expert linguist, who is good at summarizing the content.
                Help me summarizing the content into 2 lines.
                ```
                {user_input}
                ```
                """
            
            # Generate the summary
            resp1 = model.generate_content(prompt1)
            summary_text = resp1.text

            # --- ✅ CORRECT API CALL (2) ---
            # Sentiment analysis prompt
            prompt2 = f"""
                Analyse the sentiment (Positive / Negative) in one line of the following summary:

                ```
                {summary_text}
                ```
            """
            
            # Generate the sentiment
            resp2 = model.generate_content(prompt2)
            sentiment_text = resp2.text

            # Display results
            st.success(f"Summary: {summary_text}")
            st.success(f"Sentiment: {sentiment_text}")

        except Exception as e:
            st.error(f"An error occurred during generation: {e}")
    else:
        st.warning("Please enter some text to analyze.")