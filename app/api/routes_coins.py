from typing import Optional, List

from fastapi import APIRouter, Depends, Query

from app.dependencies import get_current_user
from app.schemas.coin import CoinListResponse
from app.services.coingecko_client import CoinGeckoClient

router = APIRouter(prefix="/coins", tags=["coins"])
client = CoinGeckoClient()


@router.get("", response_model=CoinListResponse)
def list_coins(
    page_num: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=250),
    _: str = Depends(get_current_user),
):
    items = client.list_coins(page_num=page_num, per_page=per_page)
    return CoinListResponse(
        page_num=page_num,
        per_page=per_page,
        total_items=None,
        items=items,
    )


@router.get("/filtered", response_model=CoinListResponse)
def list_coins_filtered(
    coin_ids: Optional[List[str]] = Query(None, description="Repeatable ?coin_ids=btc&coin_ids=eth"),
    category: Optional[str] = Query(None),
    page_num: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=250),
    _: str = Depends(get_current_user),
):
    items = client.list_coins_by_filter(
        coin_ids=coin_ids,
        category=category,
        page_num=page_num,
        per_page=per_page,
    )
    return CoinListResponse(
        page_num=page_num,
        per_page=per_page,
        total_items=None,
        items=items,
    )
