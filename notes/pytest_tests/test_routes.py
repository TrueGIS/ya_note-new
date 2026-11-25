from http import HTTPStatus

import pytest
from django.urls import reverse

from constants import NOTE_SLUG


@pytest.mark.parametrize(
    'name',
    ('notes:home', 'users:login', 'users:signup'),
)
def test_public_pages_are_available(client, name):
    url = reverse(name)

    response = client.get(url)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'name',
    ('notes:add', 'notes:list', 'notes:success'),
)
def test_private_pages_are_available_to_author(author_client, name):
    url = reverse(name)

    response = author_client.get(url)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'name',
    ('notes:detail', 'notes:edit', 'notes:delete'),
)
def test_note_pages_are_available_to_author(note, author_client, name):
    url = reverse(name, args=(NOTE_SLUG,))

    response = author_client.get(url)

    assert response.status_code == HTTPStatus.OK
