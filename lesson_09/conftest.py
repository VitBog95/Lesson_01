import pytest
from db import get_session


@pytest.fixture
def session():
    """Создаёт сессию БД и закрывает её после теста."""
    s = get_session()
    yield s
    s.close()
