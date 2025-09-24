from casino.games.slot_machine import SlotMachineGame, SlotSpin


def test_slot_machine_jackpot():
    game = SlotMachineGame()
    spin = SlotSpin(("⭐", "⭐", "⭐"))
    assert game.calculate_payout(spin, 10.0) == 50.0


def test_slot_machine_pair():
    game = SlotMachineGame()
    spin = SlotSpin(("🍋", "🍋", "🍒"))
    assert game.calculate_payout(spin, 10.0) == 20.0


def test_slot_machine_loss():
    game = SlotMachineGame()
    spin = SlotSpin(("🍋", "🍒", "🔔"))
    assert game.calculate_payout(spin, 10.0) == 0.0
