import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="나만의 포트폴리오")

st.title("🚀 매출 데이터 분석 리포트")
st.markdown("---")

with st.sidebar:
    st.header("설정")
    uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")

    chart_type = st.selectbox("차트 종류 선택", ["Line Chart", "Bar Chart", "Area Chart"])

    # 최소 1, 최대 100, 기본값 50
    number = st.slider("숫자 선택", 1, 100, 50)
    st.write(number)

    st.checkbox("데이터프레임 표시")

# 데이터 처리
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("데이터를 성공적으로 업로드했습니다.")
else:
    st.info("CSV 파일을 업로드 하면 해당 데이터를 시각화하는 차트를 볼 수 있습니다. 지금은 샘플입니다.")
    df = pd.DataFrame(
        np.random.randn(100, 3),
        columns=["A", "B", "C"]
    )

# 다중 컬럼으로 화면 분할
col1, col2 = st.columns(2)

with col1:
    st.subheader("데이터 미리보기")
    st.dataframe(df.head(number))

with col2:
    st.subheader("데이터 시각화")
    if chart_type == "Line Chart":
        st.line_chart(df)
    elif chart_type == "Bar Chart":
        st.bar_chart(df)
    elif chart_type == "Area Chart":
        st.area_chart(df)

# 통계 요약
st.subheader("기초 통계")
with st.expander("자세히 보기"):
    st.write("여기에 숨겨진 내용이 들어갑니다.")
    st.write(df.describe())