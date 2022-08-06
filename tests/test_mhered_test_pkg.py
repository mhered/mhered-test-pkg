from pathlib import Path

import toml
from pytest import raises

from src.mhered_test_pkg import (
    __version__,
    compare_moves,
    computer_play,
    move_msg,
    player_play,
    rock_paper_scissors,
)


def test_versions_are_in_sync():
    """Checks if tool.poetry.version in pyproject.toml and
    __version__ in mhered_test_pkg.__init__.py are in sync."""

    path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    pyproject = toml.loads(open(str(path)).read())
    pyproject_version = pyproject["tool"]["poetry"]["version"]

    init_py_version = __version__

    assert init_py_version == pyproject_version


def test_move_msg_r():
    """Checks message for r is ROCK"""
    assert move_msg("r") == "ROCK"


def test_move_msg_p():
    """Checks message for p is PAPER"""
    assert move_msg("p") == "PAPER"


def test_move_msg_s():
    """Checks message for s is SCISSORS"""
    assert move_msg("s") == "SCISSORS"


def test_compare_moves():
    """Checks outcome for all move pairs"""
    cases = [
        {
            "player": "r",
            "computer": "s",
            "outcome": "win",
        },
        {
            "player": "r",
            "computer": "p",
            "outcome": "lose",
        },
        {
            "player": "r",
            "computer": "r",
            "outcome": "tie",
        },
        {
            "player": "p",
            "computer": "r",
            "outcome": "win",
        },
        {
            "player": "p",
            "computer": "s",
            "outcome": "lose",
        },
        {
            "player": "p",
            "computer": "p",
            "outcome": "tie",
        },
        {
            "player": "s",
            "computer": "p",
            "outcome": "win",
        },
        {
            "player": "s",
            "computer": "r",
            "outcome": "lose",
        },
        {
            "player": "s",
            "computer": "s",
            "outcome": "tie",
        },
    ]

    for case in cases:
        assert compare_moves(case["player"], case["computer"]) == case["outcome"]


def test_computer_play():
    """Test computer plays only 'r' 'p' 's'"""
    for i in range(100):
        assert computer_play() in ["r", "p", "s"]


def test_player_play_returns_r_p_s(monkeypatch):
    """Player_play() returns r p s"""

    # Adapted from stack overflow: monkeypatching user input
    # https://stackoverflow.com/questions/52248499/pytest-how-to-test-a-separate-function-with-input-call
    # monkeypatch the "input" function, so that it returns "r".
    # This simulates the user entering "r" in the terminal:

    for user_input in ["r", "s", "p"]:
        monkeypatch.setattr("builtins.input", lambda prompt="": user_input)
        # go about using input() like you normally would:
        player_move = player_play()
        assert player_move == user_input


def test_player_play_exits_with_q(monkeypatch):
    """Player_play exits with q"""
    # Adapted from python-pandemonium: testing for sys exit
    # https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f

    with raises(SystemExit) as pytest_wrapped_e:
        monkeypatch.setattr("builtins.input", lambda prompt="": "q")
        player_move = player_play()
    assert pytest_wrapped_e.type == SystemExit
    # assert pytest_wrapped_e.value.code == 42


def test_rock_paper_scissors_overall(monkeypatch):
    """Full run"""
    # Adapted from stack overflow: iterator to simulate a sequence of inputs
    # https://stackoverflow.com/questions/53472142/pytest-user-input-simulation

    # creating iterator object
    user_inputs = iter(
        ["r", "s", "p", "r", "s", "p", "r", "s", "p", "r", "s", "p", "a", "q"]
    )

    with raises(SystemExit) as pytest_wrapped_e:
        monkeypatch.setattr("builtins.input", lambda prompt="": next(user_inputs))
        rock_paper_scissors()
    assert pytest_wrapped_e.type == SystemExit
