import os
import uuid

FILE_PATH = "data/visitors.txt"


def load_visitors():
    if not os.path.exists(FILE_PATH):
        return set()

    with open(FILE_PATH, "r") as f:
        return set(line.strip() for line in f.readlines())


def save_visitor(user_id):
    with open(FILE_PATH, "a") as f:
        f.write(user_id + "\n")


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