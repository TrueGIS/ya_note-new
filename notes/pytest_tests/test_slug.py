from pytils.translit import slugify


def test_slug_for_russian_title():
    assert slugify('Заметка') == 'zametka'


def test_slug_separates_words():
    assert slugify('Django Notes') == 'django-notes'


def test_new_title_slug():
    title = 'Новая заметка'
    expected_slug = 'novaya-zametka'
    actual_slug = slugify(title)
    assert actual_slug == expected_slug