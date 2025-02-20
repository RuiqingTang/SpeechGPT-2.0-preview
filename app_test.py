import requests
import argparse

# 设置命令行参数解析
parser = argparse.ArgumentParser(description="Process an audio file and save the output.")
parser.add_argument('--input_file', type=str,  default='audio.wav', help="Path to the input audio file (default: 227.wav)")
parser.add_argument('--output_file', type=str, default="generated_audio.wav", help="Path to save the generated audio file (default: generated_audio.wav)")

# 解析命令行参数
args = parser.parse_args()
url = "http://localhost:10936/process_audio"

# 打开文件并发送 POST 请求
with open(args.input_file, 'rb') as file:
    files = {'file': (args.input_file, file)}
    response = requests.post(url, files=files)

# 检查请求是否成功
if response.status_code == 200:
    # 将生成的音频文件保存到本地
    with open(args.output_file, 'wb') as output_file:
        output_file.write(response.content)
    print(f"Generated audio saved to {args.output_file}")
else:
    print(f"Failed to process audio. Status code: {response.status_code}")