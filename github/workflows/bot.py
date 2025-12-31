import requests
import time
import os

# Kira's Shadow Protocol - NewWorldFounder Edition
def start_extraction():
    # Yahan tumhare khufia Tokens aayenge (NP_TOKEN)
    tokens = os.getenv("NP_TOKENS").split(",")
    
    print(f"Shadow Army Size: {len(tokens)} Workers")
    
    while True:
        for i, token in enumerate(tokens):
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            # System Breach: Pinging the Nodepay Grid
            try:
                response = requests.post("https://api.nodepay.ai/api/auth/session", headers=headers, timeout=10)
                if response.status_code == 200:
                    print(f"Worker {i+1}: Data Extracted. Aura: 100%")
                else:
                    print(f"Worker {i+1}: Connection Glitch. Retrying...")
            except:
                pass
        
        # 10 minute ka sabr (Matrix Detection se bachne ke liye)
        time.sleep(600)

if __name__ == "__main__":
    start_extraction()
