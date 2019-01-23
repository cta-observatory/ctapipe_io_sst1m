from ctapipe.io.containers import DataContainer
from ctapipe.core import Container, Field, Map


__all__ = [
    'SST1MContainer',
    'SST1MCameraContainer',
    'SST1MDataContainer',
]


class SST1MCameraContainer(Container):
    pixel_flags = Field(None, 'numpy array containing pixel flags')
    digicam_baseline = Field(None, 'Baseline computed by DigiCam')
    local_camera_clock = Field(float, "camera timestamp")
    gps_time = Field(float, "gps timestamp")
    camera_event_type = Field(int, "camera event type")
    array_event_type = Field(int, "array event type")
    trigger_input_traces = Field(None, "trigger patch trace (n_patches)")
    trigger_output_patch7 = Field(
        None,
        "trigger 7 patch cluster trace (n_clusters)")
    trigger_output_patch19 = Field(
        None,
        "trigger 19 patch cluster trace (n_clusters)")


class SST1MContainer(Container):
    tels_with_data = Field([], "list of telescopes with data")
    tel = Field(
        Map(SST1MCameraContainer),
        "map of tel_id to SST1MCameraContainer")


class SST1MDataContainer(DataContainer):
    sst1m = Field(SST1MContainer(), "optional SST1M Specific Information")
