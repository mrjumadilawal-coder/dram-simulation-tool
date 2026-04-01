import os
import uuid
from services.location_service import get_user_country

FILE_PATH = "data/visitors.txt"

# ============================================
# LOAD VISITOR
# ============================================

def load_visitors():
    if not os.path.exists(FILE_PATH):
        return set()

    with open(FILE_PATH, "r") as f:
        return set(line.strip() for line in f.readlines())

# ============================================
# SAVE VISITOR (WITH COUNTRY)
# ============================================

def save_visitor(user_id):
    country = get_user_country()

    with open(FILE_PATH, "a") as f:
        f.write(f"{user_id}|{country}\n")

# ============================================
# TOTAL VISITOR
# ============================================

def get_unique_visitor_count(cookies):
    visitors = load_visitors()

    user_id = cookies.get("user_id")

    if not user_id:
        user_id = str(uuid.uuid4())
        cookies["user_id"] = user_id
        cookies.save()

    if user_id not in visitors:
        save_visitor(user_id)
        visitors.add(user_id)

    return len(visitors)

# ============================================
# COUNTRY STATS
# ============================================

def get_country_stats():
    if not os.path.exists(FILE_PATH):
        return {}

    user_country_map = {}

    with open(FILE_PATH, "r") as f:
        for line in f:
            parts = line.strip().split("|")

            if len(parts) == 2:
                user_id, country = parts
            else:
                continue

            # hanya ambil pertama kali (biar unik)
            if user_id not in user_country_map:
                user_country_map[user_id] = country

    # hitung per country
    stats = {}
    for country in user_country_map.values():
        stats[country] = stats.get(country, 0) + 1

    return stats