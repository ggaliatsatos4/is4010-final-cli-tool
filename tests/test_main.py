import subprocess
import sys
import os

def test_no_name(capsys):
    result = subprocess.run([sys.executable, os.path.join("src", "main.py")], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello! Use --name to provide your name." in result.stdout

def test_with_name(capsys):
    result = subprocess.run([sys.executable, os.path.join("src", "main.py"), "--name", "Alice"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, Alice!" in result.stdout
