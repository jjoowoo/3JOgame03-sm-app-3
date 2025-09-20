import streamlit as st

st.set_page_config(page_title="해수면 상승 시뮬레이션", layout="centered")

if "stage" not in st.session_state:
    st.session_state.stage = 0
    st.session_state.score = 50  # 지속가능 지수 (0~100)

st.title("🌊 해수면 상승 & 바다오염 시뮬레이션")
st.write("당신은 해안 도시의 시장입니다. 도시를 지켜내야 합니다!")

# 단계별 시나리오
scenarios = [
    {
        "text": "해수면이 10cm 상승했습니다. 주민들이 불안해합니다. 무엇을 하시겠습니까?",
        "options": {
            "방파제 건설 (예산 감소, 안정 ↑)": 10,
            "예산 절약 (주민 불만 ↑)": -15
        }
    },
    {
        "text": "바닷속에서 미세플라스틱이 발견되었습니다.",
        "options": {
            "플라스틱 규제 정책 시행 (환경 개선 ↑)": 20,
            "무시 (환경 악화 ↓)": -20
        }
    },
    {
        "text": "해변에 쓰레기가 쌓였습니다.",
        "options": {
            "대규모 정화 활동 (지속가능 지수 ↑)": 15,
            "그냥 둔다 (관광객 감소 ↓)": -10
        }
    }
]

if st.session_state.stage < len(scenarios):
    sc = scenarios[st.session_state.stage]
    st.subheader(sc["text"])
    for option, score_change in sc["options"].items():
        if st.button(option):
            st.session_state.score += score_change
            st.session_state.stage += 1
            st.rerun()
else:
    st.subheader("📊 최종 결과")
    st.write(f"당신의 지속가능 지수는 **{st.session_state.score}점** 입니다.")
    if st.session_state.score >= 80:
        st.success("🌟 훌륭합니다! 도시는 안전하고 지속가능합니다.")
    elif st.session_state.score >= 50:
        st.warning("😐 도시가 간신히 버티고 있습니다. 더 많은 노력이 필요합니다.")
    else:
        st.error("💀 도시가 해수면 상승과 오염에 무너졌습니다...")

    if st.button("🔄 다시 시작"):
        st.session_state.stage = 0
        st.session_state.score = 50
        st.rerun()
