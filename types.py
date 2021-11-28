from typing import NewType, TypedDict


IssuerName = NewType("IssuerName", str)
IssuerCPF = NewType("IssuerCPF", str)
IssuerCRP = NewType("IssuerCRP", str)


class Issuer(TypedDict):
    name: IssuerName
    cpf: IssuerCPF
    crp: IssuerCRP


PacientName = NewType("PacientName", str)
PacientCPF = NewType("PacientCPF", str)
SessionCost = NewType("SessionCost", int)
SessionDate = NewType("SessionDate", str)


class Sessions(TypedDict):
    name: PacientName
    cpf: PacientCPF
    cost: SessionCost
    dates: list[SessionDate]
