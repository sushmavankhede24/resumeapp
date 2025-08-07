# your_app/tests/test_models.py

import pytest
from homeapp.models import Profile, Skill, Project


@pytest.mark.django_db
def test_profile_str():
    profile = Profile.objects.create(
        name="John Doe", bio="Developer", email="john@example.com"
    )
    assert str(profile) == "John Doe"


@pytest.mark.django_db
def test_skill_str():
    profile = Profile.objects.create(
        name="Jane Smith", bio="Designer", email="jane@example.com"
    )
    skill = Skill.objects.create(profile=profile, skill_name="Photoshop", proficiency=80)
    assert str(skill) == "Photoshop (80%)"


@pytest.mark.django_db
def test_project_str():
    profile = Profile.objects.create(
        name="Alice Johnson", bio="Full-stack Dev", email="alice@example.com"
    )
    project = Project.objects.create(
        profile=profile,
        title="Portfolio Website",
        description="Built with Django and React",
    )
    assert str(project) == "Portfolio Website"
