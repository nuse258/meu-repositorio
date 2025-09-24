from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Literal


Color = Literal["vermelho", "preto", "verde"]
BetType = Literal["cor", "número"]


@dataclass(frozen=True)
class RouletteOutcome:
    number: int
    color: Color


class RouletteGame:
    """Implementa uma roleta europeia com opções básicas de aposta."""

    RED_NUMBERS = {
        1,
        3,
        5,
        7,
        9,
        12,
        14,
        16,
        18,
        19,
        21,
        23,
        25,
        27,
        30,
        32,
        34,
        36,
    }

    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()

    def spin_wheel(self) -> RouletteOutcome:
        number = self._rng.randint(0, 36)
        color: Color
        if number == 0:
            color = "verde"
        elif number in self.RED_NUMBERS:
            color = "vermelho"
        else:
            color = "preto"
        return RouletteOutcome(number=number, color=color)

    def calculate_payout(
        self, bet_type: BetType, bet_choice: str, bet: float, outcome: RouletteOutcome
    ) -> float:
        if bet <= 0:
            raise ValueError("A aposta deve ser positiva.")

        if bet_type == "número":
            try:
                expected_number = int(bet_choice)
            except ValueError as exc:  # pragma: no cover - validação simples
                raise ValueError("Aposta por número inválida.") from exc
            if not 0 <= expected_number <= 36:
                raise ValueError("O número deve estar entre 0 e 36.")
            if expected_number == outcome.number:
                return bet * 35
            return 0.0

        if bet_type == "cor":
            normalized_choice = bet_choice.strip().lower()
            if normalized_choice not in {"vermelho", "preto"}:
                raise ValueError("Apenas apostas em vermelho ou preto são permitidas.")
            if normalized_choice == outcome.color:
                return bet * 2
            return 0.0

        raise ValueError("Tipo de aposta desconhecido.")

    def play(self, bet_type: BetType, bet_choice: str, bet: float) -> tuple[RouletteOutcome, float]:
        outcome = self.spin_wheel()
        payout = self.calculate_payout(bet_type, bet_choice, bet, outcome)
        return outcome, payout
