

VALID_STATES = ("RED", "GREEN", "YELLOW")

_TRANSITIONS = {
    "RED": "GREEN",
    "GREEN": "YELLOW",
    "YELLOW": "RED",
}


class InvalidStateError(ValueError):
    """Raised when the light is asked to start in an unknown state."""


class TrafficLight:
    """A minimal traffic light controller.

    RED -> GREEN -> YELLOW -> RED -> ...
    Pedestrians may only cross while the light is RED.
    """

    def __init__(self, initial_state: str = "RED"):
        if initial_state not in VALID_STATES:
            raise InvalidStateError(f"Unknown state: {initial_state!r}")
        self._state = initial_state
        self._cycle_count = 0

    @property
    def state(self) -> str:
        """Current light color."""
        return self._state

    @property
    def cycle_count(self) -> int:
        """Number of full RED->GREEN->YELLOW->RED cycles completed."""
        return self._cycle_count

    def next(self) -> str:
        """Advance to the next state and return it."""
        previous = self._state
        self._state = _TRANSITIONS[self._state]
        if previous == "YELLOW" and self._state == "RED":
            self._cycle_count += 1
        return self._state

    def pedestrians_can_cross(self) -> bool:
        """True only while the light is RED."""
        return self._state == "RED"
