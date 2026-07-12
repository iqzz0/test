import streamlit as st
import pandas as pd
import os
from PIL import Image

# Setup Halaman
st.set_page_config(
    page_title="Klasifikasi Sampah",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ Klasifikasi Sampah")
st.markdown("Hasil Inspeksi Visual dari Model Anda")

# Dictionary untuk mapping label
LABEL_MAP = {
    0: 'Recyclable',
    1: 'Electronic',
    2: 'Organic'
}

COLOR_MAP = {
    'Recyclable': 'blue',
    'Electronic': 'orange',
    'Organic': 'green',
    'Unknown': 'gray'
}

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('submission_v2_final.csv')
        # Pastikan kolom sesuai
        if 'filepath' in df.columns and 'label' in df.columns:
            # Buat mapping text
            df['predicted_text'] = df['label'].map(LABEL_MAP).fillna('Unknown')
            # Extract ID numerik untuk sorting
            df['id_num'] = df['filepath'].apply(lambda x: int(x.split('.')[0]) if str(x).split('.')[0].isdigit() else 0)
            df = df.sort_values('id_num').reset_index(drop=True)
            return df
        else:
            st.error("Kolom 'filepath' atau 'label' tidak ditemukan di CSV.")
            return None
    except Exception as e:
        st.error(f"Gagal memuat CSV: {e}")
        return None

df = load_data()

if df is not None:
    # Filter
    filter_option = st.radio(
        "Pilih Kategori:",
        ('Semua', 'Organic', 'Recyclable', 'Electronic'),
        horizontal=True
    )
    
    # Terapkan filter
    if filter_option != 'Semua':
        filtered_df = df[df['predicted_text'] == filter_option].reset_index(drop=True)
    else:
        filtered_df = df

    # Pagination
    items_per_page = 20
    total_pages = max(1, (len(filtered_df) - 1) // items_per_page + 1)
    
    # Session state untuk halaman saat ini
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 1
        
    # Reset halaman jika filter berubah
    if 'last_filter' not in st.session_state or st.session_state.last_filter != filter_option:
        st.session_state.current_page = 1
        st.session_state.last_filter = filter_option

    # Navigasi Halaman
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️ Sebelumnya", disabled=(st.session_state.current_page <= 1)):
            st.session_state.current_page -= 1
            st.rerun()
    with col2:
        st.markdown(f"<div style='text-align: center'>Halaman {st.session_state.current_page} dari {total_pages}</div>", unsafe_allow_html=True)
    with col3:
        if st.button("Selanjutnya ➡️", disabled=(st.session_state.current_page >= total_pages)):
            st.session_state.current_page += 1
            st.rerun()

    st.markdown("---")

    # Tampilkan Gambar dalam Grid (4 Kolom)
    start_idx = (st.session_state.current_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    page_df = filtered_df.iloc[start_idx:end_idx]

    cols = st.columns(4)
    for index, row in page_df.reset_index().iterrows():
        col_idx = index % 4
        with cols[col_idx]:
            img_path = os.path.join('test', str(row['filepath']))
            
            # Label & Status
            pred_text = row['predicted_text']
            color = COLOR_MAP.get(pred_text, 'gray')
            
            # Card UI
            with st.container(border=True):
                if os.path.exists(img_path):
                    image = Image.open(img_path)
                    # PERUBAHAN DI SINI: Mengganti use_container_width=True dengan width="stretch"
                    st.image(image, width="stretch")
                else:
                    st.warning(f"Gambar tidak ditemukan")
                    
                st.markdown(f"**ID:** {row['filepath']}")
                st.markdown(f"**Prediksi:** :{color}[{pred_text}]")
                st.caption(f"Label Model: {row['label']}")

else:
    st.info("Pastikan file 'submission_v2_final.csv' dan folder 'test' berada di direktori yang sama dengan script ini.")            df['predicted_text'] = df['label'].map(LABEL_MAP).fillna('Unknown')
            # Extract ID numerik untuk sorting
            df['id_num'] = df['filepath'].apply(lambda x: int(x.split('.')[0]) if str(x).split('.')[0].isdigit() else 0)
            df = df.sort_values('id_num').reset_index(drop=True)
            return df
        else:
            st.error("Kolom 'filepath' atau 'label' tidak ditemukan di CSV.")
            return None
    except Exception as e:
        st.error(f"Gagal memuat CSV: {e}")
        return None

df = load_data()

if df is not None:
    # Filter
    filter_option = st.radio(
        "Pilih Kategori:",
        ('Semua', 'Organic', 'Recyclable', 'Electronic'),
        horizontal=True
    )
    
    # Terapkan filter
    if filter_option != 'Semua':
        filtered_df = df[df['predicted_text'] == filter_option].reset_index(drop=True)
    else:
        filtered_df = df

    # Pagination
    items_per_page = 20
    total_pages = max(1, (len(filtered_df) - 1) // items_per_page + 1)
    
    # Session state untuk halaman saat ini
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 1
        
    # Reset halaman jika filter berubah
    if 'last_filter' not in st.session_state or st.session_state.last_filter != filter_option:
        st.session_state.current_page = 1
        st.session_state.last_filter = filter_option

    # Navigasi Halaman
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️ Sebelumnya", disabled=(st.session_state.current_page <= 1)):
            st.session_state.current_page -= 1
            st.rerun()
    with col2:
        st.markdown(f"<div style='text-align: center'>Halaman {st.session_state.current_page} dari {total_pages}</div>", unsafe_allow_html=True)
    with col3:
        if st.button("Selanjutnya ➡️", disabled=(st.session_state.current_page >= total_pages)):
            st.session_state.current_page += 1
            st.rerun()

    st.markdown("---")

    # Tampilkan Gambar dalam Grid (4 Kolom)
    start_idx = (st.session_state.current_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    page_df = filtered_df.iloc[start_idx:end_idx]

    cols = st.columns(4)
    for index, row in page_df.reset_index().iterrows():
        col_idx = index % 4
        with cols[col_idx]:
            img_path = os.path.join('test', str(row['filepath']))
            
            # Label & Status
            pred_text = row['predicted_text']
            color = COLOR_MAP.get(pred_text, 'gray')
            
            # Card UI
            with st.container(border=True):
                if os.path.exists(img_path):
                    image = Image.open(img_path)
                    st.image(image, use_container_width=True)
                else:
                    st.warning(f"Gambar tidak ditemukan")
                    
                st.markdown(f"**ID:** {row['filepath']}")
                st.markdown(f"**Prediksi:** :{color}[{pred_text}]")
                st.caption(f"Label Model: {row['label']}")

else:
    st.info("Pastikan file 'submission_v2_final.csv' dan folder 'test' berada di direktori yang sama dengan script ini.")
