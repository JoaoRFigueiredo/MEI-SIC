import streamlit as st
import psycopg2
import requests



def main():
    st.markdown("<h1 style='text-align: center;'>Recommendations</h1>", unsafe_allow_html=True)
    photos = [
        {"url": "./imagem.jpg", "caption": "Gostei"},
        {"url": "./imagem.jpg", "caption": "Gostei"},
        {"url": "./imagem.jpg", "caption": "Gostei"},
        {"url": "./imagem.jpg", "caption": "Gostei"},
        {"url": "./imagem.jpg", "caption": "Gostei"}
    ]
    # Display photos horizontally
    col1, col2, col3, col4, col5 = st.columns(5)

    for i, photo in enumerate(photos):
        with locals()[f"col{i+1}"]:
            st.image(photo["url"], use_column_width=True)
            st.write(photo["caption"])
    


if __name__ == "__main__":
    main()
