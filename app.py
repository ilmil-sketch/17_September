import base64
import glob
import time
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For You Tretan! 🎈", page_icon="🎁", layout="centered"
)

# Load CSS
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass


# FUNGSI PUTAR VIDEO BACKGROUND DARI AWAL WEB DIBUKA
def set_bg_video(video_file):
    try:
        with open(video_file, "rb") as f:
            video_bytes = f.read()
            b64_video = base64.b64encode(video_bytes).decode()
            st.markdown(
                f"""
                <video autoplay loop muted playsinline id="bg-video">
                    <source src="data:video/mp4;base64,{b64_video}" type="video/mp4">
                </video>
                """,
                unsafe_allow_html=True,
            )
    except FileNotFoundError:
        pass


# Panggil Video Musim Gugur Sejak Awal Aplikasi Dibuka
set_bg_video("autumn_bg.mp4")

# ANIMASI PET NATURAL SESUAI SPESIES
components.html(
    """
    <script>
        (function() {
            var doc = parent.document;
            if (doc.getElementById('pet-layer-global')) return;

            var container = doc.createElement('div');
            container.id = 'pet-layer-global';
            container.style.cssText = 'position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:999; overflow:hidden;';
            doc.body.appendChild(container);

            var petData = [
                { icon: '🐈‍⬛', type: 'walker', speed: 1.2 },
                { icon: '🐈', type: 'walker', speed: 1.0 },
                { icon: '🐕', type: 'walker', speed: 1.5 },
                { icon: '🐇', type: 'hopper', speed: 1.8 },
                { icon: '🕊️', type: 'flyer', speed: 1.1 },
                { icon: '🦋', type: 'flutter', speed: 0.8 }
            ];

            var pets = [];

            petData.forEach(function(data, i) {
                var el = doc.createElement('div');
                el.innerText = data.icon;
                el.style.position = 'absolute';
                el.style.fontSize = (2.2 + Math.random() * 0.4) + 'rem';
                el.style.willChange = 'transform';
                container.appendChild(el);

                var startY;
                if (data.type === 'flyer') {
                    startY = parent.window.innerHeight * 0.15;
                } else if (data.type === 'flutter') {
                    startY = parent.window.innerHeight * 0.3;
                } else {
                    startY = parent.window.innerHeight - 75 - (i * 8);
                }

                pets.push({
                    el: el,
                    type: data.type,
                    x: Math.random() * parent.window.innerWidth,
                    y: startY,
                    baseY: startY,
                    speed: data.speed,
                    dir: Math.random() < 0.5 ? 1 : -1,
                    timer: Math.random() * 100,
                    state: 'moving',
                    stateTimer: 0
                });
            });

            function updatePets() {
                pets.forEach(function(p) {
                    p.timer += 0.05;
                    p.stateTimer++;

                    if (p.type === 'walker' || p.type === 'hopper') {
                        if (p.state === 'moving' && p.stateTimer > 180 + Math.random() * 200) {
                            p.state = Math.random() < 0.5 ? 'sniffing' : 'pause';
                            p.stateTimer = 0;
                        } else if ((p.state === 'sniffing' || p.state === 'pause') && p.stateTimer > 80 + Math.random() * 100) {
                            p.state = 'moving';
                            p.stateTimer = 0;
                            if (Math.random() < 0.3) p.dir *= -1;
                        }
                    }

                    var offsetY = 0;
                    var rot = 0;

                    if (p.state === 'moving') {
                        p.x += p.speed * p.dir;

                        if (p.type === 'walker') {
                            offsetY = Math.sin(p.timer * 8) * 3;
                        } else if (p.type === 'hopper') {
                            var hopCycle = Math.sin(p.timer * 6);
                            offsetY = -Math.max(0, hopCycle) * 16;
                        } else if (p.type === 'flyer') {
                            p.x += (p.speed * 0.5) * p.dir;
                            offsetY = Math.sin(p.timer * 3) * 12;
                            rot = Math.cos(p.timer * 3) * 5;
                        } else if (p.type === 'flutter') {
                            p.x += Math.sin(p.timer * 2) * 1.5;
                            offsetY = Math.cos(p.timer * 4) * 15;
                        }

                        if (p.x < -60) p.x = parent.window.innerWidth + 20;
                        if (p.x > parent.window.innerWidth + 60) p.x = -20;
                    } else if (p.state === 'sniffing') {
                        offsetY = Math.sin(p.timer * 10) * 1.5;
                        rot = Math.sin(p.timer * 5) * 4;
                    }

                    var scaleX = p.dir > 0 ? 1 : -1;
                    var curY = p.y + offsetY;
                    
                    p.el.style.transform = 'translate3d(' + p.x + 'px, ' + curY + 'px, 0) scaleX(' + scaleX + ') rotate(' + rot + 'deg)';
                });

                parent.requestAnimationFrame(updatePets);
            }

            updatePets();
        })();
    </script>
    """,
    height=0,
)

# Data Soal Kuis
questions = [
    {
        "id": 1,
        "question": "1. Mobil ireng, gagah, gedhe, dhukur...?",
        "options": ["A. Ford Raptor", "B. Angkot Carry L300"],
        "correct": "A. Ford Raptor",
        "wrong_msg": "Ups, legendaris si, tapi bukan dia",
    },
    {
        "id": 2,
        "question": "2. Hasil tebakan akar kuadrat dari 64 (√64)?",
        "options": ["A. 8", "B. Halah emboh"],
        "correct": "A. 8",
        "wrong_msg": "Halah emboh? nyerah di √64...",
    },
    {
        "id": 3,
        "question": "3. Momen paling nempel dan konyol?",
        "options": [
            "A. Motong sayur kangkung",
            "B. Nungguin semen kering di proyek",
        ],
        "correct": "A. Motong sayur kangkung",
        "wrong_msg": "Kita gak pernah ada moment nunggu semen kering please",
    },
    {
        "id": 4,
        "question": (
            "4. Pondasi paling kokoh di dunia sipil selain beton berkualitas"
            " tinggi?"
        ),
        "options": ["A. Komunikasi & Sabar", "B. Wejangan-wejangan"],
        "correct": "A. Komunikasi & Sabar",
        "wrong_msg": "Wejangan kyai ta kok marai adem",
    },
    {
        "id": 5,
        "question": (
            "5. Setinggi-tingginya gedung yang kamu rancang, tetep kalah tinggi"
            " dibanding...?"
        ),
        "options": [
            "A. Doa dan rasa sayang for kamu",
            "B. Tugas-tugas universitas",
        ],
        "correct": "A. Doa dan rasa sayang for kamu",
        "wrong_msg": "curhat kah?",
    },
]

# State
if "step" not in st.session_state:
    st.session_state.step = -1
if "poem_index" not in st.session_state:
    st.session_state.poem_index = 0
if "error_message" not in st.session_state:
    st.session_state.error_message = None
if "trigger_correct" not in st.session_state:
    st.session_state.trigger_correct = False

# ----------------------------------------------------
# 0. HALAMAN SELAMAT DATANG (WELCOME PAGE)
# ----------------------------------------------------
if st.session_state.step == -1:
    st.markdown(
        "<h1 style='text-align: center;'>🎉 Happy Birthday! 🎂</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center;'>Selamat Datang di Kuis Spesial Ultah"
        " Kamu ✨</h3>",
        unsafe_allow_html=True,
    )
    st.divider()

    st.markdown(
        """
        <div class="ppt-slide-card" style="text-align: center;">
            <p style="font-size: 1.1em; line-height: 1.6;">
                Selamat ulang tahun! 🎈<br>
                Sebelum lanjut bakal ada 5 pertanyaan,
                So, selamat menjawab.<br><br>
                <i>Yang niat yach!</i> 🫣
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    if st.button("Mulai Kuis 🚀"):
        st.session_state.step = 0
        st.rerun()

# ----------------------------------------------------
# 1. BAGIAN KUIS (BENAR = BALON TERBANG | SALAH = EMOT DATAR)
# ----------------------------------------------------
elif st.session_state.step < len(questions):
    st.title("🎂Happy Birthday Special Quiz!🎉")
    current_q = questions[st.session_state.step]

    st.caption(f"Pertanyaan {st.session_state.step + 1} dari {len(questions)}")
    st.progress((st.session_state.step + 1) / len(questions))

    st.subheader(current_q["question"])

    user_choice = st.radio(
        "Pilih jawabanmu:",
        current_q["options"],
        key=f"q_{current_q['id']}",
    )

    if st.session_state.trigger_correct:
        st.balloons()
        st.session_state.trigger_correct = False

    if st.session_state.error_message:
        st.markdown(
            f"""
            <div class="falling-emot-box">
                <div class="falling-emot">😐</div>
                <p style="margin-top:10px; font-weight:bold; color:#ff6b6b;">{st.session_state.error_message}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    button_label = (
        "Lanjut ➡️️"
        if st.session_state.step < len(questions) - 1
        else "Lihat Hadiah ✨"
    )

    if st.button(button_label):
        if user_choice == current_q["correct"]:
            st.session_state.error_message = None
            st.session_state.trigger_correct = True
            st.session_state.step += 1
            st.rerun()
        else:
            st.session_state.error_message = current_q["wrong_msg"]
            st.rerun()

# ----------------------------------------------------
# 2. GALERI PUISI (EFEK SLIDE PPT + CONFETTI MANDIRI)
# ----------------------------------------------------
else:
    st.title("🎂 Happy Birthday Special Quiz! 🎉")
    st.success("Yey! Kamu berhasil menyelesaikan semua kuisnya! 🎉")
    st.divider()

    st.header("📜 Hadiah Galeri Puisi Spesial")

    components.html(
        """
        <script>
            var script = parent.document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js';
            script.onload = function() {
                parent.confetti({
                    particleCount: 120,
                    spread: 100,
                    startVelocity: 30,
                    origin: { y: 0.1 },
                    scalar: 1.2,
                    gravity: 0.8,
                    ticks: 250
                });
            };
            parent.document.head.appendChild(script);
        </script>
        """,
        height=0,
    )

    image_extensions = ("*.png", "*.jpg", "*.jpeg", "*.PNG", "*.JPG", "*.JPEG")
    unique_images = set()
    for ext in image_extensions:
        unique_images.update(glob.glob(ext))

    image_files = sorted(list(unique_images))

    if image_files:
        total_poems = len(image_files)
        if st.session_state.poem_index >= total_poems:
            st.session_state.poem_index = 0

        current_img = image_files[st.session_state.poem_index]

        st.caption(
            f"Slide {st.session_state.poem_index + 1} dari {total_poems}"
        )

        st.markdown(
            f'<div class="ppt-slide-card" id="slide-card-{st.session_state.poem_index}-{time.time()}">',
            unsafe_allow_html=True,
        )
        st.image(
            current_img,
            caption=f"Puisi #{st.session_state.poem_index + 1}",
            use_container_width=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        col_prev, col_mid, col_next = st.columns([1, 2, 1])

        with col_prev:
            if st.button("⬅️ Slide Sebelumnya"):
                if st.session_state.poem_index > 0:
                    st.session_state.poem_index -= 1
                    st.rerun()

        with col_next:
            if st.button("Slide Selanjutnya ➡️"):
                if st.session_state.poem_index < total_poems - 1:
                    st.session_state.poem_index += 1
                    st.rerun()

    else:
        st.warning("⚠️ Belum ada gambar puisi di folder proyek.")

    st.divider()

    if st.button("🔄 Ulangi dari Kuis"):
        st.session_state.step = -1
        st.session_state.poem_index = 0
        st.session_state.error_message = None
        st.rerun()