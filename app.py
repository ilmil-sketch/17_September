import streamlit as st

# Konfigurasi halaman web (layout="wide" agar lega)
st.set_page_config(page_title="Special Birthday Gift - Shashi Mulya Putri", page_icon="💖", layout="wide")

# CSS Tambahan untuk styling, kotak teks ramping, Keypad Teknik Sipil, dan Efek Fade-In Estetik
st.markdown("""
    <style>
    .main {
        background-color: #fdf2f8;
    }
    h1, h2, h3 {
        color: #db2777;
        font-family: sans-serif;
    }
    .poetry-box {
        background-color: #ffffff;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #f3e8ff;
        color: #374151;
        font-size: 13px;
        line-height: 1.5;
        white-space: pre-line;
        max-width: 240px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-top: 10px;
    }

    /* Membuat tombol keypad PIN berbentuk persegi empat kecil */
    .pin-keypad div.stButton > button {
        border-radius: 6px !important;
        background-color: rgba(219, 39, 119, 0.1) !important;
        color: #db2777 !important;
        font-weight: bold;
        font-size: 16px !important;
        border: 1px solid #db2777 !important;
        width: 60px !important;
        height: 60px !important;
        padding: 0px !important;
        margin: auto !important;
        display: block !important;
        transition: 0.2s;
    }
    .pin-keypad div.stButton > button:hover {
        background-color: #db2777 !important;
        color: white !important;
        transform: scale(1.05);
    }
    
    /* Efek Fade-In */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .fade-in-title {
        animation: fadeIn 1.5s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATA UTAMA KADO ---
TARGET_NAME = "Shashi Mulya Putri"
CORRECT_PIN = "17092006"  # PIN: 17 September 2006
PIN_CLUE = "Tanggal lahir kamu (17 September 2006) - 8 Angka"

WELCOME_MESSAGE = """
Hai Shashi Mulya Putri,

This your day! 🎉 
and ini revisial kemarin, juga sama-sama khusus untuk menyimpan setiap keping cerita, tawa, dan memori perjalanan kita. 

Silakan nikmati setiap keping kenangan di dalamnya. Enjoy your special day!
"""

CLOSING_MESSAGE = """
Terima kasih sudah melangkah sampai di kepingan terakhir. 
Semoga lembar-lembar cerita ini selalu membawa senyum di harimu. ✨
"""

# --- DATABASE 30 KEPING PUISI & KENANGAN ---
POETRY_COLLECTION = [
    {"number": 1, "title": "1. Niskala (Pertemuan yang Tak Terbaca)", "content": "Pertemuan itu asing, hambar, dan tanpa peduli,\nNama-nama yang lewat hanya singgah lalu mati...\n\nNamun semesta punya selera humor yang tak terduga,\nMeski jalan kita berbeda dan tujuan kita tak searah,\nNyatanya kita tetap jatuh pada frekuensi yang sama.", "image": "puisi1.png"},
    {"number": 2, "title": "2. Grahita (Isyarat di Balik Canggung)", "content": "Aku adalah manusia yang malas membuka diri,\nMemasang pagar tinggi, enggan berurusan dengan orang baru lagi.\n\nNamun di sana ada empat jiwa dalam satu lingkaran,\nMengubah sunyi menjadi sapaan hangat.", "image": "puisi2.png"},
    {"number": 3, "title": "3. Anitya (Ekspektasi yang Sementara)", "content": "Ospek pun tiba, membawa riuh yang tak kuinginkan,\nKupikir pertemanan ini hanya sementara.\n\nTernyata hari-hari itu menuliskan naskah yang berbeda.", "image": "puisi3.png"},
    {"number": 4, "title": "4. Sthira (Keteguhan yang Tak Terduga)", "content": "Ospek telah usai, namun tidak dengan cerita kita,\nPertemuan tak sengaja ini punya daya.", "image": "puisi4.png"},
    {"number": 5, "title": "5. Wirya (Keteguhan di Balik Layar)", "content": "Mencari jejak di ruang maya,\nMenemukan alasan untuk kembali terpana,\nMelihat caramu memeluk hidup.", "image": "puisi5.png"},
    {"number": 6, "title": "6. Anindita (Doa dalam Lingkaran Kebaikan)", "content": "Kisah hidupmu berhias bait doa yang taat,\nMenjaga langkahmu agar tak goyah diterjang ragu.", "image": "puisi6.png"},
    {"number": 7, "title": "7. Citraleka (Goresan Warna yang Berbeda)", "content": "Unik duniamu adalah simfoni tak biasa,\nKetukan Madura dan irama Spanish yang menyatu.", "image": "puisi7.png"},
    {"number": 8, "title": "8. Hasya (Logika yang Terpinggirkan)", "content": "Ada frekuensi tawa yang kita miliki,\nMembuat dunia terasa jauh lebih ringan.", "image": "puisi8.png"},
    {"number": 9, "title": "9. Mauna (Keheningan yang Menghargai)", "content": "Satu meja, tiga nyawa membelah jalan,\nTanpa tuntutan bicara, hanya keheningan tenang.", "image": "puisi9.png"},
    {"number": 10, "title": "10. Samsara (Aliran yang Beriringan)", "content": "Baja, beton, dan algoritma dipertemukan semesta,\nMenemukan celah untuk saling menyapa.", "image": "puisi10.png"},
    {"number": 11, "title": "11. Bhisak (Penawar di Sela Penat)", "content": "Saat koding dan tugas teknik menjajah hari,\nPertemuan kita jadi pelarian penawar penat.", "image": "puisi11.png"},
    {"number": 12, "title": "12. Aptika (Dukungan dalam Diam)", "content": "Kaku dalam merangkai diksi baru,\nNamun dukunganku menyala dalam diam.", "image": "puisi12.png"},
    {"number": 13, "title": "13. Pragatya (Sumbu yang Tetap Menyala)", "content": "Proses setiap raga berbeda,\nKegagalan hanyalah jeda, bukan akhir cerita.", "image": "puisi13.png"},
    {"number": 14, "title": "14. Itihasa (Rekam Jejak Sang Pelukis Kisah)", "content": "Membaca jejak dan potret kecil penuh keberanian,\nMenuliskan sejarah yang abadi.", "image": "puisi14.png"},
    {"number": 15, "title": "15. Anugraha (Penerimaan di Sela Logika)", "content": "Foto-foto jadi jembatan jarak kita,\nMenerima kaku dan terlambatnya waktu.", "image": "puisi15.png"},
    {"number": 16, "title": "16. Sabala (Spektrum yang Utuh)", "content": "Hitam dan putih membentuk perpaduan utuh,\nPelangi kebersamaan yang tak pernah berhenti.", "image": "puisi16.png"},
    {"number": 17, "title": "17. Bala (Jiwa yang Menolak Menua)", "content": "Meraba arah di dunia yang makin gila,\nIngin kembali jadi anak kecil tanpa beban.", "image": "puisi17.png"},
    {"number": 18, "title": "18. Siddhi (Misi yang Tertuntaskan)", "content": "Menuntaskan misi hidup di jalur berbeda,\nSaling menjaga benang pertemanan.", "image": "puisi18.png"},
    {"number": 19, "title": "19. Saka (Satu Warsa yang Bermakna)", "content": "Satu warsa merajut langkah bertiga,\nLingkaran pertemanan yang penuh makna.", "image": "puisi19.png"},
    {"number": 20, "title": "20. Kertajnya (Syukur yang Mengakar)", "content": "Terima kasih telah setia menikmati karya,\nRuang berekspresi tanpa rasa takut.", "image": "puisi20.png"},
    {"number": 21, "title": "21. Aptaya (Puncak dan Janji Jenaka)", "content": "Candaan jenaka di jalur pendakian,\nMembuat langkah berat terasa damai.", "image": "puisi21.png"},
    {"number": 22, "title": "22. Wiweka (Sketsa yang Berpadu)", "content": "Goresan pena dan gaya gambar yang berbeda,\nMenjadi harmoni dalam selembar sketsa.", "image": "puisi22.png"},
    {"number": 23, "title": "23. Sama (Di Bawah Langit yang Satu)", "content": "Menikmati sisa hari sebelum kembali pulang,\nMenjadi keping memori yang mengakar.", "image": "puisi23.png"},
    {"number": 24, "title": "24. Purwaka (Gerbang Awal di Bawah Terik)", "content": "Hari-hari penuh peluh di masa orientasi,\nMenjadi gerbang awal pertemanan tumbuh.", "image": "puisi24.png"},
    {"number": 25, "title": "25. Samyoga (Harmoni dalam Perbedaan)", "content": "Topping ice cream dalam satu rasa,\nPerbedaan jadi alasan untuk bersatu.", "image": "puisi25.png"},
    {"number": 26, "title": "26. Sasti (Restu Semesta yang Mengiringi)", "content": "Doa keluarga jadi dermaga paling kokoh,\nMerajut takdir dan rencana bersama.", "image": "puisi26.png"},
    {"number": 27, "title": "27. Akshara (Abadi dalam Piksel)", "content": "Memori tersimpan dalam barisan kode digital,\nAlgoritma persahabatan yang abadi.", "image": "puisi27.png"},
    {"number": 28, "title": "28. Abhipraya (Visi dalam Genggaman)", "content": "Menuju masa depan dengan langkah mantap,\nMemegang kompas iman dalam tujuan.", "image": "puisi28.png"},
    {"number": 29, "title": "29. Arya (Kemuliaan di Masa Depan)", "content": "Membayar mimpi dengan peluh dan perjuangan,\nMenjadi pribadi terhormat di atas kaki sendiri.", "image": "puisi29.png"},
    {"number": 30, "title": "30. Nitya (Keabadian dalam Goresan)", "content": "Tiga puluh keping saksi pertemanan tulus,\nTersimpan rapat, kekal dalam memori.", "image": "puisi30.png"}
]

# --- STATE SESSION ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "entered_pin" not in st.session_state:
    st.session_state.entered_pin = ""
if "wrong_pin_alert" not in st.session_state:
    st.session_state.wrong_pin_alert = False
if "step" not in st.session_state:
    st.session_state.step = "welcome"
if "selected_poem_idx" not in st.session_state:
    st.session_state.selected_poem_idx = 0

    # --- HALAMAN 1: LOCKSCREEN PIN ---
if not st.session_state.authenticated:
    st.markdown("<h2 class='fade-in-title' style='text-align: center;'>Happy Birthday</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Masukkan 8 digit PIN untuk membuka kado.<br><i>Clue: {PIN_CLUE}</i></p>", unsafe_allow_html=True)

    if st.session_state.wrong_pin_alert:
        st.error("PIN Salah bosssssssssssssss")

    pin_len = len(st.session_state.entered_pin)
    indicators = "".join(["🟣 " if i < pin_len else "⚪ " for i in range(8)])
    st.markdown(f"<p style='text-align: center; font-size: 24px;'>{indicators}</p>", unsafe_allow_html=True)

    # Bungkus bagian keypad dengan class khusus agar hanya tombol ini yang berbentuk persegi
    st.markdown('<div class="pin-keypad">', unsafe_allow_html=True)
    _, center_col, _ = st.columns([0.5, 3, 0.5])

    with center_col:
        # Baris 1: 1, 2, 3
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("1", key="k1", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "1"
                st.session_state.wrong_pin_alert = False
                st.rerun()
        with b2:
            if st.button("2", key="k2", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "2"
                st.session_state.wrong_pin_alert = False
                st.rerun()
        with b3:
            if st.button("3", key="k3", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "3"
                st.session_state.wrong_pin_alert = False
                st.rerun()

        # Baris 2: 4, 5, 6
        b4, b5, b6 = st.columns(3)
        with b4:
            if st.button("4", key="k4", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "4"
                st.session_state.wrong_pin_alert = False
                st.rerun()
        with b5:
            if st.button("5", key="k5", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "5"
                st.session_state.wrong_pin_alert = False
                st.rerun()
        with b6:
            if st.button("6", key="k6", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "6"
                st.session_state.wrong_pin_alert = False
                st.rerun()

        # Baris 3: 7, 8, 9
        b7, b8, b9 = st.columns(3)
        with b7:
            if st.button("7", key="k7", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "7"
                st.session_state.wrong_pin_alert = False
                st.rerun()
        with b8:
            if st.button("8", key="k8", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "8"
                st.session_state.wrong_pin_alert = False
                st.rerun()
        with b9:
            if st.button("9", key="k9", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "9"
                st.session_state.wrong_pin_alert = False
                st.rerun()

        # Baris 4: Hapus (⌫), 0, Konfirmasi (✔)
        b_del, b0, b_ok = st.columns(3)
        with b_del:
            if st.button("⌫", key="k_del", use_container_width=True):
                st.session_state.entered_pin = st.session_state.entered_pin[:-1]
                st.session_state.wrong_pin_alert = False
                st.rerun()
        with b0:
            if st.button("0", key="k0", use_container_width=True) and pin_len < 8:
                st.session_state.entered_pin += "0"
                st.session_state.wrong_pin_alert = False
                st.rerun()
        with b_ok:
            if st.button("✔", key="k_ok", use_container_width=True):
                if st.session_state.entered_pin == CORRECT_PIN:
                    st.session_state.authenticated = True
                    st.session_state.wrong_pin_alert = False
                    st.rerun()
                else:
                    st.session_state.wrong_pin_alert = True
                    st.session_state.entered_pin = ""
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
                    
# --- HALAMAN SETELAH PIN BENAR ---
else:
    # --- TAHAP 1: HALAMAN SAMBUTAN / SURAT UTAMA ---
    if st.session_state.step == "welcome":
        st.balloons()
        st.markdown(f"<h1 class='fade-in-title' style='text-align: center;'>Happy Level Up, {TARGET_NAME}! 🎉</h1>", unsafe_allow_html=True)
        st.divider()
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.info(WELCOME_MESSAGE)
            st.write("")
            if st.button("Lanjut ke Kumpulan Puisi & Memori ➡️", use_container_width=True):
                st.session_state.step = "poetry"
                st.rerun()

    # --- TAHAP 2: GALERI PUISI 1 - 30 ---
    elif st.session_state.step == "poetry":
        st.balloons()
        st.markdown(f"<h2 class='fade-in-title' style='text-align: center;'>📖 Galeri Kepingan Cerita</h2>", unsafe_allow_html=True)
        
        col_top1, col_top2 = st.columns([1, 1])
        with col_top1:
            if st.button("⬅️ Kembali ke Surat Sambutan"):
                st.session_state.step = "welcome"
                st.rerun()
        with col_top2:
            if st.button("Lanjut ke Penutupan ➡️", use_container_width=True):
                st.session_state.step = "closing"
                st.rerun()
                
        st.divider()
        
        # Sidebar: Kotak Pilihan Nomor (1 sampai 30)
        st.sidebar.markdown("### 🗂️ Pilih Kepingan Puisi")
        st.sidebar.write("Klik nomor untuk membaca:")
        
        cols_sidebar = st.sidebar.columns(5)
        for idx, item in enumerate(POETRY_COLLECTION):
            col_idx = idx % 5
            with cols_sidebar[col_idx]:
                if st.button(f"{item['number']}", key=f"sb_btn_{item['number']}", use_container_width=True):
                    st.session_state.selected_poem_idx = idx
                    st.rerun()

        # Tampilan Konten Puisi (Kiri: Kotak teks ramping ~5cm, Kanan: Gambar besar)
       # Tampilan Konten Puisi (Kiri: Kotak teks ramping ~5cm, Kanan: Gambar besar)
        current_poem = POETRY_COLLECTION[st.session_state.selected_poem_idx]
        st.markdown(f"<h3 class='fade-in-title'>{current_poem['title']}</h3>", unsafe_allow_html=True)
        
        # --- TOMBOL NAVIGASI SLIDE NEXT & BACK ---
        col_prev, col_info, col_next = st.columns([1, 2, 1])
        with col_prev:
            if st.button("⬅️ Sebelumnya", use_container_width=True):
                if st.session_state.selected_poem_idx > 0:
                    st.session_state.selected_poem_idx -= 1
                    st.rerun()
        with col_info:
            st.markdown(f"<p style='text-align: center; font-weight: bold; color: #db2777;'>Kepingan ke-{st.session_state.selected_poem_idx + 1} dari 30</p>", unsafe_allow_html=True)
        with col_next:
            if st.button("Selanjutnya ➡️", use_container_width=True):
                if st.session_state.selected_poem_idx < len(POETRY_COLLECTION) - 1:
                    st.session_state.selected_poem_idx += 1
                    st.rerun()

        st.write("") # Spasi pemisah

        # --- LAYOUT KONTEN UTAMA (TEKS & GAMBAR) ---
        col_txt, col_img = st.columns([1, 3])
        
        with col_txt:
            st.markdown(f'<div class="poetry-box">{current_poem["content"]}</div>', unsafe_allow_html=True)
            
        with col_img:
            st.image(current_poem["image"], use_container_width=True)
            
    # --- TAHAP 3: HALAMAN PENUTUPAN ---
    elif st.session_state.step == "closing":
        st.balloons()
        st.markdown(f"<h1 class='fade-in-title' style='text-align: center;'>Bye Bye</h1>", unsafe_allow_html=True)
        st.divider()
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.success(CLOSING_MESSAGE)
            st.write("")
            if st.button("⬅️ Kembali Membaca Puisi", use_container_width=True):
                st.session_state.step = "poetry"
                st.rerun()
