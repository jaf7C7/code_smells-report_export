import accounts
from customer_report import customer_report


def test_lists_active_customers(monkeypatch):
    monkeypatch.setattr(accounts, "ACCOUNTS_TABLE", [
        {"acct_id": 1, "full_name": "Ada Lovelace", "signup": "2021-03-04", "spend_pence": 125000, "status": "A"},
        {"acct_id": 3, "full_name": "Grace Hopper", "signup": "2020-01-30", "spend_pence": 88000, "status": "C"},
        {"acct_id": 4, "full_name": "Edsger Dijkstra", "signup": "2023-11-02", "spend_pence": 1200, "status": "S"},
    ])
    assert [line.split() for line in customer_report().splitlines()] == [
        ["Ada", "Lovelace", "2021-03-04", "1250.00"],
    ]
