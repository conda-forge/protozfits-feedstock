from protozfits.CoreMessages_pb2 import AnyArray
from protozfits.R1v1_pb2 import Event

event = Event(waveform=AnyArray(type=AnyArray.U16, data=2 * b'\x00'))
