from __future__ import annotations

import random
from dataclasses import dataclass


SYMBOLS = ("🍒", "🍋", "🔔", "⭐", "7️⃣")


@dataclass(frozen=True)
class SlotSpin:
    symbols: tuple[str, str, str]

    @property
    def is_jackpot(self) -> bool:
        return len(set(self.symbols)) == 1

    @property
    def has_pair(self) -> bool:
        return len(set(self.symbols)) == 2


class SlotMachineGame:
    """Implementa uma slot machine simples."""

    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()

    def spin(self) -> SlotSpin:
        """Realiza uma rotação e devolve o resultado."""
        return SlotSpin(tuple(self._rng.choice(SYMBOLS) for _ in range(3)))

    def calculate_payout(self, spin: SlotSpin, bet: float) -> float:
        """Calcula o prémio de acordo com o resultado da rotação."""
        if bet <= 0:
            raise ValueError("A aposta deve ser positiva.")
        if spin.is_jackpot:
            return bet * 5
        if spin.has_pair:
            return bet * 2
        return 0.0

    def play(self, bet: float) -> tuple[SlotSpin, float]:
        """Executa a jogada completa da slot machine."""
        spin = self.spin()
        payout = self.calculate_payout(spin, bet)
        return spin, payout
