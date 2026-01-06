import streamlit as st
from transformers import pipeline

st.title("🧠 AI 감성 분석기(모델 캐싱 실습)")

# Caching 모델 로딩
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="matthewburke/korean_sentiment")

# 모델 로딩
with st.spinner("AI 모델을 로딩 중입니다..."):
    classifier = load_model()

st.write("문장을 입력하면 긍정(Positive)인지 부정(Negative)인지 분석합니다.")

# 사용자의 입력 받기
user_input = st.text_area("분석할 텍스트 입력", "나는 AI 엔지니어과정이 재밌습니다.")

if st.button("분석하기"):
    if user_input:
        # 예측 수행
        result = classifier(user_input)[0]
        label = result['label']
        score = result['score']

        if label == 'LABEL_1':
            label_text = 'POSITIVE'
        else:
            label_text = 'NEGATIVE'

        # 결과 시각화
        col1, col2 = st.columns(2)
        with col1:
            st.metric('감성 결과', label_text)
        with col2:
            st.metric('확신도 (score)', f"{score:.2%}")
            st.progress(score)

        if label_text == 'POSITIVE':
            st.success("긍정적인 문장입니다! 😊")
        elif score <0.7:
            st.info("🤔 AI가 확신하지 못하는 문장입니다.")
        else:
            st.error("부정적인 문장입니다. 😞")

    else:
        st.warning("분석할 텍스트를 입력해주세요.")