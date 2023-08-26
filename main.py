# from dotenv import load_dotenv
# load_dotenv()

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("네가 좋아하는 동물은!")
# print(result)

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
# result = chat_model.predict("네가 좋아하는 동물은")

# content = "코딩"
# result = chat_model.predict(content+"에 대한 시를 써줘")

# print(result)

import streamlit as st

st.title('코딩하는 시인의 세계')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

content = st.text_input('시의 주제를 제시하세요', '')
st.write('시의 주제는 "', content, '" 입니다.' )

if st.button('시 작성 요청하기'):
    with st.spinner('시상에 잠긴 중...'):
        result = chat_model.predict(content+"에 대한 시를 써줘")
        st.write('시: ', result)
