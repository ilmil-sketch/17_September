// Data kuis pengganti logic if-else di Python
const quizData = [
  {
    question: "Kapan pertama kali kita saling kenal?",
    options: ["Waktu ospek", "Pas sekelompok tugas", "Di kantin", "Gak sengaja papasan"],
    answerIndex: 1
  },
  {
    question: "Apa hal paling random yang pernah diobrolin?",
    options: ["Tentang alien", "Tentang masa depan", "Resep mi instan", "Logika koding"],
    answerIndex: 3
  }
];

let currentStep = 0;

const heroSection = document.getElementById("hero");
const quizSection = document.getElementById("quiz-section");
const resultSection = document.getElementById("result-section");
const questionText = document.getElementById("question-text");
const optionsContainer = document.getElementById("options-container");
const startBtn = document.getElementById("start-btn");

startBtn.addEventListener("click", () => {
  heroSection.classList.add("hidden");
  quizSection.classList.remove("hidden");
  renderQuestion();
});

function renderQuestion() {
  const q = quizData[currentStep];
  questionText.textContent = q.question;
  optionsContainer.innerHTML = "";

  q.options.forEach((opt, idx) => {
    const btn = document.createElement("button");
    btn.textContent = opt;
    btn.addEventListener("click", () => handleAnswer(idx));
    optionsContainer.appendChild(btn);
  });
}

function handleAnswer(selectedIndex) {
  // Efek confetti kecil saat klik jawaban benar
  if (selectedIndex === quizData[currentStep].answerIndex) {
    confetti({ particleCount: 50, spread: 60 });
  }

  currentStep++;
  if (currentStep < quizData.length) {
    renderQuestion();
  } else {
    // Selesai kuis, tampilkan hasil dan confetti besar
    quizSection.classList.add("hidden");
    resultSection.classList.remove("hidden");
    confetti({ particleCount: 120, spread: 100, origin: { y: 0.6 } });
  }
}