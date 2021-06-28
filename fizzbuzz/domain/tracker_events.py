

class TrackerEvent:
    """
    Emitted from physical trackers attached to assets in the field. See subclasses for
    specific events that can occur.
    """
    def __init__(self, event_type, timestamp, asset_id):
        self.event_type = event_type
        self.timestamp = timestamp
        self.asset_id = asset_id


class IgnitionOn(TrackerEvent):
    IGNITION_ON = 'Ignition On'

    def __init__(self, timestamp, asset_id):
        super().__init__(self.IGNITION_ON, timestamp, asset_id)


class IgnitionOff(TrackerEvent):
    IGNITION_OFF = 'Ignition Off'

    def __init__(self, timestamp, asset_id):
        super().__init__(self.IGNITION_OFF, timestamp, asset_id)


class LocationChanged(TrackerEvent):
    LOCATION_CHANGED = 'Location Changed'

    def __init__(self, timestamp, asset_id, in_geofence):
        super().__init__(self.LOCATION_CHANGED, timestamp, asset_id)
        self.in_geofence = in_geofence
