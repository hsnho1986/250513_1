import streamlit as st

# 이모지 사전
title_emojis = "🧑‍💻 📈 🎓"
mbti_emojis = {
    "INTJ": "🧠", "INTP": "🔬", "ENTJ": "💼", "ENTP": "🎤",
    "INFJ": "📖", "INFP": "🎶", "ENFJ": "🤝", "ENFP": "🚀",
    "ISTJ": "📚", "ISFJ": "🌼", "ESTJ": "📋", "ESFJ": "🍽️",
    "ISTP": "🔧", "ISFP": "🎨", "ESTP": "🏎️", "ESFP": "🎉"
}

career_recommendations = {
    "INTJ": ["전략기획가", "데이터 과학자", "정책 분석가"],
    "INTP": ["연구원", "이론 물리학자", "AI 엔지니어"],
    "ENTJ": ["CEO", "경영 컨설턴트", "프로젝트 매니저"],
    "ENTP": ["창업가", "크리에이티브 디렉터", "광고기획자"],
    "INFJ": ["상담가", "작가", "심리학자"],
    "INFP": ["예술가", "시인", "사회복지사"],
    "ENFJ": ["교사", "HR 매니저", "코치"],
    "ENFP": ["탐험가", "마케터", "방송인"],
    "ISTJ": ["회계사", "법률가", "공무원"],
    "ISFJ": ["간호사", "사회복지사", "초등교사"],
    "ESTJ": ["군인", "관리자", "감독관"],
    "ESFJ": ["케이터링 매니저", "유치원 교사", "간병인"],
    "ISTP": ["기계공", "파일럿", "게임 디자이너"],
    "ISFP": ["패션 디자이너", "일러스트레이터", "플로리스트"],
    "ESTP": ["운동선수", "영업 담당자", "소방관"],
    "ESFP": ["배우", "가수", "이벤트 플래너"]
}

st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🤝")
st.title(f"{title_emojis} MBTI 기반 진로 추천기")

# ✨ 여기! 아래 코드를 삽입하세요
st.markdown(\"\"\"<움직이는 장식 코드>\"\"\", unsafe_allow_html=True)
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🤝")
st.title(f"{title_emojis} MBTI 기반 진로 추천기")

# ✨ 여기! 아래 코드를 삽입하세요
st.markdown(\"\"\"<움직이는 장식 코드>\"\"\", unsafe_allow_html=True)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to right, #ffe3e3, #ffe6fa);
        color: #333333;
        font-family: 'Helvetica', sans-serif;
    }
    .stSelectbox > div {
        font-size: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("## 📑 MBTI 유형을 선택하세요!")
selected_mbti = st.selectbox("", list(mbti_emojis.keys()), index=0, format_func=lambda x: f"{x} {mbti_emojis[x]}")

if selected_mbti:
    st.markdown(f"### 당신의 MBTI: {selected_mbti} {mbti_emojis[selected_mbti]}")
    st.markdown("---")
    st.markdown(f"## 📆 추천 직업 🚀")

    for job in career_recommendations[selected_mbti]:
        st.markdown(f"- 👉 **{job}**")

    st.markdown("---")
    st.info("이 결과는 참고용이며, 다양한 경험과 탐색을 통해 자신의 진로를 구체화해보세요! 📚")

st.markdown("\n\n")
st.caption("Made with ❤️ by Notischool")
