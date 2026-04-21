from unittest.mock import patch, MagicMock
from main import main

# (Important) The order of the patches is important - they are applied from the bottom up, so the last patch in the list is applied first. This means that the mock for GAMES will be applied before the others, ensuring that the main function uses the mocked GAMES data during the test.
@patch("main.save_history")
@patch("main.send_telegram_msg")
@patch("main.load_history")
@patch("main.get_steam_data")
@patch("main.GAMES", {
    "570": {
        "name": "Dota 2",
        "type": "app",
        "target_price": 50.0,
        "target_discount": 30
    }
})

# Test that an alert is sent when the price is at or below the target
def test_sends_alert_when_price_is_reached(mock_get_steam, mock_load_history, mock_send, mock_save):
    mock_load_history.return_value = {}
    mock_get_steam.return_value = [{
        "id": "570",
        "name": "Dota 2",
        "type": "app",
        "current_price": 40.0,  # low of target_price
        "discount": 20
    }]

    main()

    mock_send.assert_called_once()  # should send alert
    mock_save.assert_called_once()  # should save to history

# (Important) Order of patches is important - they are applied from the bottom up
@patch("main.save_history")
@patch("main.send_telegram_msg")
@patch("main.load_history")
@patch("main.get_steam_data")
@patch("main.GAMES", {
    "570": {"name": "Dota 2", "type": "app", "target_price": 50.0, "target_discount": 30}
})

# Test that no alert is sent if the price is above the target
def test_no_alert_when_already_in_history(mock_get_steam, mock_load_history, mock_send, mock_save):
    mock_get_steam.return_value = [{
        "id": "570", "name": "Dota 2", "type": "app",
        "current_price": 40.0, "discount": 20
    }]
    mock_load_history.return_value = {"570_40.0": True}  # already alerted for this price
    main()

    mock_send.assert_not_called()  # should not send alert again