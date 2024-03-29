# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='comm.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\ncomm.proto\x1a\x0cnanopb.proto\"\xcd\x01\n\x11RailConfiguration\x12\x11\n\tpowerRail\x18\x01 \x02(\x05\x12\x14\n\x0c\x63urrentLimit\x18\x02 \x01(\x02\x12\x15\n\rvoltageCutoff\x18\x03 \x01(\x02\x12\x1b\n\x13\x63urrentLimitEnabled\x18\x04 \x01(\x08\x12\x1b\n\x13voltageLimitEnabled\x18\x05 \x01(\x08\x12\x11\n\ttimeLimit\x18\x06 \x01(\x03\x12\x18\n\x10timeLimitEnabled\x18\x07 \x01(\x08\x12\x11\n\tdutyCycle\x18\x08 \x01(\x02\"C\n\x12PowerConfiguration\x12-\n\x11railConfiguration\x18\x01 \x03(\x0b\x32\x12.RailConfiguration\"B\n\x0cPowerControl\x12\x11\n\tpowerRail\x18\x01 \x01(\x05\x12\x1f\n\npowerState\x18\x02 \x01(\x0e\x32\x0b.PowerState\"e\n\rPowerRailInfo\x12\x11\n\tpowerRail\x18\x01 \x01(\x05\x12\x0f\n\x07voltage\x18\x02 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x02\x12\x1f\n\npowerState\x18\x04 \x01(\x0e\x32\x0b.PowerState\"\xb1\x01\n\nPowerEvent\x12\x11\n\tpowerRail\x18\x01 \x01(\x05\x12(\n\teventType\x18\x02 \x01(\x0e\x32\x15.PowerEvent.EventType\"f\n\tEventType\x12\n\n\x06NORMAL\x10\x00\x12\x13\n\x0f\x43URRENT_LIMITED\x10\x01\x12\x13\n\x0fVOLTAGE_LIMITED\x10\x02\x12\x11\n\rPOWER_LIMITED\x10\x03\x12\x10\n\x0cTIME_LIMITED\x10\x04\"k\n\x07TxMicro\x12\x11\n\ttimeStamp\x18\x01 \x01(\x03\x12,\n\rpowerRailInfo\x18\x02 \x03(\x0b\x32\x0e.PowerRailInfoB\x05\x92?\x02\x10\n\x12\x1f\n\npowerEvent\x18\x03 \x01(\x0b\x32\x0b.PowerEvent\"_\n\x07RxMicro\x12/\n\x12powerConfiguration\x18\x01 \x01(\x0b\x32\x13.PowerConfiguration\x12#\n\x0cpowerControl\x18\x02 \x01(\x0b\x32\r.PowerControl*(\n\nPowerState\x12\x07\n\x03OFF\x10\x00\x12\x06\n\x02ON\x10\x01\x12\t\n\x05\x45RROR\x10\x03')
  ,
  dependencies=[nanopb__pb2.DESCRIPTOR,])

_POWERSTATE = _descriptor.EnumDescriptor(
  name='PowerState',
  full_name='PowerState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=862,
  serialized_end=902,
)
_sym_db.RegisterEnumDescriptor(_POWERSTATE)

PowerState = enum_type_wrapper.EnumTypeWrapper(_POWERSTATE)
OFF = 0
ON = 1
ERROR = 3


_POWEREVENT_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='PowerEvent.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURRENT_LIMITED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLTAGE_LIMITED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWER_LIMITED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME_LIMITED', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=552,
  serialized_end=654,
)
_sym_db.RegisterEnumDescriptor(_POWEREVENT_EVENTTYPE)


_RAILCONFIGURATION = _descriptor.Descriptor(
  name='RailConfiguration',
  full_name='RailConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='powerRail', full_name='RailConfiguration.powerRail', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentLimit', full_name='RailConfiguration.currentLimit', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voltageCutoff', full_name='RailConfiguration.voltageCutoff', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentLimitEnabled', full_name='RailConfiguration.currentLimitEnabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voltageLimitEnabled', full_name='RailConfiguration.voltageLimitEnabled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeLimit', full_name='RailConfiguration.timeLimit', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeLimitEnabled', full_name='RailConfiguration.timeLimitEnabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dutyCycle', full_name='RailConfiguration.dutyCycle', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=234,
)


_POWERCONFIGURATION = _descriptor.Descriptor(
  name='PowerConfiguration',
  full_name='PowerConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='railConfiguration', full_name='PowerConfiguration.railConfiguration', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=303,
)


_POWERCONTROL = _descriptor.Descriptor(
  name='PowerControl',
  full_name='PowerControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='powerRail', full_name='PowerControl.powerRail', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='powerState', full_name='PowerControl.powerState', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=371,
)


_POWERRAILINFO = _descriptor.Descriptor(
  name='PowerRailInfo',
  full_name='PowerRailInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='powerRail', full_name='PowerRailInfo.powerRail', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voltage', full_name='PowerRailInfo.voltage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current', full_name='PowerRailInfo.current', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='powerState', full_name='PowerRailInfo.powerState', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=474,
)


_POWEREVENT = _descriptor.Descriptor(
  name='PowerEvent',
  full_name='PowerEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='powerRail', full_name='PowerEvent.powerRail', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventType', full_name='PowerEvent.eventType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POWEREVENT_EVENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=654,
)


_TXMICRO = _descriptor.Descriptor(
  name='TxMicro',
  full_name='TxMicro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='TxMicro.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='powerRailInfo', full_name='TxMicro.powerRailInfo', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\002\020\n'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='powerEvent', full_name='TxMicro.powerEvent', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=656,
  serialized_end=763,
)


_RXMICRO = _descriptor.Descriptor(
  name='RxMicro',
  full_name='RxMicro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='powerConfiguration', full_name='RxMicro.powerConfiguration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='powerControl', full_name='RxMicro.powerControl', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=860,
)

_POWERCONFIGURATION.fields_by_name['railConfiguration'].message_type = _RAILCONFIGURATION
_POWERCONTROL.fields_by_name['powerState'].enum_type = _POWERSTATE
_POWERRAILINFO.fields_by_name['powerState'].enum_type = _POWERSTATE
_POWEREVENT.fields_by_name['eventType'].enum_type = _POWEREVENT_EVENTTYPE
_POWEREVENT_EVENTTYPE.containing_type = _POWEREVENT
_TXMICRO.fields_by_name['powerRailInfo'].message_type = _POWERRAILINFO
_TXMICRO.fields_by_name['powerEvent'].message_type = _POWEREVENT
_RXMICRO.fields_by_name['powerConfiguration'].message_type = _POWERCONFIGURATION
_RXMICRO.fields_by_name['powerControl'].message_type = _POWERCONTROL
DESCRIPTOR.message_types_by_name['RailConfiguration'] = _RAILCONFIGURATION
DESCRIPTOR.message_types_by_name['PowerConfiguration'] = _POWERCONFIGURATION
DESCRIPTOR.message_types_by_name['PowerControl'] = _POWERCONTROL
DESCRIPTOR.message_types_by_name['PowerRailInfo'] = _POWERRAILINFO
DESCRIPTOR.message_types_by_name['PowerEvent'] = _POWEREVENT
DESCRIPTOR.message_types_by_name['TxMicro'] = _TXMICRO
DESCRIPTOR.message_types_by_name['RxMicro'] = _RXMICRO
DESCRIPTOR.enum_types_by_name['PowerState'] = _POWERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RailConfiguration = _reflection.GeneratedProtocolMessageType('RailConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _RAILCONFIGURATION,
  __module__ = 'comm_pb2'
  # @@protoc_insertion_point(class_scope:RailConfiguration)
  ))
_sym_db.RegisterMessage(RailConfiguration)

PowerConfiguration = _reflection.GeneratedProtocolMessageType('PowerConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _POWERCONFIGURATION,
  __module__ = 'comm_pb2'
  # @@protoc_insertion_point(class_scope:PowerConfiguration)
  ))
_sym_db.RegisterMessage(PowerConfiguration)

PowerControl = _reflection.GeneratedProtocolMessageType('PowerControl', (_message.Message,), dict(
  DESCRIPTOR = _POWERCONTROL,
  __module__ = 'comm_pb2'
  # @@protoc_insertion_point(class_scope:PowerControl)
  ))
_sym_db.RegisterMessage(PowerControl)

PowerRailInfo = _reflection.GeneratedProtocolMessageType('PowerRailInfo', (_message.Message,), dict(
  DESCRIPTOR = _POWERRAILINFO,
  __module__ = 'comm_pb2'
  # @@protoc_insertion_point(class_scope:PowerRailInfo)
  ))
_sym_db.RegisterMessage(PowerRailInfo)

PowerEvent = _reflection.GeneratedProtocolMessageType('PowerEvent', (_message.Message,), dict(
  DESCRIPTOR = _POWEREVENT,
  __module__ = 'comm_pb2'
  # @@protoc_insertion_point(class_scope:PowerEvent)
  ))
_sym_db.RegisterMessage(PowerEvent)

TxMicro = _reflection.GeneratedProtocolMessageType('TxMicro', (_message.Message,), dict(
  DESCRIPTOR = _TXMICRO,
  __module__ = 'comm_pb2'
  # @@protoc_insertion_point(class_scope:TxMicro)
  ))
_sym_db.RegisterMessage(TxMicro)

RxMicro = _reflection.GeneratedProtocolMessageType('RxMicro', (_message.Message,), dict(
  DESCRIPTOR = _RXMICRO,
  __module__ = 'comm_pb2'
  # @@protoc_insertion_point(class_scope:RxMicro)
  ))
_sym_db.RegisterMessage(RxMicro)


_TXMICRO.fields_by_name['powerRailInfo']._options = None
# @@protoc_insertion_point(module_scope)
