"""
Multimodal Market Analysis & Sentiment Engine (Day 11 Update)
-----------------------------------------------------------
This module uses Gemini's gemini-embedding-2-preview to analyze 
multimodal market data (Menu Images, Social Media, Reviews).

These embeddings are used to:
1. Extract pricing trends and menu density from restaurant images.
2. Group competitors based on visual and textual brand sentiment.
3. Map consumer "vibes" from social media audio/video clips.
"""

from google import genai
from google.genai import types
import os

class MarketMultimodalEngine:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=self.api_key)

    def embed_market_data(self, consumer_review=None, image_path=None, audio_path=None):
        """
        Embeds market-related multimodal data.
        """
        contents = []
        
        if consumer_review:
            contents.append(consumer_review)
        
        if image_path and os.path.exists(image_path):
            with open(image_path, "rb") as f:
                image_bytes = f.read()
                contents.append(types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png"
                ))

        if audio_path and os.path.exists(audio_path):
            with open(audio_path, "rb") as f:
                audio_bytes = f.read()
                contents.append(types.Part.from_bytes(
                    data=audio_bytes,
                    mime_type="audio/mpeg"
                ))

        if not contents:
            raise ValueError("No content provided for embedding.")

        result = self.client.models.embed_content(
            model="gemini-embedding-2-preview",
            contents=contents,
        )
        return result.embeddings

if __name__ == "__main__":
    print("Initializing Market Multimodal Engine (Day 11)...")
    print("Model: gemini-embedding-2-preview integrated for Visual & Textual Brand Analysis.")
