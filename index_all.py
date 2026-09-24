import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="나의 개발 포트폴리오",
    page_icon="💻",
    layout="wide",
)

# 2. 사이드바 (프로필 및 연락처 정보)
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300", caption="프로필 사진")
    st.title("정윤성")
    st.markdown("**Junior Python Developer**")
    
    st.divider()
    st.markdown("### 📬 Contact")
    st.markdown("- **Email:** saysjeong@gmail.com")
    

# 3. 메인 화면 - 소개 섹션
st.title("👋 안녕하세요, 개발자 정윤성입니다!")
st.write("""
문제를 해결하는 코드를 작성하고, 사용자 중심의 웹 서비스 만드는 것을 좋아하는 개발자입니다.  
데이터베이스를 사용하지 않고 파이썬과 Streamlit만으로 가볍고 직관적인 포트폴리오 웹사이트를 구축했습니다.
""")

st.divider()

# 4. 스택 섹션 (보유 기술)
st.subheader("🛠️ Tech Stack")
col1, col2 = st.columns(2)

with col1:
    st.text("Python")
    st.progress(90) # 숙련도 조절 (0~100)
    st.text("Streamlit")
    st.progress(85)

with col2:
    st.text("Git / GitHub")
    st.progress(80)
    st.text("HTML / CSS")
    st.progress(60)

st.divider()

# 5. 프로젝트 소개 섹션
st.subheader("🚀 Projects")

# 프로젝트 1
with st.container():
    st.markdown("### 1. 개별공시지가 조회 시스템")
    st.write("**사용 기술:** Python, Streamlit")
    st.write("Open API를 활용해 최신 개별공시지가를 확인할 수 있습니다.")
    # 프로젝트 관련 링크나 버튼을 추가할 수 있습니다.
    st.button("프로젝트 1 상세보기", key="p1")
    
    st.link_button(
    label="(프로젝트 1) 개별공시지가 조회 시스템 바로가기", 
    url="https://landpriceproject-4aem4x4hcrskcadpxbaxb3.streamlit.app"         
)


st.markdown("---")

# 프로젝트 2
with st.container():
    st.markdown("### 2. 날씨 정보 시각화 대시보드")
    st.write("**사용 기술:** Python, Requests, Streamlit")
    st.write("Open API를 활용해 실시간 날씨 데이터를 가져와 그래프와 아이콘으로 시각화해 주는 대시보드입니다.")
    st.button("프로젝트 2 상세보기", key="p2")

# 6. 하단 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 Says-jeong. All rights reserved.</p>", unsafe_allow_html=True)
