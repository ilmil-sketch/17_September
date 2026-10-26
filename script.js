// 1. Verifikasi Sandi Masuk
  const CORRECT_PIN = "170906";

  function checkPin() {
    const pin = document.getElementById("pin-input").value;
    const error = document.getElementById("error-alert");

    if (pin === CORRECT_PIN) {
      document.getElementById("lock-section").classList.add("hidden");
      document.getElementById("quiz-section").classList.remove("hidden");
      loadQuestion();
    } else {
      error.classList.remove("hidden");
    }
  }

  // 2. Daftar 7 Pertanyaan Kuis
  const questions = [
    {
      question: "1. Mobil impian yang sering dibahas atau jadi idaman?",
      options: ["Ford Ranger Raptor", "Civic Turbo", "Pajero Sport", "Jeep Rubicon"],
      correct: 0
    },
    {
      question: "2. Momen paling random pas motong sayur kangkung?",
      options: [
        "Kangkungnya malah dimakan mentah",
        "Cara motongnya pakai teori simetri",
        "Batangnya dipilah satu-satu sampai lama",
        "Dipotong sambil curhat"
      ],
      correct: 2
    },
    {
      question: "3. Sebagai anak Teknik Sipil, tugas apa yang paling bikin begadang?",
      options: [
        "Analisis Struktur & Mekanika Rekayasa",
        "Gambar Teknik / AutoCAD",
        "Praktikum Uji Beton & Tanah",
        "Semua tugas di atas bikin stres"
      ],
      correct: 3
    },
    {
      question: "4. Kapan waktu paling rawan buat ngeluh soal laporan?",
      options: [
        "Pagi hari sebelum kuliah",
        "Jam 2 pagi depan laptop",
        "Pas udah deadline H-1 jam",
        "Gak pernah ngeluh, tetep tabah"
      ],
      correct: 1
    },
    {
      question: "5. Apa hal pertama yang dicari waktu selesai ujian semester?",
      options: [
        "Tidur 12 jam nonstop",
        "Makan makanan enak",
        "Jalan-jalan cari angin",
        "Langsung rebahan tanpa mikir beban"
      ],
      correct: 0
    },
    {
      question: "6. Kalau disuruh milih antara beton mutu tinggi vs Raptor?",
      options: [
        "Tentu saja Raptor",
        "Tetep setia sama beton",
        "Raptor yang ngangkut beton",
        "Gak bisa milih, dua-duanya aja"
      ],
      correct: 0
    },
    {
      question: "7. Terakhir, apa harapan terbesar di usia yang baru ini?",
      options: [
        "Skripsi & kuliah lancar",
        "Rezeki mengalir dan selalu bahagia",
        "Bisa kebeli Raptor impian",
        "Semua jawaban benar dan terwujud!"
      ],
      correct: 3
    }
  ];

  let currentQuestionIndex = 0;

  // 3. Render Pertanyaan dan Pilihan Ganda ke Layar
  function loadQuestion() {
    const q = questions[currentQuestionIndex];
    document.getElementById("quiz-counter").innerText = `Pertanyaan ${currentQuestionIndex + 1} dari ${questions.length}`;
    document.getElementById("question-text").innerText = q.question;

    const optionsDiv = document.getElementById("options-container");
    optionsDiv.innerHTML = "";

    q.options.forEach((opt, idx) => {
      const btn = document.createElement("button");
      btn.className = "option-btn";
      btn.innerText = opt;
      btn.onclick = () => selectAnswer(idx);
      optionsDiv.appendChild(btn);
    });
  }

  // 4. Handle Jawaban dan Efek Confetti Tiap Soal
  function selectAnswer(selectedIdx) {
    confetti({ 
      particleCount: 40, 
      spread: 50, 
      origin: { y: 0.7 } 
    });

    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
      loadQuestion();
    } else {
      showResults();
    }
  }

  // 5. Buka Halaman Galeri & Looping 30 Foto Puisi
  function showResults() {
    document.getElementById("quiz-section").classList.add("hidden");
    document.getElementById("result-section").classList.remove("hidden");

    // Efek ledakan confetti besar setelah kuis tamat
    confetti({ 
      particleCount: 150, 
      spread: 100, 
      origin: { y: 0.5 } 
    });

    const gallery = document.getElementById("gallery");
    gallery.innerHTML = ""; // Bersihkan kontainer jika sebelumnya ada elemen

    // Loop menampilkan puisi1.png hingga puisi30.png
    for (let i = 1; i <= 30; i++) {
      const img = document.createElement("img");
      img.src = `puisi${i}.png`;
      img.alt = `Puisi ${i}`;
      img.loading = "lazy"; // Optimasi loading bertahap saat di-scroll
      gallery.appendChild(img);
    }
  }

  // Fitur Tambahan: Tekan 'Enter' pada input sandi langsung cek PIN
  document.addEventListener("DOMContentLoaded", () => {
    const pinInput = document.getElementById("pin-input");
    if (pinInput) {
      pinInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
          checkPin();
        }
      });
    }
  });
