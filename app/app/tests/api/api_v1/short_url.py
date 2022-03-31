from gc import get_referents
from typing import Dict
from wsgiref import headers

from fastapi.testclient import TestClient
from app.core.config import settings
#from app.api.api_v1.shorturl.utils import short_uuid_generator



def test_failed_short_url(client: TestClient) -> None:
    """
    This test is success when recieve an 422 error
    """
    login_data = {
        "url": "Basic String"
    }

    r = client.post(f"{settings.SERVER_HOST}{settings.API_V1_STR}/shorten/", json=login_data)
    
    response = r.json()
    assert r.status_code == 422
    assert response['detail'][0]['msg'] == 'invalid or missing URL scheme'


def test_success_short_url(client: TestClient) -> None:
    """
    This test is success when perform an url 
    and return the shortuuid

    Then makes a get request to validate that is ok
    """
    settings.REDIRECT_ORIGINAL_URL = False

    login_datas = {
        "url": "https://google.com.mx"
    }

    post_r = client.post(f"{settings.SERVER_HOST}{settings.API_V1_STR}/shorten/", json=login_datas)
    print(post_r)
    post_response = post_r.json()
    assert post_r.status_code == 200
    short_url = post_response['url_encoded']

    get_r = client.get(f"{short_url}")
    
    get_response = get_r.json()
    assert get_r.status_code == 200
    assert get_response['url'] == login_datas['url']
