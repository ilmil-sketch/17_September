// Database 30 Puisi & Kenangan
const POETRY_COLLECTION = [
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
];

// --- 1. LOGIKA KEYPAD PIN ---
const CORRECT_PIN = "17092006";
let enteredPin = "";

function updateIndicators() {
  let str = "";
  for (let i = 0; i < 8; i++) {
    str += (i < enteredPin.length ? "🟣 " : "⚪ ");
  }
  document.getElementById("indicators").innerText = str;
}

function pressDigit(num) {
  if (enteredPin.length < 8) {
    enteredPin += num;
    document.getElementById("error-alert").classList.add("hidden");
    updateIndicators();
  }
}

function pressBackspace() {
  enteredPin = enteredPin.slice(0, -1);
  document.getElementById("error-alert").classList.add("hidden");
  updateIndicators();
}

function pressSubmit() {
  if (enteredPin === CORRECT_PIN) {
    document.getElementById("screen-lock").classList.add("hidden");
    goToStep("welcome");
  } else {
    document.getElementById("error-alert").classList.remove("hidden");
    enteredPin = "";
    updateIndicators();
  }
}

// --- 2. DATA KUIS LENGKAP DENGAN KUNCI JAWABAN & ROASTING ---
const quizData = [
  {
    question: "1. Mobil impian yang paling sering dibahas atau jadi idaman?",
    options: ["Civic Turbo", "Ford Ranger Raptor", "Pajero Sport", "Jeep Rubicon"],
    correctIndex: 1
  },
  {
    question: "2. Momen paling random pas motong sayur kangkung?",
    options: [
      "Kangkungnya dimakan mentah",
      "Dipotong pakai rumus momen inersia",
      "Batangnya dipilah satu-satu sampai subuh",
      "Dipotong sambil curhat dramatis"
    ],
    correctIndex: 2
  },
  {
    question: "3. Sebagai anak Teknik Sipil sejati, tugas apa yang paling menyiksa batin?",
    options: [
      "Analisis Struktur & Mekanika Rekayasa",
      "Gambar Denah / Gartek AutoCAD",
      "Uji Kuat Tekan Beton & Tanah",
      "Semuanya bikin pengen ganti jurusan"
    ],
    correctIndex: 3
  },
  {
    question: "4. Kapan jam-jam kritis pas ngerjain laporan praktikum?",
    options: [
      "Pagi pas mau masuk kelas",
      "Jam 2 malam depan laptop sambil ngelamun",
      "Pas file corrupt belum ke-save",
      "Gak pernah kritis, selalu sat-set"
    ],
    correctIndex: 1
  },
  {
    question: "5. Apa respon pertama kalau dapet kabar libur dadakan?",
    options: [
      "Tidur seharian penuh",
      "Cari makan enak / nongkrong",
      "Malah bingung mau ngapain",
      "Tetep mikirin revisian"
    ],
    correctIndex: 0
  },
  {
    question: "6. Kalau disuruh milih: Beton mutu tinggi K-500 atau Raptor?",
    options: [
      "Tetep cinta beton",
      "Tentu saja Raptor tanpa mikir!",
      "Raptor isi adukan semen",
      "Dua-duanya buat proyek masa depan"
    ],
    correctIndex: 1
  },
  {
    question: "7. Pertanyaan terakhir, apa harapan terbaik di umur yang baru?",
    options: [
      "Proyek & kuliah lancar jaya",
      "Selalu bahagia dan banyak duit",
      "Bisa nyetir Raptor beneran",
      "Semua doa baik terkabul tanpa tapi!"
    ],
    correctIndex: 3
  }
];

const randomRoasts = [
  "Salah woyyyy! Masa lupa sih?! 😭",
  "Teng nong! Jawabanmu terdeteksi ngawur wkwk.",
  "Mikirnya jangan sambil ngantuk dong boss! Coba lagi.",
  "Astagfirullah, ingat-ingat lagi momennya astagaaa...",
  "Bukan ituuuu! Jangan pura-pura lupa ya! 🤨",
  "Salah! Nilai kuis ini minus 100 kalau ngasal terus.",
  "Meleset jauh! Pikirin pake logika anak sipil coba."
];

let currentQuizIndex = 0;

function loadQuestion() {
  const q = quizData[currentQuizIndex];
  document.getElementById("quiz-counter").innerText = `Pertanyaan ${currentQuizIndex + 1} dari ${quizData.length}`;
  document.getElementById("question-text").innerText = q.question;

  const errorBox = document.getElementById("quiz-error");
  if (errorBox) errorBox.classList.add("hidden");

  const optionsDiv = document.getElementById("options-container");
  optionsDiv.innerHTML = "";

  q.options.forEach((opt, idx) => {
    const btn = document.createElement("button");
    btn.className = "option-btn";
    btn.innerText = opt;
    btn.onclick = () => handleAnswer(idx);
    optionsDiv.appendChild(btn);
  });
}

function handleAnswer(selectedIdx) {
  const q = quizData[currentQuizIndex];
  const errorBox = document.getElementById("quiz-error");

  if (selectedIdx === q.correctIndex) {
    if (errorBox) errorBox.classList.add("hidden");
    confetti({ particleCount: 40, spread: 60, origin: { y: 0.7 } });

    currentQuizIndex++;
    if (currentQuizIndex < quizData.length) {
      loadQuestion();
    } else {
      goToStep("poetry");
    }
  } else {
    const randomText = randomRoasts[Math.floor(Math.random() * randomRoasts.length)];
    errorBox.innerText = randomText;
    errorBox.classList.remove("hidden");

    const card = document.querySelector(".quiz-card");
    card.classList.add("shake");
    setTimeout(() => card.classList.remove("shake"), 400);
  }
}

// --- 3. EFEK BALON & STEP ROUTER ---
function triggerBalloons() {
  confetti({
    particleCount: 80,
    spread: 90,
    origin: { y: 0.6 }
  });
}

function goToStep(step) {
  document.getElementById("screen-welcome").classList.add("hidden");
  document.getElementById("screen-quiz").classList.add("hidden");
  document.getElementById("screen-poetry").classList.add("hidden");
  document.getElementById("screen-closing").classList.add("hidden");

  if (step === "welcome") {
    document.getElementById("screen-welcome").classList.remove("hidden");
    triggerBalloons();
  } else if (step === "quiz") {
    document.getElementById("screen-quiz").classList.remove("hidden");
    currentQuizIndex = 0;
    loadQuestion();
  } else if (step === "poetry") {
    document.getElementById("screen-poetry").classList.remove("hidden");
    triggerBalloons();
  } else if (step === "closing") {
    document.getElementById("screen-closing").classList.remove("hidden");
    triggerBalloons();
  }
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// --- 4. RENDER 30 PUISI ---
let selectedPoemIndex = 0;

function renderPoem(idx) {
  selectedPoemIndex = idx;
  const poem = POETRY_COLLECTION[idx];

  document.getElementById("poem-title").innerText = poem.title;
  document.getElementById("poem-content").innerText = poem.content;
  document.getElementById("poem-image").src = poem.image;

  document.querySelectorAll(".num-btn").forEach((btn, bIdx) => {
    if (bIdx === idx) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });
}

function setupNumbersGrid() {
  const grid = document.getElementById("numbers-grid");
  grid.innerHTML = "";
  POETRY_COLLECTION.forEach((item, idx) => {
    const btn = document.createElement("button");
    btn.className = "num-btn" + (idx === 0 ? " active" : "");
    btn.innerText = item.number;
    btn.onclick = () => renderPoem(idx);
    grid.appendChild(btn);
  });
}

// Inisialisasi awal
setupNumbersGrid();
renderPoem(0);
