import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')
all_df = pd.merge(day_df, hour_df, on='dteday', how='left')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
all_df['dteday'] = pd.to_datetime(all_df['dteday'])

st.sidebar.title('Pilih Analisis')
analisis = st.sidebar.radio('Pilih topik analisis:', ['Pengaruh Cuaca dan Musim', 'Pengaruh Hari Libur'])

bulan = st.sidebar.selectbox('Pilih Bulan:', 
                             ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 
                              'September', 'Oktober', 'November', 'Desember'])

tahun = st.sidebar.selectbox('Pilih Tahun:', [2011, 2012])

bulan_mapping = {
    'Januari': 1, 'Februari': 2, 'Maret': 3, 'April': 4, 'Mei': 5, 'Juni': 6,
    'Juli': 7, 'Agustus': 8, 'September': 9, 'Oktober': 10, 'November': 11, 'Desember': 12
}

selected_month = bulan_mapping[bulan]
filtered_df = all_df[(all_df['dteday'].dt.year == tahun) & (all_df['dteday'].dt.month == selected_month)]

st.title('Proyek Data Analyst Fariz')

if analisis == 'Pengaruh Cuaca dan Musim':
    st.header('Pengaruh Cuaca dan Musim terhadap Penyewaan Sepeda')
    faktor_cuaca = filtered_df.groupby(by=['season_x', 'weathersit_x']).agg({
        'cnt_x': 'sum'
    }).reset_index()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='season_x', y='cnt_x', hue='weathersit_x', data=faktor_cuaca, ax=ax)
    ax.set_title(f'Pengaruh Cuaca dan Musim terhadap Penyewaan Sepeda - {bulan} {tahun}')
    ax.set_xlabel('Musim (1: Semi, 2: Panas, 3: Gugur, 4: Salju)')
    ax.set_ylabel('Total Rentals')
    ax.legend(title='Keadaan Cuaca (1: Cerah, 2: Kabut, 3: Hujan/Salju Berat)')
    
    st.pyplot(fig)

elif analisis == 'Pengaruh Hari Libur':
    st.header('Pengaruh Hari Libur terhadap Pola Penyewaan Sepeda')
    faktor_libur = filtered_df.groupby(by=['holiday_x']).agg({
        'cnt_x': ['mean', 'std']
    })
    
    fig, ax = plt.subplots(figsize=(8, 6))
    faktor_libur.plot(kind='bar', y='cnt_x', ax=ax)
    ax.set_title(f'Pengaruh Hari Libur terhadap Pola Penyewaan Sepeda - {bulan} {tahun}')
    ax.set_xlabel('Hari Libur (0: No, 1: Yes)')
    ax.set_ylabel('Average Rentals')
    ax.legend(['Mean', 'Standard Deviation'])
    
    st.pyplot(fig)
    
# Saya taruh di doc root karena tidak terbaca jika di masukan dalam folder dashboard setelah saya membaca doc streamlit
