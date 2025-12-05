from typing import Optional
from pydantic import BaseModel


class Coin(BaseModel):
    id: str
    symbol: str
    name: str
    current_price_inr: Optional[float] = None
    current_price_cad: Optional[float] = None
    market_cap_inr: Optional[float] = None
    market_cap_cad: Optional[float] = None
    image: Optional[str] = None


class CoinListResponse(BaseModel):
    page_num: int
    per_page: int
    total_items: Optional[int] = None
    items: list[Coin]
