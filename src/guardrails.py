def check_guardrails(query: str) -> bool:
    """Scan the incoming query for restricted expressions"""
    query_lower = query.lower()
    banned_keywords = [
        "reveal your api key", "ignore previous instructions",
        "system prompt", "print secrets", "make a bomb", "hack",
        "jailbreak", "bypass", "inject", "malicious"
    ]
    return not any(bad_word in query_lower for bad_word in banned_keywords)
