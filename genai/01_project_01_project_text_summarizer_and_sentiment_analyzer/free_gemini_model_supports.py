import google.genai as genai
from google.genai import types

# # 🔑 your API key

# # ✅ Create client

client = genai.Client(api_key="YOUR_API_KEY_HERE")


# Get all available models for your key
models = list(client.models.list())

# Group models based on their type name
text_models = [m.name for m in models if "gemini" in m.name and "flash" in m.name]
pro_models = [m.name for m in models if "gemini" in m.name and "pro" in m.name]
embedding_models = [m.name for m in models if "embedding" in m.name]
image_models = [m.name for m in models if "imagen" in m.name]
audio_models = [m.name for m in models if "audio" in m.name or "tts" in m.name]

# 🧩 Display nicely
print("\n🧠 TEXT / CHAT MODELS (Free tier recommended):")
for name in text_models:
    print("  •", name)

print("\n💪 PRO / ADVANCED MODELS (might require billing):")
for name in pro_models:
    print("  •", name)

print("\n📊 EMBEDDING MODELS:")
for name in embedding_models:
    print("  •", name)

print("\n🎨 IMAGE GENERATION MODELS:")
for name in image_models:
    print("  •", name)

print("\n🎧 AUDIO / SPEECH MODELS:")
for name in audio_models:
    print("  •", name)

# 🧾 Optional count
print(f"\n✅ Total models visible to your API key: {len(models)}")
