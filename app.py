import streamlit as st
from generate_workflow import generate_workflow

def main():
    st.title("Multi-Agent Blog Writer")
    st.markdown("This app generates a multi-agent workflow for creating content.")

    # Input topic
    topic = st.text_input("Enter the topic you want to generate content about:", "Artificial Intelligence")

    # Input tone
    tone_options = ["Formal", "Informal"]
    tone = st.selectbox("Select the tone of the blog:", tone_options)

    # Input word count
    word_count = st.number_input("Enter the desired number of words for the blog:", min_value=100, step=100, value=500)

    # Generate content workflow
    if st.button("Generate Workflow"):
        result = generate_workflow(topic, tone, word_count)
        st.markdown(result)

if __name__ == "__main__":
    main()
