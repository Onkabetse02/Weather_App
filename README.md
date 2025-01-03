"""
# 🌦 Weather App

The Weather App is a web application that provides current weather information for any city worldwide. It features a simple and intuitive interface, fetching real-time data from the OpenWeather API.

---

## 🚀 Features

- **Search by City**: Enter any city name to get the current weather details.
- **Real-Time Weather Data**: Displays temperature, weather condition, wind speed, humidity, and pressure.
- **Dynamic Icons**: Weather icons change based on current conditions.
- **Responsive Design**: Fully optimized for both desktop and mobile devices.

---

## 🛠️ Technologies Used

- **Frontend**: 
  - HTML5
  - CSS3
  - JavaScript (ES6+)
- **Backend**:
  - Python (Flask Framework)
  - OpenWeather API
  - Geopy, TimezoneFinder, pytz
- **Deployment**:
  - Render (for both frontend and backend)

---

## 🎨 Project Structure


\`\`\`
weather-app/
│
├── app.py                  # Flask application code
├── .env                    # API keys and configuration (not included in repo)
├── requirements.txt        # Python dependencies
├── Procfile                # Config for deploying on Render
├── static/                 # Frontend assets
│   ├── styles.css          # Styles for the app
│   ├── script.js           # JavaScript for frontend logic
│   ├── icons/              # Weather condition icons
│   └── x-icon.ico          # Favicon
└── templates/
    └── index.html          # Main frontend HTML file
\`\`\`

---

## 🧰 Prerequisites

1. Python 3.8+
2. Node.js (for frontend local testing, optional)
3. [OpenWeather API Key](https://openweathermap.org/api)

---

## 🛠️ Installation

### Backend Setup

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/Onkabetse02/weather-app.git
   cd weather-app
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Create a \`.env\` file and add your OpenWeather API key:
   \`\`\`
   WEATHER_API_KEY=your_api_key_here
   \`\`\`

4. Run the Flask app:
   \`\`\`bash
   python app.py
   \`\`\`

5. Access the app at \`http://localhost:5000\`.

---

### Frontend Setup (Optional Local Test)

1. Open \`index.html\` in any browser.
2. Replace \`https://your-backend-url\` in \`script.js\` with \`http://localhost:5000\`.

---

## 🚀 Deployment

### Backend Deployment (Render)

1. Push your repository to GitHub.
2. Create a new web service on Render:
   - Set \`Build Command\`: \`pip install -r requirements.txt\`
   - Set \`Start Command\`: \`gunicorn app:app\`
3. Deploy the backend and note the URL (e.g., \`https://your-app.onrender.com\`).

---

## 🌟 Usage

1. Visit the deployed URL (https://weather-app-mm6r.onrender.com)
2. Enter a city name in the search box.
3. View the weather details, including:
   - Temperature
   - High/Low Range
   - Wind Speed
   - Humidity
   - Pressure
   - Weather Condition

---

## 📸 Screenshots

### Home Page:
![Home Page](./static/images/home_page.png)

### Weather Result:
![Weather Result](./static/images/weather_results.png)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- [OpenWeather API](https://openweathermap.org/api)
- [Geopy](https://geopy.readthedocs.io/)
- [Render](https://render.com/)
"""