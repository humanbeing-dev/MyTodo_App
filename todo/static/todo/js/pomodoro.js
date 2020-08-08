let countdown;
const timerDisplay = document.querySelector('#time');
const pomodoroButton = document.querySelector('#btn-pomodoro');

pomodoroButton.addEventListener('click', () => {
  timer(45*60);
})


function timer(seconds) {
    clearInterval(countdown);

    const now = Date.now();
    const then = now + seconds*1000;

    countdown = setInterval(() => {
        const secondsLeft = Math.round((then - Date.now()) / 1000);
        if(secondsLeft < 0) {
            clearInterval(countdown);
            return;
        }
    displayTimeLeft(secondsLeft);
    }, 1000);
}

function displayTimeLeft(seconds) {
    const minutes = ('0'+Math.floor(seconds / 60)).slice(-2);
    const reminderSeconds = ('0'+Math.floor(seconds % 60)).slice(-2);
    const display = `${minutes}:${reminderSeconds}`;
    document.title = display;
    timerDisplay.textContent = display;
}

function displayEndTime(timestamp) {
    const end = new Date(timestamp);
    const hour = ('0'+end.getHours()).slice(-2);
    const minutes = ('0'+end.getMinutes()).slice(-2);
    const seconds = ('0'+end.getSeconds()).slice(-2);
    endTime.textContent = `${hour}:${minutes}:${seconds}`;
}


function startTimer() {
    const seconds = 25*60;
    timer(seconds);
}

//buttons.forEach(button => button.addEventListener('click', startTimer));
// document.customForm.addEventListener('submit', function(e) {
//     e.preventDefault();
//     const mins = this.minutes.value;
//     timer(mins*60);
//     this.reset();
// });