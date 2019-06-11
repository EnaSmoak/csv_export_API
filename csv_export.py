import csv
import hug
import tempfile
from typing import List
from dataclasses import dataclass
import marshmallow_dataclass
import marshmallow.validate
from datetime import datetime


@dataclass
class Account:
    reference: str
    bene_name: str
    bank: str
    branch: str
    address: str
    country: str
    debit_acc_number: str
    currency: str
    city: str
    activation: str
    debit_reference: str
    credit_reference: str


@dataclass
class TransferDetails:
    source: Account
    dest: Account
    amount: float
    date: datetime


def gen_instr(transfers: List[TransferDetails]):
    with open("transfer_data.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(
            ["H", "icam_corp_inst", "icam_transfer", "", "", datetime.now(), "10100"]
        )
        for transfer in transfers:
            csvwriter.writerow(
                ["D", transfer.source.reference]
                + [""] * 2
                + [transfer.source.bene_name]
                + [""] * 3
                + [
                    transfer.source.bank,
                    transfer.source.branch,
                    "",
                    transfer.dest.branch,
                    transfer.dest.address,
                    transfer.source.bank,
                    transfer.source.debit_acc_number,
                    transfer.source.currency,
                    "",
                    transfer.source.address,
                    transfer.source.country,
                    "",
                    transfer.source.city,
                ]
                + [""] * 2
                + [transfer.source.debit_acc_number, transfer.dest.currency]
                + [""] * 3
                + [transfer.amount, "", transfer.source.activation, transfer.date]
                + [""] * 9
                + [transfer.source.debit_reference, transfer.dest.credit_reference]
                + [""] * 7
            )
        csvwriter.writerow(
            ["T", len(transfers), sum(t.amount for t in transfers), "", ""]
        )


TransferdetilsSchema = marshmallow_dataclass.class_schema(TransferDetails)


@hug.get("/transactiondetails")
def transactiondetails():
    with open("transfer_data.csv", "r") as f:
        contents = f.read()

    return {"success": True, "contents": contents}


"""print(
    gen_instr(
        [
            TransferDetails(
                Account(
                    "TO00T",
                    "EnterpriseGH",
                    "GN",
                    "542601254102",
                    "GHS",
                    "EL368",
                    "Ghana",
                    "Accra",
                    "54444554878745450",
                    "active",
                    "dbt15240",
                    "crdt102021",
                ),
                Account(
                    "TO00T",
                    "EnterpriseGH",
                    "GN",
                    "542601254102",
                    "GHS",
                    "EL368",
                    "Ghana",
                    "Accra",
                    "54444554878745450",
                    "active",
                    "dbt15240",
                    "crdt102021",
                ),
                1000,
                datetime.now(),
            )
        ]
    )
)"""
