#analisa pertemuan 5 tentang 5 feature addition.py

import streamlit as st
import pandas as pd

st.title("cek judul dan status data SKP")
#1.Membaca file excel
df=pd.read_excel("data_skp.xlsx")

#2.Membuat kolom status (nilai default: lulus)
df['status']='lulus'

#3. membuat kolom status _judul(cek apakah judul kosong atau ada)
df["status_judul"] = df["JUDUL"].apply(
    lambda x: "JUDUL KOSONG" if pd.isnull(x) or x==""else"ada judul"
)

#4. tampilkan isi data frame di streamlit
st.subheader("Data SKP")
st.dataframe(df)