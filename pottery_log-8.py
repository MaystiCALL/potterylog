# === Stage 8: Текстовый поиск ===
# Project: PotteryLog
def search_with_highlight(items, query, field="name"):
    query = query.strip().lower()
    results = []
    for item in items:
        value = getattr(item, field, "")
        if query in value.lower():
            results.append((item, value))
    return results


def highlight_matches(text, query):
    query = query.strip().lower()
    if not query:
        return text
    parts = []
    index = 0
    lower_text = text.lower()
    while True:
        found = lower_text.find(query, index)
        if found == -1:
            parts.append(text[index:])
            break
        parts.append(text[index:found])
        parts.append(f"<mark>{text[found:found + len(query)]}</mark>")
        index = found + len(query)
    return "".join(parts)


def format_search_result(item, value, query):
    return f"{highlight_matches(value, query)}"


def render_search(items, query, field="name"):
    query = query.strip().lower()
    if not query:
        return ""
    lines = []
    for item, value in search_with_highlight(items, query, field):
        lines.append(f"- {highlight_matches(value, query)}")
    return "\n".join(lines)
