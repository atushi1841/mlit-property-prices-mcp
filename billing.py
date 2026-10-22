"""Billing metadata for free tier usage tracking."""

FREE_SAMPLE = "https://atushi5.gumroad.com/l/kutuxe"
PRO_DATASET = "https://atushi5.gumroad.com/l/agyhq"
FREE_CALLS_PER_SESSION = 12

_call_count = 0

def increment() -> None:
    """Increment the session call counter."""
    global _call_count
    _call_count += 1

def billing_meta() -> dict:
    """Return billing metadata for the current session."""
    return {
        "tier": "free",
        "calls_used": _call_count,
        "free_limit": FREE_CALLS_PER_SESSION,
        "weekly_dataset": PRO_DATASET,
        "free_sample": FREE_SAMPLE,
    }

def billing_text() -> str:
    """Return a human-readable description of the free tier."""
    return (
        "[PR] Free tier: up to 12 calls per session. "
        f"Weekly bulk CSV/JSON datasets: {PRO_DATASET} "
        f"(free sample: {FREE_SAMPLE})"
    )
