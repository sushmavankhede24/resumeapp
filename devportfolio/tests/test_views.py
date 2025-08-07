import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_homepage_view_without_data(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert b"John Doe" not in response.content
