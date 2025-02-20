import requests

url = "http://localhost:10936/process_audio"
file_path = "audio.wav"
output_path = "generated_audio.wav"

# 打开文件并发送 POST 请求
with open(file_path, 'rb') as file:
    files = {'file': (file_path, file)}
    response = requests.post(url, files=files)

# 检查请求是否成功
if response.status_code == 200:
    # 将生成的音频文件保存到本地
    with open(output_path, 'wb') as output_file:
        output_file.write(response.content)
    print(f"Generated audio saved to {output_path}")
else:
    print(f"Failed to process audio. Status code: {response.status_code}")