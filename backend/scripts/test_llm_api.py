
import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)
else:
    print(f"警告: 找不到 .env 文件 ({dotenv_path})")

def test_llm_api():
    print("正在从 .env 验证 LLM API 配置...")
    
    api_key = os.environ.get('LLM_API_KEY')
    base_url = os.environ.get('LLM_BASE_URL', 'https://api.openai.com/v1')
    model_name = os.environ.get('LLM_MODEL_NAME', 'gpt-4o-mini')

    if not api_key:
        print("❌ LLM_API_KEY 未配置")
        return

    print(f"使用的模型: {model_name}")
    print(f"Base URL: {base_url}")
    
    try:
        client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你好，请回复'pong'以确认 API 调用正常。"}
        ]
        
        print("正在发送请求到 LLM...")
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.7,
            max_tokens=100
        )
        
        content = response.choices[0].message.content
        print(f"LLM 响应: {content}")
        
        if 'pong' in content.lower() or '你好' in content or content.strip():
            print("✅ LLM API 调用成功！")
        else:
            print("⚠️ LLM API 响应成功，但内容为空。")
            
    except Exception as e:
        print(f"❌ LLM API 调用失败: {str(e)}")

if __name__ == "__main__":
    test_llm_api()
