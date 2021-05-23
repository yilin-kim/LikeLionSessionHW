// 배경색 random
const getRandomHexaColor = () => {
  const hexa = "0123456789abcdef";
  // random color를 반환하는 로직 (힌트는 헥사 코드)
  let randomHexa = Math.floor(Math.random() * 0xffffff).toString(16);
  return (colorCode = "#" + randomHexa);
};

// setInterval은 100ms당 해당 함수를 실행하는 함수
setInterval(() => {
  document.querySelector("body").style.backgroundColor = getRandomHexaColor();
}, 100);

// Year Month Day Hour Minute Second 시계
const clockContent = document.querySelector(".now");

const getCurrentTime = () => {
  //현재 시간을 반환하는 객체 Date
  const date = new Date();
  const year = date.getFullYear();
  const month = date.getMonth();
  const day = date.getDate();
  const hour = date.getHours();
  const minute = date.getMinutes();
  const second = date.getSeconds();

  let YYMMDD = `${year}년 ${month < 10 ? `0${month}` : month}월 ${
    day < 10 ? `0${day}` : day
  }일`;
  let HHMMSS = `${hour < 10 ? `0${hour}` : hour}시 ${
    minute < 10 ? `0${minute}` : minute
  }분 ${second < 10 ? `0${second}` : second}초`;

  clockContent.innerText = YYMMDD + " " + HHMMSS;
};

const initClock = () => {
  getCurrentTime();
  setInterval(getCurrentTime, 1000);
};

initClock();
