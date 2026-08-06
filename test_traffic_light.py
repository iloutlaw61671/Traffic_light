import pytest
from traffic_light import TrafficLight, InvalidStateError


def test_initial_state_defaults_to_red():
    '''Verify default initial state'''
    light = TrafficLight()
    assert light.state == "RED"


def test_rejects_invalid_initial_state():
    '''Verify invalid initial state'''
    with pytest.raises(InvalidStateError):
        TrafficLight(initial_state="PURPLE")


def test_red_transitions_to_green():
    '''Transition fromm red to green'''
    light = TrafficLight()
    assert light.next() == "GREEN"


def test_green_transitions_to_yellow():
    '''Transition fromm green to yellow'''
    light = TrafficLight(initial_state="GREEN")
    assert light.next() == "YELLOW"


def test_yellow_transitions_back_to_red():
    '''Transition from yellow to red'''
    light = TrafficLight(initial_state="YELLOW")
    assert light.next() == "RED"


def test_full_cycle_returns_to_red():
    '''Doing the full cycle'''
    light = TrafficLight()
    for _ in range(3):
        light.next()
    assert light.state == "RED"
    assert light.cycle_count == 1

def test_pedestrians_can_cross_only_when_red():
    '''Verify pedestrian method works'''
    light = TrafficLight()
    assert light.pedestrians_can_cross() is True
    light.next()
    assert light.pedestrians_can_cross() is False
