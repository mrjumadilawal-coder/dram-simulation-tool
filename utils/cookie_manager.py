from streamlit_cookies_manager import EncryptedCookieManager

def get_cookie_manager():
    cookies = EncryptedCookieManager(
        prefix="dram_app_",
        password="secret_key_123"
    )

    if not cookies.ready():
        return None

    return cookies