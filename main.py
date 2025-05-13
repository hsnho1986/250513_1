import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 사이트", page_icon="❤️", layout="centered")

# MBTI 목록 및 이모지 매핑
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]
mbti_emojis = {
    "ISTJ": "📚", "ISFJ": "🌼", "INFJ": "🔮", "INTJ": "🧠",
    "ISTP": "🔧", "ISFP": "🎨", "INFP": "💖", "INTP": "🔬",
    "ESTP": "🏎️", "ESFP": "🎉", "ENFP": "🚀", "ENTP": "🗣️",
    "ESTJ": "📋", "ESFJ": "🤗", "ENFJ": "🤝", "ENTJ": "💼"
}

# 궁합 데이터 (샘플 점수)
import random
random.seed(42)
compatibility = {
    (t, s): random.randint(50, 100) for t in mbti_list for s in mbti_list
}

def get_compat_score(teacher, student):
    return compatibility.get((teacher, student), 0)

# 타이틀
st.title("✨ 선생님 vs 학생 MBTI 궁합 테스트 ✨")

# 사이드바
st.sidebar.header("MBTI 선택")
teacher_mbti = st.sidebar.selectbox("선생님 MBTI", mbti_list)
student_mbti = st.sidebar.selectbox("학생 MBTI", mbti_list)

# 궁합 점수 계산
score = get_compat_score(teacher_mbti, student_mbti)

# 메인 컬럼
st.markdown(f"### 선생님: {mbti_emojis[teacher_mbti]} **{teacher_mbti}**  vs 학생: {mbti_emojis[student_mbti]} **{student_mbti}**")

# 점수 표시
st.progress(score / 100)
st.metric("궁합 점수", f"{score}/100")

# 재미있 코멘트
if score > 85:
    st.success("🎉 환상의 듀오! 이 수업은 불타오를 준비 완료!")
elif score > 70:
    st.info("👍 잘 어울려요! 서로 시너지 UP!")
elif score > 55:
    st.warning("🤔 괜찮은 조합이지만 더 친해져 보세요.")
else:
    st.error("😅 조금 힘들 수 있어요. 공감 스킬을 발동해보세요!")

# 배경 애니메이션 (Balloon)
st.balloons()

# 하단 꾸미기
st.markdown("---")
st.markdown("made with ❤️ by Notischool MBTI Compatibility Team")
