from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/3090?v=4'
    resp_mock.json.return_value = {
        'login': 'marcus', 'id': 3090, 'node_id': 'MDQ6VXNlcjMwOTA=',
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('marcus')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('marvinsilva')
    assert 'https://avatars1.githubusercontent.com/u/45732834?v=4' == url
