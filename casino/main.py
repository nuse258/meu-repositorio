from __future__ import annotations

from casino.games.roulette import RouletteGame
from casino.games.slot_machine import SlotMachineGame
from casino.player import Player


def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            print("Valor inválido, tente novamente.")
            continue
        if value <= 0:
            print("O valor deve ser positivo.")
            continue
        return value


def main() -> None:
    print("Bem-vindo ao Casino Virtual! 🃏")
    name = input("Qual é o seu nome? ")
    player = Player(name=name or "Jogador", balance=100.0)

    slot_machine = SlotMachineGame()
    roulette = RouletteGame()

    def play_slot() -> None:
        """Jogar na slot machine"""

        if not player.can_place_bet(1):
            print("Saldo insuficiente para apostar. Adicione fundos e tente novamente.")
            return
        bet = read_float("Valor da aposta: ")
        if not player.can_place_bet(bet):
            print("Saldo insuficiente para esta aposta.")
            return
        player.debit(bet)
        spin, payout = slot_machine.play(bet)
        print(f"Resultado: {' | '.join(spin.symbols)}")
        if payout:
            print(f"Parabéns! Ganhou {payout:.2f}€.")
            player.credit(payout)
        else:
            print("Não foi desta vez. Boa sorte na próxima!")

    def play_roulette_color() -> None:
        """Apostar na roleta (cor)"""

        bet = read_float("Valor da aposta: ")
        if not player.can_place_bet(bet):
            print("Saldo insuficiente para esta aposta.")
            return
        bet_choice = input("Escolha a cor (vermelho/preto): ")
        player.debit(bet)
        outcome, payout = roulette.play("cor", bet_choice, bet)
        print(f"A bola caiu no {outcome.number} ({outcome.color}).")
        if payout:
            print(f"Parabéns! Ganhou {payout:.2f}€.")
            player.credit(payout)
        else:
            print("Não ganhou desta vez.")

    def play_roulette_number() -> None:
        """Apostar na roleta (número exato)"""

        bet = read_float("Valor da aposta: ")
        if not player.can_place_bet(bet):
            print("Saldo insuficiente para esta aposta.")
            return
        bet_choice = input("Escolha um número entre 0 e 36: ")
        player.debit(bet)
        outcome, payout = roulette.play("número", bet_choice, bet)
        print(f"A bola caiu no {outcome.number} ({outcome.color}).")
        if payout:
            print(f"Incrível! Ganhou {payout:.2f}€.")
            player.credit(payout)
        else:
            print("Não ganhou desta vez.")

    while True:
        print("\n===== Menu Principal =====")
        print(f"Saldo atual: {player.balance:.2f}€")
        print("1. Jogar slot machine")
        print("2. Apostar na roleta (cor)")
        print("3. Apostar na roleta (número)")
        print("4. Adicionar fundos")
        print("0. Sair")

        choice = input("> ").strip()
        if choice == "1":
            play_slot()
        elif choice == "2":
            play_roulette_color()
        elif choice == "3":
            play_roulette_number()
        elif choice == "4":
            amount = read_float("Quantos euros deseja adicionar? ")
            player.credit(amount)
            print(f"Novo saldo: {player.balance:.2f}€")
        elif choice == "0":
            print(f"Obrigado por jogar, {player.name}! Até a próxima.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
