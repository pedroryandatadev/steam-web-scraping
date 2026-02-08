from app.config import GAMES
from app.steam_api import get_steam_data
from app.telegram_bot import send_telegram_msg
from app.database import load_history, save_history

def main():
    # Load the history of sent alerts to avoid duplicates
    history = load_history()
    
    # Iterate through each game in the wishlist
    for item_id, goals in GAMES.items():
        print(f"Checking {goals['name']}...")
        version_list = get_steam_data(item_id, goals['type'])
        deals_found = []
        
        for v in version_list:
            # Logic: Price or Discount meets the goal
            price_reached = v['current_price'] <= goals['target_price']
            discount_reached = v['discount'] >= goals['target_discount']
            
            # Unique key to avoid spamming the same price
            alert_id = f"{v['id']}_{v['current_price']}"

            # Only alert if either condition is met and we haven't alerted for this price before
            if (price_reached or discount_reached) and alert_id not in history:
                store_link = f"https://store.steampowered.com/{v['type']}/{v['id']}"
                block = (f"🎮 *{v['name']}*\n"
                         f"💰 Price: R$ {v['current_price']:.2f}\n"
                         f"📉 Discount: {v['discount']}%\n"
                         f"🔗 [View on Store]({store_link})")
                deals_found.append(block)
                history[alert_id] = True

        # If we found any deals for this game, send a Telegram message
        if deals_found:
            message_body = "\n\n---\n\n".join(deals_found)
            final_msg = f"🎯 *DEALS FOUND FOR: {goals['name'].upper()}*\n\n{message_body}"
            send_telegram_msg(final_msg)
            print(f"Success: Alerts sent for {goals['name']}")
    
    # Save the updated history to avoid duplicate alerts in the future
    save_history(history)

# Entry point of the script
if __name__ == "__main__":
    main()