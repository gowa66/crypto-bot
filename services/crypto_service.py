# services/crypto_service.py

import requests
from datetime import datetime

BASE_URL = "https://api.coingecko.com/api/v3"

class CryptoService:
    def get_coin_id(self, symbol: str) -> str:
        symbol_map = {
            'BTC': 'bitcoin',
            'ETH': 'ethereum',
            'ADA': 'cardano',
            'SOL': 'solana',
            'XRP': 'ripple'
        }
        symbol_upper = symbol.upper()
        if symbol_upper in symbol_map:
            return symbol_map[symbol_upper]

        response = requests.get(f"{BASE_URL}/coins/list")
        for coin in response.json():
            if coin['symbol'].lower() == symbol.lower():
                return coin['id']
        return None

    def get_current_price(self, symbol: str) -> dict:
        coin_id = self.get_coin_id(symbol)
        if not coin_id:
            return {"error": "Invalid symbol"}

        response = requests.get(f"{BASE_URL}/simple/price", params={
            "ids": coin_id,
            "vs_currencies": "usd",
            "include_24hr_change": "true"
        })
        data = response.json().get(coin_id, {})

        return {
            "symbol": symbol.upper(),
            "price": data.get("usd"),
            "change": data.get("usd_24h_change")
        }

    def get_historical_data(self, symbol: str, days: int = 30) -> dict:
        coin_id = self.get_coin_id(symbol)
        if not coin_id:
            return {"error": "Invalid symbol"}

        response = requests.get(f"{BASE_URL}/coins/{coin_id}/market_chart", params={
            "vs_currency": "usd",
            "days": days
        })
        prices = response.json().get("prices", [])

        history = {}
        for timestamp, price in prices:
            date_str = datetime.utcfromtimestamp(timestamp / 1000).strftime("%Y-%m-%d")
            history[date_str] = price

        return history
