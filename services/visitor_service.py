import os
import uuid
from datetime import datetime
from services.location_service import get_user_country

FILE_PATH = "data/visitors.txt"

# ============================================
# LOAD VISITOR HARI INI
# ============================================

def load_visitors_today():
    if not os.path.exists(FILE_PATH):
        return set()

    today = datetime.now().strftime("%Y-%m-%d")
    visitors = set()

    with open(FILE_PATH, "r") as f:
        for line in f:
            parts = line.strip().split("|")

            # FORMAT BARU: user_id|country|date
            if len(parts) == 3:
                user_id, _, date = parts

                if date == today:
                    visitors.add(user_id)

            # FORMAT LAMA: user_id|country (anggap hari ini)
            elif len(parts) == 2:
                user_id, _ = parts
                visitors.add(user_id)

    return visitors

# ============================================
# SAVE VISITOR (WITH COUNTRY + DATE)
# ============================================

def save_visitor(user_id):
    country = get_user_country()
    today = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_PATH, "a") as f:
        f.write(f"{user_id}|{country}|{today}\n")

# ============================================
# TOTAL VISITOR (PER HARI)
# ============================================

def get_unique_visitor_count(cookies):
    visitors_today = load_visitors_today()

    user_id = cookies.get("user_id")

    # generate user_id kalau belum ada
    if not user_id:
        user_id = str(uuid.uuid4())
        cookies["user_id"] = user_id
        cookies.save()

    # hanya hitung kalau belum ada hari ini
    if user_id not in visitors_today:
        save_visitor(user_id)
        visitors_today.add(user_id)

    return len(visitors_today)

# ============================================
# COUNTRY STATS (UNIQUE USER ALL TIME)
# ============================================

def get_country_stats():
    if not os.path.exists(FILE_PATH):
        return {}

    user_country_map = {}

    with open(FILE_PATH, "r") as f:
        for line in f:
            parts = line.strip().split("|")

            if len(parts) >= 2:
                user_id = parts[0]
                country = parts[1]

                # ambil pertama kali saja (unique user)
                if user_id not in user_country_map:
                    user_country_map[user_id] = country

    stats = {}
    for country in user_country_map.values():
        stats[country] = stats.get(country, 0) + 1

    return stats