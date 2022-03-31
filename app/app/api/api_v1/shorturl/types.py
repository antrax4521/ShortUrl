from decimal import Decimal
from typing import Dict, List, Optional
from typing_extensions import TypedDict
from pydantic import BaseModel, HttpUrl



class URLOriginal(BaseModel):
    url: HttpUrl


class URLShort(BaseModel):
    url_encoded: HttpUrl
