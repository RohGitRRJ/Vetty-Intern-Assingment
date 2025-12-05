from fastapi import APIRouter, Depends

from app.dependencies import get_current_user
from app.schemas.category import CategoryListResponse
from app.services.coingecko_client import CoinGeckoClient

router = APIRouter(prefix="/categories", tags=["categories"])
client = CoinGeckoClient()


@router.get("", response_model=CategoryListResponse)
def list_categories(_user: str = Depends(get_current_user)):
    items = client.list_categories()
    return CategoryListResponse(items=items)
