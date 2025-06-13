
import streamlit as st

st.set_page_config(page_title="Noise Filter App 🎧", page_icon="🎧")

st.title("Noise Filter App")
st.write(
    """
Welcome to **Noise Filter App** – a simple Streamlit tool that removes background noise from your WAV recordings.

**How to use**  
1. Head to the **New Journey** page to upload a noisy `.wav` file.  
2. Wait a few seconds while the app applies spectral‑gating noise reduction.  
3. Jump to **Filtered Output** to compare waveforms, listen, and download the cleaned file.
    """
)

st.info("Ready to begin? Click **New Journey** in the sidebar 👉")
