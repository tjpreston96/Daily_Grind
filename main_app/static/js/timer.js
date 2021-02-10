const timerEl = document.getElementById("timer");
const startBtn = document.getElementById("startButton");
const threeMinBtn = document.getElementById("threeMinButton");
const fiveMinBtn = document.getElementById("fiveMinButton");
const timeBar = document.getElementById("time");

let timerInterval;
let min, sec;
let seconds = 120;
let initSec;
startBtn.addEventListener("click", () => {
  if (timerInterval) {
    clearInterval(timerInterval);
    return (timerInterval = null);
  }
  // if (seconds === 0) {
  //   break;
  // }
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
  
  if (sec < 10) {
    timerEl.innerText = `${min}:0${sec}`;
  } else {
    timerEl.innerText = `${min}:${sec}`;
  }
  timeBar.style = `width: ${(sec / 60) * 100}%`;
  timeBar.innerText = ` ${min} minutes ${sec} seconds`;
}
