import pytest

import accounts
from customer_report import customer_report


@pytest.fixture(autouse=True)
def accounts_table(monkeypatch):
    monkeypatch.setattr(accounts, "ACCOUNTS_TABLE", [
        {"acct_id": 1, "full_name": "Ada Lovelace", "joined_on": "2021-03-04", "spend_pence": 125000, "status": "A"},
        {"acct_id": 2, "full_name": "Alan Turing", "joined_on": "2022-07-19", "spend_pence": 4550, "status": "A"},
        {"acct_id": 3, "full_name": "Grace Hopper", "joined_on": "2020-01-30", "spend_pence": 88000, "status": "C"},
        {"acct_id": 4, "full_name": "Edsger Dijkstra", "joined_on": "2023-11-02", "spend_pence": 1200, "status": "S"},
    ])


def test_text_report_lists_active_customers():
    assert [line.split() for line in customer_report("text").splitlines()] == [
        ["Ada", "Lovelace", "2021-03-04", "1250.00"],
        ["Alan", "Turing", "2022-07-19", "45.50"],
    ]


def test_csv_report_lists_active_customers():
    assert customer_report("csv").splitlines() == [
        "name,joined,spend",
        "Ada Lovelace,2021-03-04,1250.00",
        "Alan Turing,2022-07-19,45.50",
    ]


def test_rejects_unknown_formats():
    with pytest.raises(ValueError):
        customer_report("pdf")
