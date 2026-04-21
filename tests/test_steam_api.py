from unittest.mock import patch, MagicMock
from app.steam_api import get_steam_data

# Test that get_steam_data returns the correct fields
@patch("app.steam_api.requests.get")
def test_get_steam_data_returns_correct_fields(mock_requests):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "570": {
            "success": True,
            "data": {
                "name": "Dota 2",
                "price_overview": {
                    "final": 4000,  # price in cents
                    "discount_percent": 20
                }
            }
        }
    }
    mock_requests.return_value = mock_response

    result = get_steam_data("570", "app")
    
    assert len(result) > 0
    assert result[0]["current_price"] == 40.0
    assert result[0]["discount"] == 20

# Test that get_steam_data returns an empty list if the API call fails
@patch("app.steam_api.requests.get")
def test_returns_empty_list_on_api_failure(mock_requests):
    mock_requests.side_effect = Exception("Connection error")

    result = get_steam_data("570", "app")

    assert result == []