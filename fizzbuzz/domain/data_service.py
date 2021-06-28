from .tracker_events import TrackerEvent


class TrackerData:
    def __init__(self):
        self.data = {}

    def save(self, event: TrackerEvent):
        self.data[event.asset_id] = event

    def find(self, asset_id: int) -> TrackerEvent:
        if asset_id in self.data:
            return self.data[asset_id]

        return None
