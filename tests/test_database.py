import json
import pytest
from unittest.mock import mock_open, patch
from app.database import load_history, save_history

# Test that load_history returns an empty dictionary if the file does not exist
def test_load_history_returns_empty_dict_when_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_history()
    assert result == {}

# Test that load_history correctly parses the JSON file
def test_load_history_parses_json_correctly():
    fake_data = json.dumps({"570_40.0": True})
    with patch("builtins.open", mock_open(read_data=fake_data)):
        result = load_history()
    assert result == {"570_40.0": True}

# Test that save_history writes the correct data to the file
def test_save_history_writes_json():
    m = mock_open()
    with patch("builtins.open", m):
        save_history({"570_40.0": True})
    m.assert_called_once()