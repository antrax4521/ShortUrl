from sqlalchemy.orm import Session

from app.api.api_v1.shorturl.crud import save_original_url, save_shortener_log, get_original_url


def test_create_original_url(db: Session) -> None:
    
    ## Query to perfom a new row
    url = "https://example.com"
    url_object = save_original_url(db, url)
    
    assert url_object.original_url == url

    ##Query to get the last inserted id
    get_url = get_original_url(db, url_object.short_uuid)

    assert get_url.short_uuid == url_object.short_uuid
