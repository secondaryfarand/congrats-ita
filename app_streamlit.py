import streamlit as st
from datetime import datetime
import base64 
from PIL import Image


st.set_page_config (
    page_title= "SELAMAT MENJABAT !!!", 
    page_icon= ":sparkles::",
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
        "path": "images/fotbem1.JPG",
        "caption": "😍",
        "lucu": True
    },
    {
        "path": "images/fotbem2.JPG",
        "caption": " 🤣",
        "lucu": True
    },
    {
        "path": "images/fotbem3.JPG",
        "caption": " 🍕💖",
        "lucu": True
    },
    {
        "path": "images/fotbem4.JPG",
        "caption": "Dingin, tapi hatiku hangat karena ada kamu.(apasih) 🏔️🥰",
        "lucu": True
    },    
    {
        "path": "images/fotbem5.jpeg",
        "caption": "",
        "lucu": True
    },
    {
        "path": "images/fotbem6.JPG",
        "caption": "",
        "lucu": True
    }
    
]

yulita = [
    {
        "path": "images/foto1.jpeg",
        "caption": "😍",
        "lucu": True
    },
    {
        "path": "images/foto2.jpeg",
        "caption": " 🤣",
        "lucu": True
    },
    {
        "path": "images/foto3.jpeg",
        "caption": " 🍕💖",
        "lucu": True
    },
    {
        "path": "images/foto4.jpeg",
        "caption": "Dingin, tapi hatiku hangat karena ada kamu.(apasih) 🏔️🥰",
        "lucu": True
    },    
    {
        "path": "images/foto5.jpeg",
        "caption": "",
        "lucu": True
    },
    {
        "path": "images/foto6.jpeg",
        "caption": "",
        "lucu": True
    },
    {
        "path": "images/foto7.jpeg",
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


st.markdown(
    """
    Selamat menjabat ya, yulita. Selamat kembali berproses panjang ya di BEM, semoga dapet pengalaman baik selama satu tahun kedepan. Tentunya pasti akan ada bad dan very bad moment, tenang ceritain aja nanti dan setelah itu lupain, pasti bakal lewat juga.



Aku buat ini pas begadang kemarin sampai jam setengah 6an, dan karena ortu dah bangun ditambah juga kepala udah ruet liat codingan, mata udah capek jadi aku tidur dan lanjut di jam 11 siang setelah aku khe bangunin.

Meskipun sebenernya kemarin malem (kalo khe bacanya pas pelantikan), itu kita bareng lewat online dan gak sengaja buka hal yang seharusnya gak kita buka, dan kebetulannya itu bukanya barengan wkwkw, jadi agak akward kemarin, tapi aku udah netral sih jadi aman aja. Jadi aku langsung ajak khe call lagi biar khe gak ngira aku gimana". Ya gimana" sih tapi yaudah lah itu udah diluar kendali jadi ya belajar untuk ngerti dan tau posisi juga. Kebetulan juga besok itu dah jadi hari special mu sebagai anak organisasi, tentunya harus ikut dibanggain dan dibahagiain aja, cukup di pendem hal" yang bikin ngga bahagia karena ini moment bahagia khe sebagai pimpinan di organisasi , keren.

Untungnya kemarin aku ngajakin lagi dan kita jadi meet malem, jadi aku buka project dan darisanalah aku dapet ide untuk bikin ini buat khe besok pagi, karena ini moment special jadi aku iseng aja sih pengen ngasih ini sebagai ucapan dan biar khe seneng juga, semoga wkwk

#  Ga ada apa apanya sih cuma ucapan yang dibungkus kayak gini aja, priceless tapi harapanya ini bisa jadi hal yang berkesan lah buat khe, sama seperti dinofar-hijau yang aku kasi.
      
        ... 😊  
    """
)
st.image("images/dinofar.jpeg", use_container_width=True)


st.markdown(
    """
  Jadi malem malem aku gas garap sembari khe tidur dan siapin tenaga buat esok.

Terakhir, untuk momen ini harapanku kita bisa belajar dari satu tahun kepengurusan kita di BEM bersama, terus harapan berikutnya semoga khe aman-aman aja ya di BEM 2026 dengan segala huru hara dan ruetnya yang baru dari tahun sebelumnya, itu akan ada dan khe harus dan pasti bisa hadapin juga kok, ibarat mengulang baca buku yang sama tapi sekarang khe bawa tinta buat ganti teks yang khe ngga suka atau pengen merubah tulisan di buku itu. Dan harapan untuk kita yaitu semoga diakhir 2026 nanti aku dan khe, kita berdua, bisa sama-sama menunjukan dan memamerkan wkwk apa yang udah kita dapet, dan value atau perubahan apa sih yang udah kita bawa dan capai selama itu. 

Walau aku cuma bisa liat dari jauh / dari luar gimana proses mu di tahun depan tapi gpp aku bakal pantau dan semangat in sebisanya. meski aku gaada di sana tenang dah ada dinoku yang bakal nemeinn khe jadi tanpa aku pun ttep semangat. Sekian dari aku, aku bakal berproses juga dan jadiin rasa" slek dan gaenak di diriku ini sebagai motivasi aja. Rasa itu kan emang ada ya, tapi aku gabisa apa apain, aku sedih, galau, marah ,ngambul, kangen ,seneng, itu pun dah gabisa di apa apain gitu..jadi yaudah aku jadiin itu tantangan dan motivasi aja sebagaimana aku sering "jokes" in khe tentang demis hehe.

Liat juga aku ya, aku penasaran gimana je aku nanti menannggapi kondisi ku kayak sekarang ini, apakah aku bisa di akhir taun depan mencapai semua targetku tanpa ada keluarga (organisasi)lagi sebagai wadah. Ini bener-bener ditentuin sama gimana aku nanti, kalau aku males ya gabisa, kalau aku rajin dan disiplin untuk membuktikan, astungkara bisa.



Fokus ke topik utama, intinya selamat dan bye sampai jumpa di akhir nanti dengan versi ter new ...

Terbang yang tinggi dan fokus ke tujuan masing-masing.


Ucapkan dan koreksi dalam hati kalau salah 

# YULITA, KAMU AKAN BISA BAWA PDP JADI BIDANG TERBAIK, BAWA PIONEER LEBIH BERDAMPAK DAN BAWA INVASI LEBIH INOVATIF DI BEM FMIPA 2026 


Semangat dan sukses dari - f
     


      
        ... 😊  
    """
)


st.info(f"**-** kanggoin yaa wkkw aku awag awag aja dan br kepikiran kemarin malem, awkdakwdmawk ")


N_COLS = 3
cols = st.columns(N_COLS)
curr_col = 0 

for item in yulita:
    with cols[curr_col]:
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
    curr_col += 1
    
    # Jika sudah mencapai N_COLS, reset ke kolom pertama untuk baris baru
    if curr_col >= N_COLS:
        cols = st.columns(N_COLS)
        curr_col = 0


st.balloons()
st.divider()
st.caption("Made by **Farand Darmika** :sparkles:")





