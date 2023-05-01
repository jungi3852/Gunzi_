import streamlit as st
import pandas as pd


#pandas와 stramlit 설치 완료
#좌측 파일, 설정, 프로젝트, Python 인터프리터에서 다운받을 수 있음!
st.title("프실 정리")
intro='''
2213 이준기
A+은 안될까요
'''
st.text("2213 이준기")
code='''st.title('title입니다')
st.header("header입니다")
st.subheader("subheader입니다")
st.text("text입니다")
st.caption("caption입니다")
st.write("write입니다")'''
st.code(code,language='python')
st.title('title입니다')
st.header("header입니다")
st.subheader("subheader입니다")
st.text("text입니다")
st.caption("caption입니다")
st.write("write입니다") #write는 약간 만능 느낌 안에 뭘 써도 되더라
#https://docs.streamlit.io/library/api-reference/write-magic/st.write
st.divider()


st.header("code")
st.text("아래는 st.code(code, language='python')를 사용한 것입니다.\ncode는 '''코드'''를 사용해서 출력합니다") #preormatted text
code='''from itertools import combinations
    a=[1,2,3,4,5]
    print(combinations(a,3))'''
st.code(code, language='python')


st.divider()
st.header('markdown')
st.write('https://namu.wiki/w/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4')
ppap='''st.markdown(something)
something="blablabla(with markdown grammer)"'''
st.code(ppap,language='python')
code='''
markdown은 마크업 언어의 일종으로 작년에 했던 colaboratory 에서 했던 문법을 지원합니다.
즉, title, header 등과 같이 크기 등이 정해져있지 않고
샵, 샵샵, 등과 같이 썼을 때 특정 기능을 지원합니다. 예시는 아래와 같습니다
# 앞에 샵을 하나 썼을때
## 앞에 샵을 두개 썼을때
* 별을 하나 썼을때
* 별을 하나 썼을때
* markdown의 문법에 대한 자세한 내용은 나무위키 참고
'''
st.markdown(code)
st.divider()


st.header("colored text")
code='''st.success("success입니다") #green
st.warning("warning입니다") #yellow
st.info("info입니다") #blue
st.error("error입니다") #red
st.exception("exception입니다. 내용물을 입력하면 이 곳에 들어갑니다 볼드처리된 str:과 밑의 Traceback은 알아서 출력하는거같네요")
'''
st.code(code,language='python')
st.success("success입니다")
st.warning("warning입니다")
st.info("info입니다")
st.error("error입니다")
st.exception("exception입니다. 내용물을 입력하면 이 곳에 들어갑니다 볼드처리된 str:과 밑의 Traceback은 알아서 출력하는거같네요")


st.divider()
st.header("write, help")
code='''
st.write(1+2)
st.write(dir(st))
st.help(range)'''
st.code(code,language='python')
st.write(1+2)
st.write(dir(st))
st.help(range)
st.divider()


st.header("pandas")
df=pd.read_csv("sample.csv")
st.write("pandas로 csv파일을 불러오는 방법, streamlit에 출력하는 방법은 다음과 같습니다")
code='''df=pd.read_csv(이름) #df:DataFrame을 의미
st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0)) #axis=0 : 행 방향(세로줄끼리 비교)
#위 코드 해석: 각 세로줄마다 최대값 highlight
#만약 axis=1을 한다면? str과 int를 비교하므로 에러남
st.table(df)
#pd.read_csv에 대해...
#local에서만 쓸거면 pd.read_csv()에 경로만 넣어도 됨, 허나 서버에서는 사용 불가
#서버에서 쓰려면 github및 내 프로젝트 폴더에 csv파일을 넣어놔야 함!
#하는법: pycharm 왼쪽 프로젝트 data_app(실행하는.py가 있는 폴더) 클릭 후 파일 복사한 상태에서 ctrl.v'''
st.code(code, language='python')
st.write("실행 결과입니다")
st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df)
st.divider()


st.header('display json')
st.write('https://namu.wiki/w/JSON 참고')
code='''st.json({'data': 'name'})
#엑셀보다 효율적이라더나 뭐라나... 뭐 잘 모르겠고
#다음주에 설명해주신답니다~
#json 스쳐지나가는거 보니까 나와봤자 1문제?'''
st.code(code,language='python')
st.json({'data': 'name'}) #출력은 큰따옴표로 됨, 큰따옴표가 안정적이다 뭐라나...암튼 json쓸때는 큰따옴표 쓰랍니다~
st.write()
st.divider()


st.header("columns")
code='''col1,col2,col3=st.columns(3)
col1.metric("Temperature","70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity","86%","4%")
'''
st.code(code,language='python')
col1,col2,col3=st.columns(3)
col1.metric("Temperature","70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity","86%","4%")
st.divider()

st.header("button")
name='Lee Jun Gi'
code='''name='Lee Jun Gi'
if st.button("응애", key=1):
    st.write(f'Name: {name}')
if st.button("응애", key=2):
    st.write(f'Name: {name}')
#key에 특별한 의미는 없는 것 같음... st.button(내용, key=뭐시기)
#key가 같은게 여러개일 수는 없는듯, 오류남
#중복 선택은 안되는 듯 합니다
#st.button()은 true, false값을 가진다
'''
st.code(code,language='python')
if st.button("응애", key=1):
    st.write(f'Name: {name}')
if st.button("응애", key=2):
    st.write(f'Name: {name}')
st.divider()


st.header("radio button")
code='''titan=st.radio('다음 중 에렌 예거가 소지한 거인이 아닌 것은?', ('진격의 거인','턱 거인','시조의 거인','전퇴의 거인'))
if titan=="턱 거인":
    st.success("정답입니다")
else:st.error("오답입니다")
#st.radio()는 특정 값(선택지)을 가진다
'''
st.code(code,language='python')
titan=st.radio('다음 중 에렌 예거가 소지한 거인이 아닌 것은?', ('진격의 거인','턱 거인','시조의 거인','전퇴의 거인'))
if titan=="턱 거인":
    st.success("정답입니다")
else:st.error("오답입니다")
st.divider()


st.header('checkbox')
code='''cb=st.checkbox('눌러요')
if cb is True:
    st.write('잘했다')
else:st.write('눌러라고')
#st.checkbox는 true false값을 가진다'''
st.code(code,language='python')
cb=st.checkbox('눌러요')
if cb is True:
    st.write('잘했다')
else:st.write('눌러라고')
st.divider()


st.header('selectbox')
code='''selectlist=['아','무','거나','골라','요']
sb=st.selectbox('선택해', selectlist)
st.write(f'너가 선택한건 {sb}입니다')
#st.selectlist()은 특정 값(선택지)를 가진다
'''
st.code(code,language='python')
selectlist=['조서현','이준기','이용현','신지호','김강민']
sb=st.selectbox('선택해', selectlist)
st.write(f'당신의 남친은 {sb}입니다')
