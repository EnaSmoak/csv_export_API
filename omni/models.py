from datetime import datetime
from dataclasses import dataclass
import marshmallow_dataclass
import marshmallow.validate


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


TransferdetilsSchema = marshmallow_dataclass.class_schema(TransferDetails)
