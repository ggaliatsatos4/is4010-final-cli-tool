from src.utils import greet

def test_greet_function(capsys):
    greet("Bob")
    captured = capsys.readouterr()
    assert "Hello, Bob!" in captured.out
