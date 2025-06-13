import streamlit as st

# Page configuration
st.set_page_config(page_title="Sppech Preprocessing Recognition 🎧", page_icon="🎧")

# Custom CSS to make the UI green
st.markdown(
    """
    <style>
    body {
        background-color: #006400; /* Dark green */
        color: white;
    }
    .stApp {
        background-color: #006400;
    }
    .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCode, .stCaption {
        color: white !important;
    }
    .stButton>button {
        background-color: #228B22;
        color: white;
    }
    .stSidebar {
        background-color: #004d00;
        color: white;
    }
    .stSidebar .css-1d391kg, .stSidebar .css-1v3fvcr {
        color: white !important;
    }
    .css-1aumxhk {
        background-color: #006400;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App content
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
