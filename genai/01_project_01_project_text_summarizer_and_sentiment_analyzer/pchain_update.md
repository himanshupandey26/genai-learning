```python
# Old SDK (google-generativeai) = ❌ outdated syntax + errors on new models (like gemini-1.5 / 2.0).

import os
import google.generativeai as genai #pip install google-generativeai``
import streamlit as st

# st.title('Language Translation')
st.title('Text Summarizer & Sentiment Analyzer')

os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY_HERE"

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter your content")

# model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-1.0-pro')
model = genai.GenerativeModel('gemini-1.5-pro-latest')

if(st.button('Start Summary')):

    prompt1 = f"""
        You are an expert linguist, who is good at summarizing the content.
        Help me summarizing the content into 2 lines.
        ```
        {user_input}
        ```
        """
    
    response1 = model.generate_content(prompt1)

    prompt2 = f"""
        You need to analyze the sentiment of provided text as positive/negative.
        ```
        {response1} # This is the summary
        ```
    """

    response2 = model.generate_content(prompt2)

    st.success(f"Summary: {response1.text}")
    st.success(f"Sentiment: {response2.text}")




```



Good that you reached out. Yes — you’re right to suspect it: your code is using an **older** version of the SDK for google‑generativeai (i.e., `import google.generativeai as genai`) and the way it’s being used has changed now. I’ll walk you through *what’s changed*, and *what you should update* in your code — then we can tweak your code together.

---

### ✅ What changed

Here are the key updates:

1. The older library `google-generativeai` is now **deprecated**. The maintainers say you should migrate to the new unified SDK: google‑genai (`pip install google-genai`). ([GitHub][1])

2. The new SDK has a different import and initialization pattern:

   * `from google import genai` (instead of `import google.generativeai as genai`) ([googleapis.github.io][2])
   * You create a `Client` object rather than directly `GenerativeModel` in some cases. ([googleapis.github.io][2])

3. Model names / availabilities have updated: for example, older model aliases like `gemini-1.0-pro` are no longer supported. ([Google AI for Developers][3])

4. The older library may still work for *basic tasks*, but for newer features, full support, and future-proofing you should move to the new SDK. ([Google AI Developers Forum][4])

---

### 🛠 What you should change in your code

Let’s adapt your code to the new SDK (just a proposal). Then you can test and we can debug further if errors pop up.

Here’s a modified version of your code with the new SDK style:

````python
import os
import streamlit as st
from google import genai
from google.genai import types

st.title('Text Summarizer & Sentiment Analyzer')

# Set your API key
os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY_HERE"
# Or you can do: api_key = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key=os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter your content")

if st.button('Start Summary'):
    # Summarize prompt
    prompt1 = f"""
    You are an expert linguist, summarise the content into 2 lines:
    ```
    {user_input}
    ```
    """
    resp1 = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt1
    )

    summary = resp1.text

    # Sentiment analysis prompt
    prompt2 = f"""
    Analyse the sentiment (Positive / Negative) of the following summary:
    ```
    {summary}
    ```
    """
    resp2 = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt2
    )

    sentiment = resp2.text

    st.success(f"Summary: {summary}")
    st.success(f"Sentiment: {sentiment}")
````

**Changes to note:**

* Use `from google import genai` and `client = genai.Client(...)`.
* Use `client.models.generate_content(...)` instead of `model = genai.GenerativeModel(...)` and `model.generate_content(...)`.
* Pick a model name that is supported (e.g., `"gemini-2.0-flash-001"`). You’ll need to check what models your API key has access to.
* Keep your API key safe — don’t expose openly in production.
* Ensure you’ve installed the new library: `pip install google-genai`.

---

### 🤔 Some questions for you

To help fine-tune the fix, could you check/answer these:

1. What **error message** are you getting currently? (The exact traceback helps a lot.)
2. Are you using the **free tier / personal API key** for the Gemini API, or a Google Cloud Vertex AI project key?
3. Which Python version are you on (e.g., Python 3.10)?
4. Have you already installed the library `google-genai` (and uninstalled or replaced `google-generativeai`)?

---

If you like, I can **give you a ready-to-go template** (full Streamlit app) using the new SDK, that you can plug in and test. Want me to prepare that for you?

[1]: https://github.com/google-gemini/deprecated-generative-ai-python?utm_source=chatgpt.com "google-gemini/deprecated-generative-ai-python: This SDK ... - GitHub"
[2]: https://googleapis.github.io/python-genai/?utm_source=chatgpt.com "Google Gen AI SDK documentation"
[3]: https://ai.google.dev/gemini-api/docs/changelog?utm_source=chatgpt.com "Release notes | Gemini API | Google AI for Developers"
[4]: https://discuss.ai.google.dev/t/google-generativeai-vs-python-genai/53873?utm_source=chatgpt.com "Google.generativeai vs python-genai - Gemini API"
