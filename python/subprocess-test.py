import subprocess

# curl (GET)
res = subprocess.run(
    ["curl", "-s", "https://httpbin.org/get"], capture_output=True, text=True
)
print(res.stdout)

# ftp (anonymous接続 - LISTコマンドだけ試す)
# 注意: FTPサーバによって動かないことも多い
# subprocess.run(['ftp', '-n', 'ftp.debian.org'], input='user anonymous\nls\nbye\n', text=True)

# wget
subprocess.run(["wget", "-q", "https://httpbin.org/image/png", "-O", "image.png"])

# nc (netcat - エコーサーバに接続してデータ送信)
# 例: ローカルで `nc -l 12345` を別ターミナルで立ち上げておくと良い
subprocess.run(["nc", "localhost", "12345"], input="hello from python\n", text=True)

# ssh (パスワードなし鍵認証が前提)
subprocess.run(["ssh", "user@host", "echo Hello from SSH!"])
