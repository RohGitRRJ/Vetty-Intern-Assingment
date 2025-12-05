from typing import List, Optional

import requests

from app.config import get_settings
from app.schemas.coin import Coin
from app.schemas.category import Category

settings = get_settings()


class CoinGeckoClient:
    def __init__(self) -> None:
        self.base_url = settings.coingecko_base_url

    def _get(self, path: str, params: Optional[dict] = None) -> dict | list:
        url = f"{self.base_url}{path}"
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    # -------- Coins --------
    def list_coins(
        self, page_num: int = 1, per_page: int = 10
    ) -> List[Coin]:
        
        markets_inr = self._get(
            "/coins/markets",
            params={
                "vs_currency": "inr",
                "order": "market_cap_desc",
                "per_page": per_page,
                "page": page_num,
                "sparkline": "false",
            },
        )
        markets_cad = self._get(
            "/coins/markets",
            params={
                "vs_currency": "cad",
                "order": "market_cap_desc",
                "per_page": per_page,
                "page": page_num,
                "sparkline": "false",
            },
        )

        cad_map = {c["id"]: c for c in markets_cad}

        coins: list[Coin] = []
        for c in markets_inr:
            cad = cad_map.get(c["id"])
            coins.append(
                Coin(
                    id=c["id"],
                    symbol=c["symbol"],
                    name=c["name"],
                    image=c.get("image"),
                    current_price_inr=c.get("current_price"),
                    market_cap_inr=c.get("market_cap"),
                    current_price_cad=cad.get("current_price") if cad else None,
                    market_cap_cad=cad.get("market_cap") if cad else None,
                )
            )
        return coins

    def list_coins_by_filter(
        self,
        coin_ids: Optional[list[str]] = None,
        category: Optional[str] = None,
        page_num: int = 1,
        per_page: int = 10,
    ) -> List[Coin]:
        ids_param = ",".join(coin_ids) if coin_ids else None

        def fetch(vs_currency: str):
            return self._get(
                "/coins/markets",
                params={
                    "vs_currency": vs_currency,
                    "order": "market_cap_desc",
                    "per_page": per_page,
                    "page": page_num,
                    "sparkline": "false",
                    "ids": ids_param,
                    "category": category,
                },
            )

        markets_inr = fetch("inr")
        markets_cad = fetch("cad")
        cad_map = {c["id"]: c for c in markets_cad}

        coins: list[Coin] = []
        for c in markets_inr:
            cad = cad_map.get(c["id"])
            coins.append(
                Coin(
                    id=c["id"],
                    symbol=c["symbol"],
                    name=c["name"],
                    image=c.get("image"),
                    current_price_inr=c.get("current_price"),
                    market_cap_inr=c.get("market_cap"),
                    current_price_cad=cad.get("current_price") if cad else None,
                    market_cap_cad=cad.get("market_cap") if cad else None,
                )
            )
        return coins

    # -------- Categories --------
    def list_categories(self) -> List[Category]:
        data = self._get("/coins/categories")
        categories: list[Category] = []
        for item in data:
            categories.append(
                Category(
                    category_id=item.get("id"),
                    name=item.get("name"),
                )
            )
        return categories
