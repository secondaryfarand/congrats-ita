import streamlit as st
from datetime import datetime
import base64 
from PIL import Image


st.set_page_config (
    page_title= "SELAMAT MENJABAT !!!", 
    page_icon= ":sparkles:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <audio controls autoplay loop style="display:none">
        <source src="data:audio/mp3;base64,{}" type="audio/mp3">
    </audio>
    """.format(base64.b64encode(open("music/background_music.mp3", "rb").read()).decode()),
    unsafe_allow_html=True,
)




st.title("Selamat Dilantik Menjadi Pimpinan, Yulita Prabawati")
st.markdown("04.35 AM - 6 th December 2025")
st.markdown("dari ...")

# st.images("images/foto.jpg", use_column_width=True)
st.write("---")

st.markdown(
    """
    Hai, per hari ini kamu dilantik sebagai pimpinan di BEM FMIPA Periode 2026, meskipun aku belum bisa membersamai secara langsung di organisasi yang sama, tapi gapapa, aku ucapin selamat yaa atas dedikasi nya selama satu tahun dan kini akan lanjut di tahun yang kedua. Semoga semua target nya tercapai, jangan lupa kompetisi kita ... 😊  
    """
)

st.write("---")


kenangan = [
    {
        "path": "images/fotbem1.jpg",
        "caption": "😍",
        "lucu": True
    },
    {
        "path": "images/fotbem2.jpg",
        "caption": " 🤣",
        "lucu": True
    },
    {
        "path": "images/fotbem3.jpg",
        "caption": " 🍕💖",
        "lucu": True
    },
    {
        "path": "images/fotbem4.jpg",
        "caption": "Dingin, tapi hatiku hangat karena ada kamu.(apasih) 🏔️🥰",
        "lucu": True
    },    
    {
        "path": "images/fotbem5.jpeg",
        "caption": "",
        "lucu": True
    },
    {
        "path": "images/fotbem6.jpg",
        "caption": "",
        "lucu": True
    }
    
]


N_COLS = 3
cols = st.columns(N_COLS)
current_col = 0 

for item in kenangan:
    with cols[current_col]:
        try:
            # Gunakan lebar kolom penuh (use_column_width=True)
            st.image(item["path"], use_container_width=True)
            
            # Keterangan (Caption)
            if item["lucu"]:
                # Style Kasual & Lucu (gunakan st.info atau st.warning untuk highlight)
                # st.info(f"**-** {item['caption']}")
                a=0
            else:
                # Style Minimalis & Elegan
                st.markdown(f"**_capt_**: _{item['caption']}_")
            
            st.markdown("---") # Pemisah antara foto
            
        except FileNotFoundError:
            st.error(f"⚠️ Foto tidak ditemukan: {item['path']}")

    # Pindah ke kolom berikutnya
    current_col += 1
    
    # Jika sudah mencapai N_COLS, reset ke kolom pertama untuk baris baru
    if current_col >= N_COLS:
        cols = st.columns(N_COLS)
        current_col = 0

st.balloons()





