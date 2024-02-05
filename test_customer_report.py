import accounts
from customer_report import customer_report


def test_lists_active_customers(monkeypatch):
    monkeypatch.setattr(accounts, "LEGACY_CUSTOMERS", [
        ("Ada Lovelace", "2021-03-04", 1250.00, True),
        ("Grace Hopper", "2020-01-30", 880.00, False),
    ])
    assert [line.split() for line in customer_report().splitlines()] == [
        ["Ada", "Lovelace", "2021-03-04", "1250.00"],
    ]
