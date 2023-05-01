import streamlit as st
import pandas as pd

#pandas와 stramlit 설치 완료
#좌측 파일, 설정, 프로젝트, Python 인터프리터에서 다운받을 수 있음!
st.title('title입니다')
st.header("header입니다")
st.subheader("subheader입니다")
st.text("text입니다")
st.caption("caption입니다")
st.write("write입니다") #write는 약간 만능 느낌 안에 뭘 써도 되더라
#https://docs.streamlit.io/library/api-reference/write-magic/st.write
st.divider()

st.text("아래는 st.code(code, language='python')를 사용한 것입니다.\ncode는 '''코드'''를 사용해서 출력합니다") #preormatted text
code='''from itertools import combinations
    a=[1,2,3,4,5]
    print(combinations(a,3))'''
st.code(code, language='python')

ppap='''
여기서부터 st.markdown입니다 
markdown은 마크업 언어의 일종으로 작년에 했던 colaboratory 에서 했던 문법을 지원합니다.
즉, title, header 등과 같이 크기 등이 정해져있지 않고
샵, 샵샵, 등과 같이 썼을 때 특정 기능을 지원합니다. 예시는 아래와 같습니다
# 앞에 샵을 하나 썼을때
## 앞에 샵을 두개 썼을때
* 별을 하나 썼을때
* 별을 하나 썼을때
* markdown의 문법에 대한 자세한 내용은 나무위키 참고
\n여기까지가 st.markdown 입니다

'''
st.divider()
st.markdown(ppap)
st.divider()

st.subheader("colored text")
st.success("success입니다")
st.warning("warning입니다")
st.info("info입니다")
st.error("error입니다")
st.exception("exception입니다. 내용물을 입력하면 이 곳에 들어갑니다 볼드처리된 str:과 밑의 Traceback은 알아서 출력하는거같네요")

st.divider()
st.write("아래는 st.write(1+2)를 실행한 결과입니다")
st.write(1+2)
st.write("아래는 st.write(dir(st))를 실행한 결과입니다")
st.write(dir(st))
st.write("아래는 st.help(range)를 실행한 결과입니다")
st.help(range)
st.divider()

st.subheader("pandas")
df=pd.read_csv("sample.csv")
st.write("pandas로 csv파일을 불러오는 방법, streamlit에 출력하는 방법은 다음과 같습니다")
code='''df=pd.read_csv('경로') #df:DataFrame을 의미
st.dataframe(df)
#or
st.dataframe(df.style.highlight_max(axis=0))
st.table(df)'''
st.code(code, language='python')
st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df)