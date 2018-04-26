import pytest

@pytest.fixture
def app():
    return {
      "id": "e43a024d-9e16-41ea-8d16-b8b0e8d88464",
      "name": "App",
      "description": "Access your account programmatically.",
      "website": "https://test.com/",
      "slug": "test",
      "createdAt": "2016-06-30 02:08:06",
      "updatedAt": "2018-04-21 13:13:09",
      "isPublic": True,
      "iconUrl": "/assets/media/test.png"
    }
