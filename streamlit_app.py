import streamlit as st
import openai
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")


def detect_gpt3(prompt):
    generated_text = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    prompt_prob = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        log_probs=True
    ).log_probs

    generated_text_prob = openai.Completion.create(
        engine="text-davinci-002",
        prompt=generated_text,
        log_probs=True
    ).log_probs

    return prompt_prob, generated_text_prob

st.title("GPT-3 Text Detection App")

text = st.text_area("Enter text to check if generated by GPT-3:")

if st.button("Check"):
    prompt_prob, generated_text_prob = detect_gpt3(text)
    if abs(prompt_prob - generated_text_prob) < 0.05:
        st.success("The text is generated by GPT-3")
    else:
        st.error("The text is not generated by GPT-3")
