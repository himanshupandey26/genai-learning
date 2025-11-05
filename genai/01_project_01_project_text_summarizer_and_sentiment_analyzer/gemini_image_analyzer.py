import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# os.environ['GOOGLE_API_KEY'] = "your_api_key"

# --- 1. API Key Configuration ---

# # Streamlit ke 'secrets' feature ka istemaal karna best practice hai.
# Pehle check karo ki key Streamlit Cloud 'secrets' mein hai
if "GOOGLE_API_KEY" in st.secrets["google"]:
    # (Production/Share ke liye) Streamlit Cloud se secret load karega
    GOOGLE_API_KEY = st.secrets["google"]["GOOGLE_API_KEY"]
else:
    # (Local testing ke liye) Local environment variable se load karega
    # .get() use karna safe hai, agar key na mile toh yeh error nahin dega
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# Ab final check karein ki key kahin se mili ya nahin
if not GOOGLE_API_KEY:
    st.error("API Key nahin mili! Please 'GOOGLE_API_KEY' ko Streamlit secrets (deployment ke liye) ya environment variable (local testing ke liye) mein set karein.")
    st.stop()


genai.configure(api_key=GOOGLE_API_KEY)


# --- 2. Model Initialization ---
# Hum 'flash' model use kar rahe hain jo vision (image) ko support karta hai
try:
    model = genai.GenerativeModel('models/gemini-2.5-flash')
except Exception as e:
    st.error(f"Model initialization mein error: {e}")
    st.stop()


# --- 3. Streamlit App UI ---
st.set_page_config(page_title="Gemini Image Analyzer", layout="centered")
st.title("🖼️ Gemini Image Analyzer")
st.write("Any image upload karein aur uske baare mein sawaal poochein.")
st.write("File support : [jpg, jpeg, png].")

# --- 4. Image Upload ---
uploaded_file = st.file_uploader("Upload your image here...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Image ko PIL format mein open karein (Gemini ke liye zaroori)
    img = Image.open(uploaded_file)
    
    # Uploaded image ko display karein
    st.image(img, caption="Your Uploaded Image", width="stretch")
    
    # --- 5. Text Prompt ---
    prompt_text = st.text_input(
        "Aap is image ke baare mein kya poochna chahte hain?", 
        value="Is picture mein kya-kya dikh raha hai? Detail mein batao." + "Reply in the same language and tone I use.If I write in English → reply fully in English.If I write in Hinglish → reply naturally in Hinglish or mixed English (not Hindi translation).Never switch to pure Hindi unless I use it first"
    )
    
    # --- 6. Process Button ---
    if st.button("Analyze Image"):
        # Button dabane par spinner (loading) dikhayein
        with st.spinner("Gemini soch raha hai... 🤖"):
            try:
                # Model ko dono cheezein (text aur image) ek saath bhejein
                # Yeh ek multimodal prompt hai
                response = model.generate_content([prompt_text, img])
                
                st.subheader("Gemini Response:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Image process karne mein error aaya: {e}")
else:
    st.info("Analyze karne ke liye please ek image upload karein.")

