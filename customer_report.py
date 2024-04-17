import accounts


def customer_report():
    lines = []
    for row in accounts.ACCOUNTS_TABLE:
        if row["status"] == "A":
            spend = row["spend_pence"] / 100
            lines.append(f"{row['full_name']:<15} {row['signup']}  {spend:>9.2f}")
    return "\n".join(lines)
