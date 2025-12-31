import requests
import time
import os

def start_extraction():
    # GitHub Secrets se tumhara khufia Token uthayega
    raw_tokens = os.getenv("NP_TOKENS")
    if not raw_tokens:
        print("Error: No Token Found in Secrets!")
        return
    
    tokens = raw_tokens.split(",")
    print(f"Shadow Army: {len(tokens)} Nodes Active.")
    
    while True:
        for token in tokens:
            headers = {
                "Authorization": f"Bearer {token.strip()}",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            try:
                # Nodepay ke server ko 'Alive' signal bhejna
                r = requests.post("https://api.nodepay.ai/api/auth/session", headers=headers, timeout=15)
                if r.status_code == 200:
                    print("Status: Connected. Extracting Value...")
                else:
                    print(f"Connection Status: {r.status_code}")
            except Exception as e:
                print(f"Matrix Glitch: {e}")
        
        # 10 minute ka intezar taaki system ko shak na ho
        print("Engine Sleeping for 10 minutes...")
        time.sleep(600)

if __name__ == "__main__":
    start_extraction()
