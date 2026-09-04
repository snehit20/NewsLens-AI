import streamlit as st
from sample import build_chain   # replace with your filename

st.set_page_config(
    page_title="NewsLens AI",
    page_icon="📰",
    layout="wide"
)

st.title("NewsLens AI")
st.caption("Research any news topic using RAG")

# Store chain between reruns
if "chain" not in st.session_state:
    st.session_state.chain = None

topic = st.text_input(
    "Enter a news topic",
    placeholder="AI healthcare"
)

if st.button("Load News"):
    if topic:
        with st.spinner("Loading articles and building knowledge base... This may take a few seconds to a minute. Please wait."):
            st.session_state.chain = build_chain(topic)

        st.success(f"Loaded news for: {topic}")

if st.session_state.chain is not None:

    question = st.chat_input("Ask about the news...")

    if question:
        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = st.session_state.chain.invoke(question)

            st.write(answer)
