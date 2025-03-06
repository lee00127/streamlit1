import tkinter as tk
from tkinter import messagebox
import requests

# OpenWeatherMap API 정보
API_KEY = "3f0c83a7ddf4d26396af316702eae3d3"  # 여기에 본인의 API 키 입력
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("오류", "도시 이름을 입력하세요!")
        return
    
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "kr"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if data.get("cod") != 200:
        messagebox.showerror("오류", f"도시를 찾을 수 없습니다: {city}")
        return
    
    weather = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    result_text.set(f"날씨: {weather}\n온도: {temp}°C\n습도: {humidity}%\n풍속: {wind_speed} m/s")

# Tkinter GUI 설정
root = tk.Tk()
root.title("날씨 조회 프로그램")
root.geometry("350x300")

# 입력 필드 및 버튼
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

tk.Button(root, text="날씨 조회", font=("Arial", 12), command=get_weather).pack()

# 결과 표시 레이블
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
