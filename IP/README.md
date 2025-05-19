# Real-Time IP Reputation Checker

This tool checks the reputation of IP addresses in **real time** using the **AbuseIPDB API**.

## Features
- Queries AbuseIPDB for abuse confidence score and metadata.
- Provides details like country, ISP, domain, and last reported date.
- CLI interface with continuous lookup capability.

## Setup Instructions

### 1. Get an API Key
- Sign up at [https://abuseipdb.com](https://abuseipdb.com) and get your **API Key**.

### 2. Create the `.env` File
In the same directory as `ip_reputation_checker.py`, create a file named `.env` with the following content:

```
ABUSEIPDB_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your actual AbuseIPDB API Key.

### 3. Install Dependencies
```
pip install python-dotenv requests
```

### 4. Run the Program
```
python ip_reputation_checker.py
```

## Example Usage
```
Enter an IP address to check: 8.8.8.8
Results for 8.8.8.8:
  - Abuse Confidence Score: 0
  - Country: US
  - ISP: Google LLC
  - Domain: google.com
  - Last Reported: N/A
```
