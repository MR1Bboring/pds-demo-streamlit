import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("pie chart keilmuan SKP")

#1.Membaca file excel
df=pd.read_excel("data_skp.xlsx")

#2. group berdasarkan keilmuan
grouped= df.groupby("keilmuan")["JUDUL"].count().reset_index()

labels= grouped["keilmuan"]
values = grouped["JUDUL"]

#3. plot pie chart
fig, ax = plt.subplots()
ax.pie(values, labels= labels, autopct='%1.1f%%', startangle=90)
ax.set_title("propinsi judul penelitian berdasarkan keilmuan")

#4. tampilkan di streamlit
st.pyplot(fig)

#5. tampilkan tabel datanya
st.subheader("tabel data keilmuan")
st.dataframe(grouped)
