import streamlit as st
from api_client import api_client

def main():
    st.set_page_config(
        page_title="世界乐器探索",
        page_icon="🎵",
        layout="wide"
    )
    
    # 应用标题
    st.title("🌍 世界乐器探索")
    st.markdown("欢迎来到奇妙的世界乐器之旅！")
    
    # 检查API连接
    if not api_client.health_check():
        st.error("无法连接到API服务")
        return
    
    # 获取乐器数据
    instruments = api_client.get_instruments()
    
    # 显示乐器
    st.header("🎵 世界乐器")
    for instrument in instruments:
        with st.expander(f"{instrument['name']} - {instrument['country']}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(instrument['description'])
                audio_url = api_client.get_audio_url(instrument['id'])
                st.audio(audio_url)
                
            with col2:
                if st.button(f"学习{instrument['name']}", key=instrument['id']):
                    show_learning_page(instrument)

def show_learning_page(instrument):
    """显示学习页面"""
    st.header(f"🎵 {instrument['name']}")
    
    # 获取相关问题
    question = api_client.get_quiz_question(instrument['id'])
    if question:
        st.subheader("知识测试")
        st.write(f"**{question['question']}**")
        
        selected = st.radio("选择答案:", question['options'])
        
        if st.button("提交答案"):
            result = api_client.submit_answer(question['id'], selected)
            if result:
                if result['is_correct']:
                    st.success("✅ 回答正确！")
                else:
                    st.error("❌ 回答错误")
                st.write(f"**解释:** {result['explanation']}")

if __name__ == "__main__":
    main()
