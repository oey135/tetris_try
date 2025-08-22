# streamlit_best_dish.py
import streamlit as st
import random
from datetime import datetime

# 앱 타이틀
st.title("🍽 오늘의 베스트 요리 추천")

# 현재 계절 계산 함수
def get_season():
    month = datetime.now().month
    if month in [12, 1, 2]:
        return "겨울"
    elif month in [3, 4, 5]:
        return "봄"
    elif month in [6, 7, 8]:
        return "여름"
    else:
        return "가을"

# 계절별 제철 음식과 요리 매핑
seasonal_dishes = {
    "봄": ["냉이 된장국", "달래 무침", "두릅 볶음", "딸기 스무디", "참나물 겉절이"],
    "여름": ["오이 냉국", "가지 튀김", "토마토 파스타", "수박 샐러드", "옥수수 구이"],
    "가을": ["사과 파이", "배 샐러드", "버섯 전골", "밤 조림", "고구마 라떼"],
    "겨울": ["귤 샐러드", "무국", "배숙", "배추 김치", "고등어 구이"]
}

# 현재 계절 가져오기
current_season = get_season()
st.subheader(f"🌸 현재 계절: {current_season}")

# 제철 요리 표시
st.write(f"이번 {current_season} 제철 요리 목록: {', '.join(seasonal_dishes[current_season])}")

# 오늘의 요리 추천
if st.button("🍴 오늘의 베스트 요리 추천!"):
    dish = random.choice(seasonal_dishes[current_season])
    st.success(f"오늘의 추천 요리는 **{dish}** 입니다!")
