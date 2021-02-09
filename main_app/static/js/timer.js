const timerEl = document.getElementById("timer");
const startBtn = document.getElementById("startButton");
const threeMinBtn = document.getElementById("threeMinButton");
const fiveMinBtn = document.getElementById("fiveMinButton");
const secBar = document.getElementById("seconds");
const minBar = document.getElementById("minutes");

let timerInterval;
let min, sec;
let seconds = 15;

startBtn.addEventListener("click", () => {
  if (timerInterval) {
    clearInterval(timerInterval);
    return (timerInterval = null);
  }
//   if (seconds === 0) {
//     break;
//   }
  startTimer();
});

threeMinBtn.addEventListener("click", () => {
  clearInterval(timerInterval);
  seconds = 180;
  render();
  return (timerInterval = null);
});

fiveMinBtn.addEventListener("click", () => {
  clearInterval(timerInterval);
  seconds = 300;
  render();
//   startTimer();
  return (timerInterval = null);
});

function tick() {
  seconds--;
  if (seconds === 0) {
    clearInterval(timerInterval);
  }
  render();
}

function startTimer() {
  clearInterval(timerInterval);
  timerInterval = setInterval(tick, 1000);
}

function render() {
  min = Math.floor(seconds / 60);
  sec = seconds % 60;
  min = min % 60;
  if (sec < 10) {
    timerEl.innerText = `${min}:0${sec}`;
  } else {
    timerEl.innerText = `${min}:${sec}`;
  }
  secBar.style = `width: ${(sec / 60) * 100}%`;
  secBar.innerText = sec;
  minBar.style = `width: ${(min / 5) * 100}%`;
  minBar.innerText = min;
}
