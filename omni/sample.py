from datetime import datetime
from . import models

TRANSFER = models.TransferDetails(
    models.Account(
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
    models.Account(
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
