from typing import NewType, TypedDict


IssuerName = NewType("IssuerName", str)
IssuerCPF = NewType("IssuerCPF", str)
IssuerCRP = NewType("IssuerCRP", str)
IssuerAddress = NewType("IssuerAddress", str)
IssuerTelephone = NewType("IssuerTelephone", str)


class Issuer(TypedDict):
    name: IssuerName
    cpf: IssuerCPF
    crp: IssuerCRP
    address: IssuerAddress
    telephone: IssuerTelephone


PacientName = NewType("PacientName", str)
PacientCPF = NewType("PacientCPF", str)
SessionCost = NewType("SessionCost", int)
SessionDate = NewType("SessionDate", str)
SessionWrittenCost = NewType("SessionWrittenCost", str)


class Sessions(TypedDict):
    name: PacientName
    cpf: PacientCPF
    cost: SessionCost
    dates: list[SessionDate]


class Session(TypedDict, total=False):
    name: PacientName
    cpf: PacientCPF
    cost: SessionCost
    date: SessionDate
    written_cost: SessionWrittenCost
