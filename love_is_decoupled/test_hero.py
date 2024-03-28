from .hero import Hero
from .wellness import Wellness
from .partner import Partner


"""
Geezum creepers, I am finding it really hard to validate the expected behaviors
of our Hero.

The tests are taking forever to run. Its slowing down my feedback,
and its making it a real pain to continue to develop the Hero.

There are a couple of cases that I'd like to test, but its just so painful.

Right now there is a lot of beahvior that I'd like to test in the three public
methods (get_wellness, get_life_plan, should_find_new_partner) of the Hero class.
But I am finding it really hard to do so.

I'd also like to clean-codeify Hero, but without tests in place, that would be
irresponsible.
"""


class MockPartnerGetWellness(Partner):
    def __init__(self, **kwargs):
        pass

    def __str__(self):
        return "I'm a get wellness mock."

    def communicate(self):
        return "Hey, what's up? I'm fast!"


class MockPartnerGetLifePlan(Partner):
    def __init__(self, **kwargs):
        self.priorities = ["lame", "stuff"]

    def __str__(self):
        return "I'm a get life plan mock."


class MockPartnerShouldFindNewPartner(Partner):
    def __init__(self, **kwargs):
        self.priorities = ["curling", "day trading", "hero"]

    def __str__(self):
        return "I should probably find a new partner but I guess I'm stuck."


def test_hero_get_wellness():
    """
    Given:
        - a Hero instance
        - a mocked Partner instance that has a fast communicate method

    When:
        - the get_wellness method is called

    Then:
        - the method should return Wellness.FAIR
    """
    # Given
    mock_partner = MockPartnerGetWellness()
    hero = Hero(name="Pat", interests=["doesn't matter"], partner=mock_partner)

    # When
    wellness = hero.get_wellness()

    # Then
    assert wellness == Wellness.JUST_FINE


def test_hero_get_life_plan():
    """
    Given:
        - a Hero instance
        - a Partner that has no overlapping interests with the Hero

    When:
        - the get_life_plan method is called

    Then:
        - the method should return a dictionary with the interests as keys and the value as 1
    """
    # Given
    mock_partner = MockPartnerGetLifePlan()
    hero = Hero(name="Vic", interests=["entrepreneurship", "helping others"], partner=mock_partner)

    # When
    life_plan = hero.get_life_plan()

    # Then
    assert life_plan == {"entrepreneurship": 1, "helping others": 1}


def test_hero_should_find_new_partner():
    """
    Given:
        - a Hero instance
        - a Partner with HERO in its list of priorities

    When:
        - the should_find_new_partner method is called

    Then:
        - the method should return False
    """
    # Given
    mock_partner = MockPartnerShouldFindNewPartner()
    hero = Hero(name="Tracy", interests=["vaping", "Jean-Claude Van Damme"], partner=mock_partner)

    # When
    should_find_new_partner = hero.should_find_new_partner()

    # Then
    assert should_find_new_partner is False
