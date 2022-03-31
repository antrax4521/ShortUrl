from urllib import request
import shortuuid
from starlette.requests import Request
from starlette.responses import RedirectResponse

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.api import deps
from fastapi import HTTPException
from app.api.api_v1.shorturl.types import URLOriginal, URLShort
from app.core.config import settings
from app.api.api_v1.shorturl.crud import save_original_url, get_original_url
from app.api.api_v1.shorturl.tasks import perform_shortener_log


app = APIRouter()


@app.post('/shorten/')
async def encode_url(
    *,
    db: Session = Depends(deps.get_db),
    request: Request,
    url: URLOriginal
):  
    obj = save_original_url(db, url.url)

    if not obj:
        raise HTTPException(status_code=422)
    
    return URLShort(url_encoded=f"{request.url}{obj.short_uuid}")


@app.get('/shorten/{short_key}/', response_model=URLOriginal)
async def decode_url(
    *,
    db: Session = Depends(deps.get_db),
    short_key: str,
    background_tasks: BackgroundTasks
):  
    obj = get_original_url(db, short_key)

    if not obj:
        raise HTTPException(status_code=404)

    background_tasks.add_task(perform_shortener_log, db , obj.id)

    if settings.REDIRECT_ORIGINAL_URL:
        return RedirectResponse(url=obj.original_url)

    return URLOriginal(url=obj.original_url)
