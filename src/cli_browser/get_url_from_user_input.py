import re

def get_url_from_user_input(user_input: str) -> str:
    match = re.match(r"^#add\s+(.*)", user_input)
    if match:
        return match.group(1).strip()
    return ""