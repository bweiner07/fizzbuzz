import unittest
from datetime import datetime, timedelta

from fizzbuzz.asset_status_service import AssetStatusService
from fizzbuzz.domain.tracker_events import IgnitionOff, IgnitionOn

event_start_time = datetime(2014, 5, 5)

# Asset IDs
skid_loader = 1
boom_lift = 2


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.service = AssetStatusService()

        self.events = [
            IgnitionOn(event_start_time, skid_loader),
            IgnitionOn(event_start_time, boom_lift),
            IgnitionOn(event_start_time + timedelta(days=3), boom_lift), # Note `days` here
            IgnitionOff(event_start_time + timedelta(hours=3), boom_lift),
            IgnitionOff(event_start_time + timedelta(days=2, hours=3), skid_loader),
            IgnitionOn(event_start_time + timedelta(days=2), skid_loader),
        ]

    def test_engine_status_is_stored_correctly_when_events_are_out_of_order(self):
        for event in self.events:
            self.service.on_tracker_event(event)

        self.assertTrue(self.service.is_engine_running(boom_lift))
        self.assertFalse(self.service.is_engine_running(skid_loader))


if __name__ == '__main__':
    unittest.main()
