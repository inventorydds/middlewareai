import streamlit as st
import chromadb

st.set_page_config(page_title="Streamlit + ChromaDB", layout="centered")

st.title("🔍 Streamlit + ChromaDB")

if st.button("Run Chroma Query"):
    try:
        client = chromadb.HttpClient(host="chromadb", port=8000)
        st.success("Connected to ChromaDB")

        collection = client.get_or_create_collection("my_collection")
        collection.add(documents=["Hello from Chroma!"], ids=["doc1"])
        result = collection.query(query_texts=["hello"], n_results=1)

        st.write("### Query Result")
        st.json(result)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
