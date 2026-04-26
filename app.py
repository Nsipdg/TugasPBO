import streamlit as st
import pandas as pd
import numpy as np

class AnalisisCitraApp:
    def __init__(self):
        self.config_page()
        # Simulasi data performa (KPI & Tren)
        self.data = pd.DataFrame({
            'Detik': np.arange(1, 21),
            'Akurasi': np.random.uniform(0.8, 0.98, 20),
            'Objek_Terdeteksi': np.random.randint(5, 25, 20)
        })

    def config_page(self):
        st.set_page_config(page_title="Dashboard Analisis PBO", layout="wide")
        st.sidebar.title("Navigasi")

    def render_header(self):
        st.title("📊 Sistem Monitoring Performa Citra")
        st.info("Aplikasi ini dibangun menggunakan prinsip Pemrograman Berbasis Objek (OOP).")

    def render_metrics(self):
        st.subheader("Key Performance Indicators")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Rata-rata Akurasi", f"{self.data['Akurasi'].mean():.2%}")
        with c2:
            st.metric("Total Objek", self.data['Objek_Terdeteksi'].sum())
        with c3:
            st.metric("FPS", "30.5")

    def render_charts(self):
        tab1, tab2 = st.tabs(["📈 Tren Akurasi", "📊 Distribusi Objek"])
        with tab1:
            st.line_chart(self.data.set_index('Detik')['Akurasi'])
        with tab2:
            st.bar_chart(self.data.set_index('Detik')['Objek_Terdeteksi'])

    def run(self):
        self.render_header()
        self.render_metrics()
        self.render_charts()

if __name__ == "__main__":
    app = AnalisisCitraApp()
    app.run()
  
