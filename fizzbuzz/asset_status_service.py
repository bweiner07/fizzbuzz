from fizzbuzz.domain.tracker_events import TrackerEvent
from fizzbuzz.domain.data_service import TrackerData


class AssetStatusService:

    def __init__(self):
        self.data_service = TrackerData()
        self.on_violation = None

    def on_tracker_event(self, event: TrackerEvent):
        if event.event_type == 'Location Changed' and event.in_geofence == True:
            self.on_violation(event.asset_id)

        last_tracker_event = self.data_service.find(event.asset_id)
        if last_tracker_event is None:
            self.data_service.save(event)
        elif last_tracker_event.timestamp < event.timestamp:
            self.data_service.save(event)

    def is_engine_running(self, asset_id: int):
        tracker_event = self.data_service.find(asset_id).event_type
        return tracker_event == 'Ignition On'

    def subscribe_to_geofence_violations(self, on_violation):
        self.on_violation = on_violation
