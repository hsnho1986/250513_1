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
    # MBTI별 유머러스한 학생 특징
mbti_descriptions = {
    "INTJ": "조용히 교실 한켠에서 미래 교육 제도를 설계 중인 전략가. 친구보다는 계획표를 더 사랑함.",
    "INTP": "질문은 많고 대답은 적다. 혼잣말로 실험하고, 급식 반찬에서 분자 구조를 유추함.",
    "ENTJ": "조별과제 리더 예약. 모두가 쉬는 시간에도 회의자료 만드는 야망꾼.",
    "ENTP": "선생님보다 먼저 질문하고, 답변보다 아이디어가 더 많은 수다왕 혁신가.",
    "INFJ": "친구의 고민 상담은 천직. 조용하지만 교실 뒤에서 세상을 바꾸는 방법을 고민 중.",
    "INFP": "수업 시간에 창밖을 보며 마음속으로 소설 한 편을 씀. 감성 100% 충전 완료.",
    "ENFJ": "반장? 당연함. 교실에 사랑과 질서를 동시에 전달하는 따뜻한 카리스마 소유자.",
    "ENFP": "수업 중 손 들기 1위. 친구와 이야기하다 수업 내용을 넘어 우주 이야기까지 확장함.",
    "ISTJ": "노트 필기 장인. 교사의 말 한 마디도 빠뜨리지 않음. 규칙은 생명임.",
    "ISFJ": "모두가 급식 줄 설 때, 친구 도시락 뚜껑 먼저 닫아주는 따뜻한 조력자.",
    "ESTJ": "무질서를 참지 못함. 책상 배열이 어긋나면 바로 정렬 시작하는 교실 관리자.",
    "ESFJ": "생일파티 기획과 급식 생일노래 담당. 모두의 행복을 책임지는 교실 호스트.",
    "ISTP": "가위, 테이프, 드라이버까지 다 갖춘 만능 공구왕. 교실 물건은 다 고쳐줌.",
    "ISFP": "그림 그리다 지우다, 다시 그리다… 결국 완벽하게 완성해서 감탄받는 예술혼.",
    "ESTP": "쉬는 시간이 되면 누구보다 먼저 운동장으로 돌진! 반응 속도는 게임 캐릭터급.",
    "ESFP": "오늘도 교실의 햇살 같은 존재. 춤추며 노래하고, 교실 분위기는 이 친구에게 달림."
}

    st.markdown(f"## 📆 추천 직업 🚀")

    for job in career_recommendations[selected_mbti]:
        st.markdown(f"- 👉 **{job}**")

    st.markdown("---")
    st.info("이 결과는 참고용이며, 다양한 경험과 탐색을 통해 자신의 진로를 구체화해보세요! 📚")

st.markdown("\n\n")
st.caption("Made with ❤️ by Notischool")
