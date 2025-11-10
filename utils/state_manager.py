import streamlit as st
import json
import os

def initialize_app_state():
    """初始化应用状态"""
    if 'app_initialized' not in st.session_state:
        st.session_state.app_initialized = True
        
        # 用户数据
        st.session_state.user_data = {
            'stars': 0,
            'completed_modules': [],
            'current_location': None,
            'current_instrument': None,
            'drawings': {},
            'quiz_answers': {},
            'visited_pages': ['welcome']
        }
        
        # 页面状态
        st.session_state.current_page = 'welcome'
        st.session_state.previous_page = None

def get_current_page():
    """获取当前页面"""
    return st.session_state.current_page

def navigate_to(page_name, from_page=None):
    """导航到指定页面"""
    if from_page:
        st.session_state.previous_page = from_page
    
    st.session_state.current_page = page_name
    
    # 记录访问过的页面
    if page_name not in st.session_state.user_data['visited_pages']:
        st.session_state.user_data['visited_pages'].append(page_name)
    
    # 强制重新运行以更新页面
    st.rerun()

def go_back():
    """返回上一页"""
    if st.session_state.previous_page:
        navigate_to(st.session_state.previous_page)
    else:
        navigate_to('map_explorer')

def add_stars(count):
    """添加星星"""
    st.session_state.user_data['stars'] += count

def complete_module(module_name, stars_earned=0):
    """完成一个模块"""
    if module_name not in st.session_state.user_data['completed_modules']:
        st.session_state.user_data['completed_modules'].append(module_name)
    
    if stars_earned > 0:
        add_stars(stars_earned)

def get_user_progress():
    """获取用户进度"""
    total_modules = 15  # 假设总模块数
    completed = len(st.session_state.user_data['completed_modules'])
    return {
        'completed': completed,
        'total': total_modules,
        'percentage': (completed / total_modules) * 100 if total_modules > 0 else 0,
        'stars': st.session_state.user_data['stars']
    }

def save_user_progress():
    """保存用户进度到文件"""
    try:
        with open('user_progress.json', 'w', encoding='utf-8') as f:
            json.dump(st.session_state.user_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存进度失败: {e}")

def load_user_progress():
    """从文件加载用户进度"""
    try:
        if os.path.exists('user_progress.json'):
            with open('user_progress.json', 'r', encoding='utf-8') as f:
                saved_data = json.load(f)
                st.session_state.user_data.update(saved_data)
    except Exception as e:
        print(f"加载进度失败: {e}")