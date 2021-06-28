
## Problem 1

ES manages thousands of assets, each with a small tracking device on it. These tracking devices
trigger events when things like the ignition is turned on.

For this first use case, we want to build some service that, given it consumes this inbound stream
of events, can answer the question:

    Given an asset id, is it currently running?


## Problem 2

Except, it turns out, most of the trackers are not entirely reliable - for instance, they may be
retrofitted on equipment with no good way to tell ignition events. In these cases, trackers rely on
secondary signals, like sudden drops in battery voltage, to infer ignition events. This makes the
stream of events unreliable - for instance, sometimes it sends duplicates.

Problem 2, then is:

    Given the stream sometimes contains several consecutive "IgnitionOn" events, sensibly satisfy Problem 1.


## Problem 3

We don't only track ignition events; another common event is LocationChanged, issued intermittently when
an asset changes GPS location. A key use case for this is signaling when equipment enters certain areas,
like when it shows up at a worksite. We call these areas geofences, and this repo provides a mock service
to tell if a coordinate is within a geofence or not.

Just as with the ignition events, GPS events in the real world are.. terribly inaccurate. Location events
will be triggered with coordinates that are within some surprisingly large error margin from their actual
location, meaning sometimes they end up with coordinates outside geofences, even if the actual asset in the
real world is well within bounds.

We now want to extend our system to be able to handle Problem 1 as well as answer the question:

    Given that the trackers are surprisingly inaccurate, make the system resilient to invalid notifications,
    meaning, avoid incorrectly triggering geofence alerts if an asset is not, in the real world, violating
    the geofence.
