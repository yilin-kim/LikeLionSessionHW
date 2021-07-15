const input = document.querySelector("#city");
const button = document.querySelector("#submit");
const weatherBox = document.querySelector("#weatherBox");

const API_KEY = "65e84b3fa4225a9e8e6f2912ff989cbd";

button.addEventListener("click", async () => {
  // input에 입력된 도시명을 사용하여 적절한 uri로 날씨정보 요청
  const city = input.value;
  // response받아서 weatherBox에 적절하게 넣어준다.
  // innerHTML활용!
  // weatherBox html template 예시

  try {
    //save Current weather data API
    const res = await axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}`);
    console.log(res);

    //save weather description, icon, temp info
    const {description, icon} = res.data.weather[0];
    const temp = Math.round(res.data.main.temp - 273.15);
    const temp_max = Math.round(res.data.main.temp_max - 273.15);
    const temp_min = Math.round(res.data.main.temp_min - 273.15);
    const lat = Math.round(res.data.coord.lat);
    const lon = Math.round(res.data.coord.lon);
    const name = res.data.name;

    //save One Call API
    const resOne = await axios.get(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude=minutely,hourly&appid=${API_KEY}
    `);
    console.log(resOne);

    //save feels_like temp, clouds
    const feelTemp = Math.round(resOne.data.current.feels_like - 273.15);
    const clouds = resOne.data.current.clouds;
    const humidity = resOne.data.current.humidity;

    const alert = (weatherBox.innerHTML = `
    <div class="name">${name}</div>
     <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
     <div class="description">${description}</div>
     <div class="clouds">cloud ${clouds}%</div>
     <div class="humid">humidity ${humidity}%</div>
     <div class="temp">${temp}°C -- feels like ${feelTemp}°C</div>
     <div class="temp">MIN ${temp_min}°C \n MAX ${temp_max}°C</div>
     `);
  } catch (error) {
    console.log(error);
  }
});
