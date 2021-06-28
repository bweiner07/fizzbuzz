import unittest
from collections import defaultdict
from datetime import datetime, timedelta

from fizzbuzz.asset_status_service import AssetStatusService
from fizzbuzz.domain.tracker_events import IgnitionOn, LocationChanged

event_start_time = datetime(2014, 5, 5)

# Asset IDs
skid_loader = 1

inside_fence = True
outside_fence = False


class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.alerts_count = defaultdict(int)
        self.service = AssetStatusService()

        self.events = [
            IgnitionOn(event_start_time, skid_loader),
            LocationChanged(event_start_time + timedelta(minutes=1), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=2), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=3), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=4), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=5), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=6), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=7), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=8), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=9), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=10), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=11), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=12), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=13), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=14), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=15), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=16), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=17), skid_loader, outside_fence),
            LocationChanged(event_start_time + timedelta(minutes=18), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=19), skid_loader, inside_fence),
            LocationChanged(event_start_time + timedelta(minutes=20), skid_loader, inside_fence),
        ]

    def test_geofence_alerts_are_sent(self):

        self.service.subscribe_to_geofence_violations(self.on_violation)

        for event in self.events:
            self.service.on_tracker_event(event)

        number_of_alerts = 10  # CHANGE THIS: You define what drives a geofence alert
        self.assertEqual(number_of_alerts, self.alerts_count[skid_loader])

    def on_violation(self, asset_id):
        self.alerts_count[asset_id] += 1


if __name__ == '__main__':
    unittest.main()
