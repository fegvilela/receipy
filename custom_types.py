from typing import NewType, TypedDict


IssuerName = NewType("IssuerName", str)
IssuerCPF = NewType("IssuerCPF", str)
IssuerCRP = NewType("IssuerCRP", str)


class Issuer(TypedDict):
    name: IssuerName
    cpf: IssuerCPF
    crp: IssuerCRP


PacientName = NewType("PacientName", str)
SessionCost = NewType("SessionCost", int)
SessionDate = NewType("SessionDate", str)
SessionWrittenCost = NewType("SessionWrittenCost", str)


class Sessions(TypedDict):
    name: PacientName
    cost: SessionCost
    dates: list[SessionDate]


class Session(TypedDict, total=False):
    name: PacientName
    cost: SessionCost
    date: SessionDate
    written_cost: SessionWrittenCost
