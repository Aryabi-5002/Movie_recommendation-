import streamlit as st
import pandas as pd
import pickle
from model import recommend
from preprocessing import Final_movie


st.markdown(
    """
    <style>
    .stApp {
    background-color: white;
    color: red;
}

    </style>
    """,
    unsafe_allow_html=True
)



st.title("Movie Recommendation System")
movies_dict=pickle.load(open("../Raw_data/movies_dict.pkl","rb"))
movies=pd.DataFrame(movies_dict)

selected=st.selectbox("Which type of movie do you like?",movies['title'].values)


st.markdown("""
<style>
.card {
    background-color: #1c1c1c;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 250px;
    border: 1px solid rgba(255,255,255,0.1);
    overflow: hidden

}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.6);
}

.card-title {
    font-size: 18px;
    font-weight: 600;
    color: #E50914; 
    margin-bottom: 10px;
}

.card-desc {
    font-size: 14px;
    color: #cfcfcf;
    line-height: 1.4;
            display: -webkit-box;
    -webkit-line-clamp: 5;      /* number of lines */
    -webkit-box-orient: vertical;

    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)
if st.button("Recommend"):

    titles, tags = recommend(selected)

    cols = st.columns(5)
    for col, title, tag in zip(cols, titles, tags):
     with col:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-desc">{" ".join(tag)[:80]}...</div>
        </div>
        """, unsafe_allow_html=True)



