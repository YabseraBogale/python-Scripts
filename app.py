#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:19:07 2022
file of work
@author: yabsera
"""
import pandas as pd
import plotly.express as pt
import streamlit as st
st.set_page_config(
        page_title="Probablity Assigment",
        page_icon=":bar_chart:",
        layout="wide"
        )
df = pd.read_excel(
        io="member2.xlsx",
        engine='openpyxl',
        usecols="A:N"
        )

st.sidebar.header("please filter here: ")
zone=st.sidebar.multiselect(
        "select ዞን:",
        options=df['ዞን'].unique(),
        default=df['ዞን'].unique()
        )
filed=st.sidebar.multiselect(
        "select የተሰማራበት ዘርፍ :",
        options=df['ዘርፍ'].unique(),
        default=df['ዘርፍ'].unique()
        )
df_sel=df.query(
            "ዞን==@zone & ዘርፍ==@filed"
        )

st.title(":bar_chart: sales dash borad")
st.markdown("##")
total_sales=int(df_sel["ወቅታዊ ጠቅላላ ሃብት"].sum())
sales_mean=round(df_sel["ወቅታዊ ጠቅላላ ሃብት"].mean(),2)
ave_rating=round(df_sel["ወቅታዊ የአባላት ብዛት"].mean(),1)
star_rating=":star:"*round(int(ave_rating),0)
left_col,mid_col,right_col=st.columns(3)
with left_col:
    st.subheader("Totale sales:")
    st.subheader(f"Ethio birr {total_sales:,}")
with mid_col:
    st.subheader("Average Rating:")
    st.subheader(f"Rating {ave_rating}, {star_rating}")
with right_col:
    st.subheader("Average transcation:")
    st.subheader(f"{sales_mean}")
st.markdown("----")

