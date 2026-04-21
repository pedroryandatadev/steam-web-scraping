from unittest.mock import patch
from app.telegram_bot import send_telegram_msg

# Test that send_telegram_msg calls the correct Telegram API endpoint
@patch("app.telegram_bot.requests.post")
def test_send_telegram_msg_calls_correct_endpoint(mock_post):
    send_telegram_msg("Offer found!")
    mock_post.assert_called_once()
    url_called = mock_post.call_args[0][0]
    assert "api.telegram.org" in url_called

# Test that send_telegram_msg does not raise an exception even if the request fails
@patch("app.telegram_bot.requests.post")
def test_send_telegram_msg_handles_error_gracefully(mock_post):
    mock_post.side_effect = Exception("Timeout")
    send_telegram_msg("Message")  # should not raise an exception even if the request fails