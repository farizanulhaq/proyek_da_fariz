import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')
all_df = pd.merge(day_df, hour_df, on='dteday', how='left')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
all_df['dteday'] = pd.to_datetime(all_df['dteday'])

st.title('Proyek Data Analyst Fariz')

st.header('Pengaruh Cuaca dan Musim terhadap Penyewaan Sepeda')
faktor_cuaca = all_df.groupby(by=['season_x', 'weathersit_x']).agg({
    'cnt_x': 'sum'
}).reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='season_x', y='cnt_x', hue='weathersit_x', data=faktor_cuaca, ax=ax)
plt.title('Pengaruh Cuaca dan Musim terhadap Penyewaan Sepeda')
plt.xlabel('Musim (1: Semi, 2: Panas, 3: Gugur, 4: Salju)')
plt.ylabel('Total Rentals')
plt.legend(title='Keadaan Cuaca (1: Cerah, 2: Kabut, 3: Hujan/Salju Berat)')
st.pyplot(fig)

st.header('Pengaruh Hari Libur terhadap Pola Penyewaan Sepeda')
faktor_libur = all_df.groupby(by=['holiday_x']).agg({
    'cnt_x': ['mean', 'std']
})
fig, ax = plt.subplots(figsize=(8, 6))
faktor_libur.plot(kind='bar', y='cnt_x', ax=ax)
plt.title('Pengaruh Hari Libur terhadap Pola Penyewaan Sepeda')
plt.xlabel('Hari Libur (0: No, 1: Yes)')
plt.ylabel('Average Rentals')
plt.legend(['Mean', 'Standard Deviation'])
st.pyplot(fig)