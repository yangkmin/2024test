import streamlit as st

def mbti_info(mbti):
    data = {
        "INFJ": {
            "description": "INFJ는 선의의 조언자이자 비전을 가진 사람으로, 타인을 돕는 일을 중요하게 생각해요. 🕊️",
            "jobs": "심리상담사, 작가, 교사, 사회운동가가 잘 맞아요. 📚",
            "compatible": "INTP, ENFP와 좋은 궁합을 자랑해요. 서로의 꿈을 지지하는 조합이죠! 🌟"
        },
        "INTJ": {
            "description": "INTJ는 전략가로, 미래를 설계하는 데 강한 능력을 발휘해요. 🧠",
            "jobs": "데이터 과학자, 개발자, 경영 컨설턴트가 잘 어울려요. 💼",
            "compatible": "ENTP, ENFP와 함께하면 계획과 창의력이 어우러져 시너지를 낼 수 있어요! ⚡"
        },
        "ENTP": {
            "description": "ENTP는 아이디어 뱅크이자 논쟁을 즐기는 혁신가예요. 💡",
            "jobs": "창업가, 마케팅 전략가, 변호사가 잘 맞아요. 📈",
            "compatible": "INTJ, INFJ와 함께하면 도전적이고 창의적인 관계를 만들 수 있어요! 🔥"
        },
        "ISFP": {
            "description": "ISFP는 감성을 가진 예술가이자 평화를 사랑하는 사람입니다. 🎨",
            "jobs": "디자이너, 사진작가, 수의사가 잘 맞아요. 🌿",
            "compatible": "ESFJ, ESTJ와 잘 어울려요. 서로의 다름을 인정하고 조화를 만들어가죠. 💕"
        },
        # 다른 MBTI 유형 추가
    }
    return data.get(mbti, {
        "description": "아직 준비되지 않은 MBTI예요. 업데이트를 기대해주세요! 😅",
        "jobs": "",
        "compatible": ""
    })

# Streamlit 설정
st.title("MBTI 유형별 직업 및 궁합 맞추기 💼💖")

# MBTI 선택 드롭다운
mbti_types = ["INFJ", "INTJ", "ENTP", "ISFP"]
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요!", mbti_types)

# MBTI 설명
info = mbti_info(selected_mbti)
st.subheader(f"✨ {selected_mbti} 유형의 특징 ✨")
st.write(info["description"])

st.subheader("🏆 어울리는 직업")
st.write(info["jobs"])

st.subheader("💞 잘 맞는 사람")
st.write(info["compatible"])

st.write("---")
st.write("재미있게 봐주셨나요? MBTI는 참고용이지만, 여러분의 가능성은 무한대예요! 🚀")
