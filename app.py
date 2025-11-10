import streamlit as st
import sys
import os

# 添加自定义模块路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'pages'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'components'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# 导入自定义模块
from utils.state_manager import initialize_app_state, get_current_page, navigate_to
from components.header import show_header

def main():
    # 应用配置
    st.set_page_config(
        page_title="音乐文化探险",
        page_icon="🎵",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # 初始化应用状态
    initialize_app_state()
    
    # 显示页面头部（进度、星星等）
    show_header()
    
    # 根据当前页面显示不同内容
    current_page = get_current_page()
    
    # 页面路由
    if current_page == "welcome":
        from pages.welcome import show_welcome_page
        show_welcome_page()
        
    elif current_page == "map_explorer":
        from pages.map_explorer import show_map_explorer_page
        show_map_explorer_page()
        
    elif current_page == "drawing_challenge":
        from pages.drawing_challenge import show_drawing_challenge_page
        show_drawing_challenge_page()
        
    elif current_page == "music_player":
        from pages.music_player import show_music_player_page
        show_music_player_page()
        
    elif current_page == "video_quiz":
        from pages.video_quiz import show_video_quiz_page
        show_video_quiz_page()
        
    elif current_page == "text_challenge":
        from pages.text_challenge import show_text_challenge_page
        show_text_challenge_page()
        
    elif current_page == "rewards":
        from pages.rewards import show_rewards_page
        show_rewards_page()
    
    # 调试信息（开发时使用）
    if st.sidebar.checkbox("显示调试信息", False):
        st.sidebar.write("当前页面:", current_page)
        st.sidebar.write("用户数据:", st.session_state.user_data)

if __name__ == "__main__":
    main()