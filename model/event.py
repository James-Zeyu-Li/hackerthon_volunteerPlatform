from enum import Enum


class EventType(Enum):
    FLOOD_WARNING = "Flood Warning"
    EARTHQUAKE = "Earthquake"
    FIRE_WARNING = "Fire Warning"
    FLOOD = "Flood"
    EARTHQUAKE_WARNING = "Earthquake Warning"
    FIRE = "Fire"


class Severity(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class CurrentEvent:
    def __init__(self, event_type, severity, affection_rate,
                 road_closure_status):
        self.event_type = event_type
        self.severity = severity
        self.affection_rate = affection_rate
        self.road_closure_status = road_closure_status
