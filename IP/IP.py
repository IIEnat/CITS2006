import os
import requests
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv('ABUSEIPDB_API_KEY')

if not API_KEY:
    raise ValueError("ABUSEIPDB_API_KEY not found in .env file")

API_URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip(ip):
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }

    headers = {
        'Key': API_KEY,
        'Accept': 'application/json'
    }

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        print(f"\nResults for {ip}:")
        print(f"  - Abuse Confidence Score: {data['abuseConfidenceScore']}")
        print(f"  - Country: {data.get('countryCode', 'N/A')}")
        print(f"  - ISP: {data.get('isp', 'N/A')}")
        print(f"  - Domain: {data.get('domain', 'N/A')}")
        print(f"  - Last Reported: {data.get('lastReportedAt', 'N/A')}")
    else:
        print(f"\nFailed to check {ip}: {response.text}")


def main():
    print("Real-Time IP Reputation Checker (AbuseIPDB)")
    print("Type 'exit' to quit.\n")

    while True:
        ip = input("Enter an IP address to check: ").strip()
        if ip.lower() == 'exit':
            break
        check_ip(ip)


if __name__ == "__main__":
    main()
