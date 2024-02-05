import accounts


def customer_report():
    lines = []
    for name, joined, spend, active in accounts.LEGACY_CUSTOMERS:
        if active:
            lines.append(f"{name:<15} {joined}  {spend:>9.2f}")
    return "\n".join(lines)
