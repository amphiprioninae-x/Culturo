import subprocess
import sys
import time
import webbrowser
import os

def start_backend():
    """启动后端服务"""
    print("🚀 启动后端API服务...")
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    os.chdir(backend_dir)
    
    process = subprocess.Popen([
        sys.executable, "-m", "uvicorn", 
        "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"
    ])
    
    os.chdir(os.path.dirname(__file__))
    return process

def start_frontend():
    """启动前端服务"""
    print("🎨 启动前端应用...")
    time.sleep(3)
    
    frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
    os.chdir(frontend_dir)
    
    process = subprocess.Popen([
        sys.executable, "-m", "streamlit", "run", 
        "app.py", "--server.port", "8501"
    ])
    
    os.chdir(os.path.dirname(__file__))
    return process

def main():
    print("🎵 启动世界乐器探索应用...")
    
    backend = start_backend()
    frontend = start_frontend()
    
    time.sleep(5)
    
    webbrowser.open("http://localhost:8501")
    webbrowser.open("http://localhost:8000/docs")
    
    print("✅ 应用启动成功！")
    print("📱 前端: http://localhost:8501")
    print("📚 API文档: http://localhost:8000/docs")
    print("⏹️  按 Ctrl+C 停止服务")
    
    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("🛑 停止服务...")
        backend.terminate()
        frontend.terminate()

if __name__ == "__main__":
    main()
