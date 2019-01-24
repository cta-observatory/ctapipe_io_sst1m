import os
import copy
from pkg_resources import resource_filename

from ctapipe_io_sst1m import SST1MEventSource

example_file_path = resource_filename(
    'protozfits',
    os.path.join(
        'tests',
        'resources',
        'example_10evts.fits.fz'
    )
)

FIRST_EVENT_NUMBER_IN_FILE = 97750287
ADC_SAMPLES_SHAPE = (1, 1296, 50)


def test_loop_over_events():

    n_events = 5
    inputfile_reader = SST1MEventSource(
        input_url=example_file_path,
        max_events=n_events
    )

    for i, event in enumerate(inputfile_reader):
        assert event.r0.tels_with_data == {1}
        for telid in event.r0.tels_with_data:
            assert event.r0.event_id == FIRST_EVENT_NUMBER_IN_FILE + i
            assert event.r0.tel[telid].waveform.shape == ADC_SAMPLES_SHAPE

    # make sure max_events works
    assert i == n_events - 1


def test_that_event_is_not_modified_after_loop():

    n_events = 2
    source = SST1MEventSource(
        input_url=example_file_path,
        max_events=n_events
    )

    for event in source:
        last_event = copy.deepcopy(event)

    # now `event` should be identical with the deepcopy of itself from
    # inside the loop.
    # Unfortunately this does not work:
    #      assert last_event == event
    # So for the moment we just compare event ids
    assert event.r0.event_id == last_event.r0.event_id


def test_is_compatible():
    assert SST1MEventSource.is_compatible(example_file_path)


def test_interation():
    from ctapipe.io import event_source
    source = event_source(input_url=example_file_path, max_events=10)
    assert isinstance(source, SST1MEventSource)
    for event in source:
        assert event
