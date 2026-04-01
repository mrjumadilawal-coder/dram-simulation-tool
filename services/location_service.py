import requests
    
def get_user_country():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        return data.get("country", "Unknown")
    except:
        return "Unknown"