from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Player:
    """Representa um jogador do casino."""

    name: str
    balance: float

    def can_place_bet(self, amount: float) -> bool:
        """Verifica se o jogador tem saldo suficiente para apostar."""
        return amount > 0 and amount <= self.balance

    def debit(self, amount: float) -> None:
        """Remove um valor do saldo do jogador."""
        if amount <= 0:
            raise ValueError("O valor do débito deve ser positivo.")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente para realizar o débito.")
        self.balance -= amount

    def credit(self, amount: float) -> None:
        """Adiciona um valor ao saldo do jogador."""
        if amount <= 0:
            raise ValueError("O valor do crédito deve ser positivo.")
        self.balance += amount
