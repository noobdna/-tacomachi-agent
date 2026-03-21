import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


class TacomachiAgent:
    def __init__(self):
        self.cf_api_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
        self.cf_account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID", "")
        self.cf_zone_id = os.getenv("CLOUDFLARE_ZONE_ID", "")

    def load_skill(self):
        try:
            with open("skill.md", "r", encoding="utf-8") as f:
                skill = f.read()
            print("[INFO] skill.md loaded:", len(skill), "chars")
        except FileNotFoundError:
            print("[WARN] skill.md not found")

    def fetch_logs(self):
        print("[INFO] Fetch logs (Cloudflare) - placeholder")
        return []

    def detect_anomaly(self, logs):
        print("[INFO] Detect anomaly - placeholder")
        return []

    def send_alert(self, anomalies):
        if anomalies:
            print("[ALERT] anomaly detected")
        else:
            print("[INFO] no anomaly")

    def run(self):
        print("=== Tacomachi Agent Start ===")
        print("Time:", datetime.now())

        print("Token set:", bool(self.cf_api_token))
        print("Account ID set:", bool(self.cf_account_id))
        print("Zone ID set:", bool(self.cf_zone_id))

        self.load_skill()

        logs = self.fetch_logs()
        anomalies = self.detect_anomaly(logs)
        self.send_alert(anomalies)

        print("=== Agent End ===")


if __name__ == "__main__":
    agent = TacomachiAgent()
    agent.run()
