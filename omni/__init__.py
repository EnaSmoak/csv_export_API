import csv
import tempfile
from typing import List
from datetime import datetime
from io import StringIO
import hug
from marshmallow import fields
from . import sample, models


def gen_instr(transfers: List[models.TransferDetails]):
    with StringIO() as csvfile:
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
        return csvfile.getvalue()


@hug.post("/transactiondetails")
def transactiondetails(
    transfers: hug.types.MarshmallowInputSchema(models.TransferDetailsSchema(many=True))
) -> models.CSVResponse():
    return {"csv": gen_instr([sample.TRANSFER])}
