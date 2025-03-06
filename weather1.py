import streamlit as st
import requests

# OpenWeatherMap API 정보
API_KEY = "3f0c83a7ddf4d26396af316702eae3d3"  # 여기에 본인의 API 키 입력
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Streamlit UI 설정
st.title("🌤️ 실시간 날씨 조회")

# 사용자 입력 (도시 이름)
city = st.text_input("도시 이름을 입력하세요:")

if st.button("날씨 조회"):
    if not city:
        st.error("도시 이름을 입력하세요!")
    else:
        params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "kr"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if data.get("cod") != 200:
            st.error(f"도시를 찾을 수 없습니다: {city}")
        else:
            weather = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            # 결과 출력
            st.success(f"**{city}의 날씨 정보**")
            st.write(f"🌡️ 온도: {temp}°C")
            st.write(f"💧 습도: {humidity}%")
            st.write(f"🌬️ 풍속: {wind_speed} m/s")
            st.write(f"☁️ 날씨 상태: {weather}")
