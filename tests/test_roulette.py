import pytest

from casino.games.roulette import RouletteGame, RouletteOutcome


def test_roulette_win_number():
    game = RouletteGame()
    outcome = RouletteOutcome(number=17, color="preto")
    assert game.calculate_payout("número", "17", 5.0, outcome) == 175.0


def test_roulette_lose_number():
    game = RouletteGame()
    outcome = RouletteOutcome(number=5, color="vermelho")
    assert game.calculate_payout("número", "17", 5.0, outcome) == 0.0


def test_roulette_win_color():
    game = RouletteGame()
    outcome = RouletteOutcome(number=8, color="preto")
    assert game.calculate_payout("cor", "Preto", 10.0, outcome) == 20.0


def test_roulette_invalid_color_choice():
    game = RouletteGame()
    outcome = RouletteOutcome(number=8, color="preto")
    with pytest.raises(ValueError):
        game.calculate_payout("cor", "azul", 10.0, outcome)


def test_roulette_invalid_number_choice():
    game = RouletteGame()
    outcome = RouletteOutcome(number=8, color="preto")
    with pytest.raises(ValueError):
        game.calculate_payout("número", "40", 10.0, outcome)
