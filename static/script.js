// Function to fetch and display weather data
function getWeather() {
    const city = document.getElementById('city').value.trim();
    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    // Fetch weather data
    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            const weatherInfo = document.getElementById('weather-info');

            if (data.error) {
                weatherInfo.innerHTML = `
                    <p class="error-message">Error: ${data.error}</p>
                `;
            } else {
                // Update weather info dynamically
                weatherInfo.innerHTML = `
                    <div class="weather-info-header">
                        <img src="https://openweathermap.org/img/wn/${data.icon}@2x.png" alt="${data.description}">
                        <h2>${data.city}</h2>
                    </div>
                    <p class="current-time">Time: ${data.current_time}</p>
                    <p class="temperature">${data.temperature}°C</p>
                    <p class="temp-range">${data.min_temp}°C - ${data.max_temp}°C</p>
                    <p class="weather-condition">${data.description}</p>
                    <div class="weather-details">
                        <div class="weather-detail">
                            <h3>Wind Speed</h3>
                            <span>${data.wind_speed} km/h</span>
                        </div>
                        <div class="weather-detail">
                            <h3>Humidity</h3>
                            <span>${data.humidity}%</span>
                        </div>
                        <div class="weather-detail">
                            <h3>Pressure</h3>
                            <span>${data.pressure} hPa</span>
                        </div>
                    </div>
                `;
            }
        })
        .catch(error => {
            document.getElementById('weather-info').innerHTML = `
                <p class="error-message">Error: ${error.message}</p>
            `;
        });
}

// Event listener for button click
document.getElementById('get-weather').addEventListener('click', getWeather);

// Remove the loader after the page fully loads
window.addEventListener('load', () => {
    setTimeout(() => {
        document.body.classList.add('loaded');
    }, 1500);
});
