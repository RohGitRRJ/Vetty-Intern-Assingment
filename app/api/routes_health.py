from fastapi import APIRouter

from app.config import get_settings

router = APIRouter(tags=["meta"])


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/version")
def version():
    settings = get_settings()
    return {"app_name": settings.app_name, "version": settings.version}
