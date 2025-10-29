import requests
import tkinter as tk
from tkinter import messagebox

# 🔹 Step 1: Create window
def create_app():
    root = tk.Tk()
    root.title("Weather App 🌦")
    root.geometry("400x300")
    root.config(bg="#d0eaff")

    # 🔹 Step 2: API key aur base URL
    API_KEY = "00b2d8afd40ccc395d5053796899f1aa"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    # 🔹 Step 3: Function to get weather
    def get_weather():
        city = city_entry.get()
        if not city:
            messagebox.showwarning("⚠️ Warning", "Please enter a city name!")
            return

        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("❌ Error", f"City not found: {city}")
            return

        # 🔹 Extract useful info
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # 🔹 Show in labels
        result_label.config(
            text=f"🌆 City: {city.title()}\n🌡 Temp: {temp}°C\n💧 Humidity: {humidity}%\n☁ {description.title()}"
        )

    # 🔹 Step 4: GUI Components
    title_label = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"), bg="#d0eaff")
    title_label.pack(pady=10)

    city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
    city_entry.pack(pady=10)

    search_btn = tk.Button(root, text="Check Weather", font=("Arial", 12, "bold"),
                           command=get_weather, bg="#4da6ff", fg="white")
    search_btn.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Arial", 14), bg="#d0eaff")
    result_label.pack(pady=10)

    root.mainloop()


# 🔹 Step 5: Run only if script is main
if __name__ == "__main__":
    print("Launching Weather App...")
    create_app()
