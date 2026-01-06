import streamlit as st
from model_4 import MyModel             # 분리된 로직 파일 import

st.set_page_config(page_title="구조화된 AI 앱", page_icon="🏗️")

st.title("🏗️ 구조화된 AI 앱 (FastAPI 준비)")
st.info("UI 코드와 모델 로직(model.py)을 분리하여 개발하는 패턴입니다.")

# [Caching] 클래스 인스턴스도 캐싱 가능
@st.cache_resource
def get_model_instance():
    return MyModel()

model = get_model_instance()

# 미션3 = 금지어 UI에서 입력 받기
st.sidebar.header("금지어 설정")
user_keywords = st.sidebar.text_input("쉼표로 구분", "광고,무료,당첨")

keyword_list = [s.strip() for s in user_keywords.split(",")]

# UI 구성
text = st.text_input("스팸 메일인지 테스트할 문장 입력")

if st.button("검사"):
    # 분리된 model.py의 함수 호출
    result = model.predict(text, keyword_list)

    st.json(result)         # 결과를 JSON 형태로 출력

    # 미션2 = 감지된 이유 알려주기
    st.info(f"감지결과: {result['reason']}")

    if result['is_spam']:
        st.warning("스팸일 확률이 높습니다!")
    else:
        st.success("정상적인 메시지입니다.")    