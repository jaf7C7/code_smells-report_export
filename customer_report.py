import accounts


def customer_report(fmt="text"):
    customers = []
    for row in accounts.ACCOUNTS_TABLE:
        if row["status"] == "A":
            customers.append((row["full_name"], row["joined_on"], row["spend_pence"] / 100))
    total = sum(spend for _, _, spend in customers)

    if fmt == "csv":
        lines = ["name,joined,spend"]
        lines += [f"{name},{joined},{spend:.2f}" for name, joined, spend in customers]
        lines.append(f"Total,,{total:.2f}")
        return "\n".join(lines)
    if fmt == "text":
        lines = [f"{name:<15} {joined}  {spend:>9.2f}" for name, joined, spend in customers]
        lines.append(f"{'Total':<15} {'':10}  {total:>9.2f}")
        return "\n".join(lines)
    raise ValueError(f"Unknown format: {fmt}")
