# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iterators.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='iterators.proto',
  package='iterators',
  syntax='proto3',
  serialized_pb=_b('\n\x0fiterators.proto\x12\titerators\"R\n\rTriplePattern\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x11\n\tpredicate\x18\x02 \x01(\t\x12\x0e\n\x06object\x18\x03 \x01(\t\x12\r\n\x05graph\x18\x04 \x01(\t\"e\n\x11SavedScanIterator\x12(\n\x06triple\x18\x01 \x01(\x0b\x32\x18.iterators.TriplePattern\x12\x11\n\tlast_read\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61rdinality\x18\x03 \x01(\x03\"\x95\x02\n\x17SavedProjectionIterator\x12\x0e\n\x06values\x18\x01 \x03(\t\x12\x33\n\x0bscan_source\x18\x02 \x01(\x0b\x32\x1c.iterators.SavedScanIteratorH\x00\x12\x38\n\x0bjoin_source\x18\x03 \x01(\x0b\x32!.iterators.SavedIndexJoinIteratorH\x00\x12\x38\n\x0cunion_source\x18\x04 \x01(\x0b\x32 .iterators.SavedBagUnionIteratorH\x00\x12\x37\n\rfilter_source\x18\x05 \x01(\x0b\x32\x1e.iterators.SavedFilterIteratorH\x00\x42\x08\n\x06source\"\xb2\x02\n\x16SavedIndexJoinIterator\x12\x33\n\x0bscan_source\x18\x01 \x01(\x0b\x32\x1c.iterators.SavedScanIteratorH\x00\x12\x38\n\x0bjoin_source\x18\x02 \x01(\x0b\x32!.iterators.SavedIndexJoinIteratorH\x00\x12\'\n\x05inner\x18\x03 \x01(\x0b\x32\x18.iterators.TriplePattern\x12\x37\n\x03muc\x18\x04 \x03(\x0b\x32*.iterators.SavedIndexJoinIterator.MucEntry\x12\x11\n\tlast_read\x18\x05 \x01(\t\x1a*\n\x08MucEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x08\n\x06source\"\xec\x03\n\x15SavedBagUnionIterator\x12\x37\n\tproj_left\x18\x01 \x01(\x0b\x32\".iterators.SavedProjectionIteratorH\x00\x12\x36\n\nunion_left\x18\x02 \x01(\x0b\x32 .iterators.SavedBagUnionIteratorH\x00\x12\x36\n\tjoin_left\x18\x03 \x01(\x0b\x32!.iterators.SavedIndexJoinIteratorH\x00\x12\x35\n\x0b\x66ilter_left\x18\x04 \x01(\x0b\x32\x1e.iterators.SavedFilterIteratorH\x00\x12\x38\n\nproj_right\x18\x05 \x01(\x0b\x32\".iterators.SavedProjectionIteratorH\x01\x12\x37\n\x0bunion_right\x18\x06 \x01(\x0b\x32 .iterators.SavedBagUnionIteratorH\x01\x12\x37\n\njoin_right\x18\x07 \x01(\x0b\x32!.iterators.SavedIndexJoinIteratorH\x01\x12\x36\n\x0c\x66ilter_right\x18\x08 \x01(\x0b\x32\x1e.iterators.SavedFilterIteratorH\x01\x42\x06\n\x04leftB\x07\n\x05right\"\x96\x02\n\x13SavedFilterIterator\x12\x33\n\x0bscan_source\x18\x01 \x01(\x0b\x32\x1c.iterators.SavedScanIteratorH\x00\x12\x39\n\x0bproj_source\x18\x02 \x01(\x0b\x32\".iterators.SavedProjectionIteratorH\x00\x12\x37\n\rfilter_source\x18\x03 \x01(\x0b\x32\x1e.iterators.SavedFilterIteratorH\x00\x12\x38\n\x0bjoin_source\x18\x04 \x01(\x0b\x32!.iterators.SavedIndexJoinIteratorH\x00\x12\x12\n\nexpression\x18\x05 \x01(\tB\x08\n\x06source\"\xc2\x01\n\x08RootTree\x12\x39\n\x0bproj_source\x18\x01 \x01(\x0b\x32\".iterators.SavedProjectionIteratorH\x00\x12\x38\n\x0cunion_source\x18\x02 \x01(\x0b\x32 .iterators.SavedBagUnionIteratorH\x00\x12\x37\n\rfilter_source\x18\x03 \x01(\x0b\x32\x1e.iterators.SavedFilterIteratorH\x00\x42\x08\n\x06sourceb\x06proto3')
)




_TRIPLEPATTERN = _descriptor.Descriptor(
  name='TriplePattern',
  full_name='iterators.TriplePattern',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject', full_name='iterators.TriplePattern.subject', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predicate', full_name='iterators.TriplePattern.predicate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='iterators.TriplePattern.object', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph', full_name='iterators.TriplePattern.graph', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=112,
)


_SAVEDSCANITERATOR = _descriptor.Descriptor(
  name='SavedScanIterator',
  full_name='iterators.SavedScanIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='triple', full_name='iterators.SavedScanIterator.triple', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_read', full_name='iterators.SavedScanIterator.last_read', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardinality', full_name='iterators.SavedScanIterator.cardinality', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=215,
)


_SAVEDPROJECTIONITERATOR = _descriptor.Descriptor(
  name='SavedProjectionIterator',
  full_name='iterators.SavedProjectionIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='iterators.SavedProjectionIterator.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_source', full_name='iterators.SavedProjectionIterator.scan_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='join_source', full_name='iterators.SavedProjectionIterator.join_source', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_source', full_name='iterators.SavedProjectionIterator.union_source', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_source', full_name='iterators.SavedProjectionIterator.filter_source', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='iterators.SavedProjectionIterator.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=218,
  serialized_end=495,
)


_SAVEDINDEXJOINITERATOR_MUCENTRY = _descriptor.Descriptor(
  name='MucEntry',
  full_name='iterators.SavedIndexJoinIterator.MucEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='iterators.SavedIndexJoinIterator.MucEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='iterators.SavedIndexJoinIterator.MucEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=794,
)

_SAVEDINDEXJOINITERATOR = _descriptor.Descriptor(
  name='SavedIndexJoinIterator',
  full_name='iterators.SavedIndexJoinIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_source', full_name='iterators.SavedIndexJoinIterator.scan_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='join_source', full_name='iterators.SavedIndexJoinIterator.join_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inner', full_name='iterators.SavedIndexJoinIterator.inner', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='muc', full_name='iterators.SavedIndexJoinIterator.muc', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_read', full_name='iterators.SavedIndexJoinIterator.last_read', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SAVEDINDEXJOINITERATOR_MUCENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='iterators.SavedIndexJoinIterator.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=498,
  serialized_end=804,
)


_SAVEDBAGUNIONITERATOR = _descriptor.Descriptor(
  name='SavedBagUnionIterator',
  full_name='iterators.SavedBagUnionIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proj_left', full_name='iterators.SavedBagUnionIterator.proj_left', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_left', full_name='iterators.SavedBagUnionIterator.union_left', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='join_left', full_name='iterators.SavedBagUnionIterator.join_left', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_left', full_name='iterators.SavedBagUnionIterator.filter_left', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proj_right', full_name='iterators.SavedBagUnionIterator.proj_right', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_right', full_name='iterators.SavedBagUnionIterator.union_right', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='join_right', full_name='iterators.SavedBagUnionIterator.join_right', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_right', full_name='iterators.SavedBagUnionIterator.filter_right', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='left', full_name='iterators.SavedBagUnionIterator.left',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='right', full_name='iterators.SavedBagUnionIterator.right',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=807,
  serialized_end=1299,
)


_SAVEDFILTERITERATOR = _descriptor.Descriptor(
  name='SavedFilterIterator',
  full_name='iterators.SavedFilterIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_source', full_name='iterators.SavedFilterIterator.scan_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proj_source', full_name='iterators.SavedFilterIterator.proj_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_source', full_name='iterators.SavedFilterIterator.filter_source', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='join_source', full_name='iterators.SavedFilterIterator.join_source', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expression', full_name='iterators.SavedFilterIterator.expression', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='iterators.SavedFilterIterator.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1302,
  serialized_end=1580,
)


_ROOTTREE = _descriptor.Descriptor(
  name='RootTree',
  full_name='iterators.RootTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proj_source', full_name='iterators.RootTree.proj_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_source', full_name='iterators.RootTree.union_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_source', full_name='iterators.RootTree.filter_source', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='iterators.RootTree.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1583,
  serialized_end=1777,
)

_SAVEDSCANITERATOR.fields_by_name['triple'].message_type = _TRIPLEPATTERN
_SAVEDPROJECTIONITERATOR.fields_by_name['scan_source'].message_type = _SAVEDSCANITERATOR
_SAVEDPROJECTIONITERATOR.fields_by_name['join_source'].message_type = _SAVEDINDEXJOINITERATOR
_SAVEDPROJECTIONITERATOR.fields_by_name['union_source'].message_type = _SAVEDBAGUNIONITERATOR
_SAVEDPROJECTIONITERATOR.fields_by_name['filter_source'].message_type = _SAVEDFILTERITERATOR
_SAVEDPROJECTIONITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDPROJECTIONITERATOR.fields_by_name['scan_source'])
_SAVEDPROJECTIONITERATOR.fields_by_name['scan_source'].containing_oneof = _SAVEDPROJECTIONITERATOR.oneofs_by_name['source']
_SAVEDPROJECTIONITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDPROJECTIONITERATOR.fields_by_name['join_source'])
_SAVEDPROJECTIONITERATOR.fields_by_name['join_source'].containing_oneof = _SAVEDPROJECTIONITERATOR.oneofs_by_name['source']
_SAVEDPROJECTIONITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDPROJECTIONITERATOR.fields_by_name['union_source'])
_SAVEDPROJECTIONITERATOR.fields_by_name['union_source'].containing_oneof = _SAVEDPROJECTIONITERATOR.oneofs_by_name['source']
_SAVEDPROJECTIONITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDPROJECTIONITERATOR.fields_by_name['filter_source'])
_SAVEDPROJECTIONITERATOR.fields_by_name['filter_source'].containing_oneof = _SAVEDPROJECTIONITERATOR.oneofs_by_name['source']
_SAVEDINDEXJOINITERATOR_MUCENTRY.containing_type = _SAVEDINDEXJOINITERATOR
_SAVEDINDEXJOINITERATOR.fields_by_name['scan_source'].message_type = _SAVEDSCANITERATOR
_SAVEDINDEXJOINITERATOR.fields_by_name['join_source'].message_type = _SAVEDINDEXJOINITERATOR
_SAVEDINDEXJOINITERATOR.fields_by_name['inner'].message_type = _TRIPLEPATTERN
_SAVEDINDEXJOINITERATOR.fields_by_name['muc'].message_type = _SAVEDINDEXJOINITERATOR_MUCENTRY
_SAVEDINDEXJOINITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDINDEXJOINITERATOR.fields_by_name['scan_source'])
_SAVEDINDEXJOINITERATOR.fields_by_name['scan_source'].containing_oneof = _SAVEDINDEXJOINITERATOR.oneofs_by_name['source']
_SAVEDINDEXJOINITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDINDEXJOINITERATOR.fields_by_name['join_source'])
_SAVEDINDEXJOINITERATOR.fields_by_name['join_source'].containing_oneof = _SAVEDINDEXJOINITERATOR.oneofs_by_name['source']
_SAVEDBAGUNIONITERATOR.fields_by_name['proj_left'].message_type = _SAVEDPROJECTIONITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['union_left'].message_type = _SAVEDBAGUNIONITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['join_left'].message_type = _SAVEDINDEXJOINITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['filter_left'].message_type = _SAVEDFILTERITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['proj_right'].message_type = _SAVEDPROJECTIONITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['union_right'].message_type = _SAVEDBAGUNIONITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['join_right'].message_type = _SAVEDINDEXJOINITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['filter_right'].message_type = _SAVEDFILTERITERATOR
_SAVEDBAGUNIONITERATOR.oneofs_by_name['left'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['proj_left'])
_SAVEDBAGUNIONITERATOR.fields_by_name['proj_left'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['left']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['left'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['union_left'])
_SAVEDBAGUNIONITERATOR.fields_by_name['union_left'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['left']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['left'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['join_left'])
_SAVEDBAGUNIONITERATOR.fields_by_name['join_left'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['left']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['left'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['filter_left'])
_SAVEDBAGUNIONITERATOR.fields_by_name['filter_left'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['left']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['right'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['proj_right'])
_SAVEDBAGUNIONITERATOR.fields_by_name['proj_right'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['right']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['right'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['union_right'])
_SAVEDBAGUNIONITERATOR.fields_by_name['union_right'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['right']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['right'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['join_right'])
_SAVEDBAGUNIONITERATOR.fields_by_name['join_right'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['right']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['right'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['filter_right'])
_SAVEDBAGUNIONITERATOR.fields_by_name['filter_right'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['right']
_SAVEDFILTERITERATOR.fields_by_name['scan_source'].message_type = _SAVEDSCANITERATOR
_SAVEDFILTERITERATOR.fields_by_name['proj_source'].message_type = _SAVEDPROJECTIONITERATOR
_SAVEDFILTERITERATOR.fields_by_name['filter_source'].message_type = _SAVEDFILTERITERATOR
_SAVEDFILTERITERATOR.fields_by_name['join_source'].message_type = _SAVEDINDEXJOINITERATOR
_SAVEDFILTERITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDFILTERITERATOR.fields_by_name['scan_source'])
_SAVEDFILTERITERATOR.fields_by_name['scan_source'].containing_oneof = _SAVEDFILTERITERATOR.oneofs_by_name['source']
_SAVEDFILTERITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDFILTERITERATOR.fields_by_name['proj_source'])
_SAVEDFILTERITERATOR.fields_by_name['proj_source'].containing_oneof = _SAVEDFILTERITERATOR.oneofs_by_name['source']
_SAVEDFILTERITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDFILTERITERATOR.fields_by_name['filter_source'])
_SAVEDFILTERITERATOR.fields_by_name['filter_source'].containing_oneof = _SAVEDFILTERITERATOR.oneofs_by_name['source']
_SAVEDFILTERITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDFILTERITERATOR.fields_by_name['join_source'])
_SAVEDFILTERITERATOR.fields_by_name['join_source'].containing_oneof = _SAVEDFILTERITERATOR.oneofs_by_name['source']
_ROOTTREE.fields_by_name['proj_source'].message_type = _SAVEDPROJECTIONITERATOR
_ROOTTREE.fields_by_name['union_source'].message_type = _SAVEDBAGUNIONITERATOR
_ROOTTREE.fields_by_name['filter_source'].message_type = _SAVEDFILTERITERATOR
_ROOTTREE.oneofs_by_name['source'].fields.append(
  _ROOTTREE.fields_by_name['proj_source'])
_ROOTTREE.fields_by_name['proj_source'].containing_oneof = _ROOTTREE.oneofs_by_name['source']
_ROOTTREE.oneofs_by_name['source'].fields.append(
  _ROOTTREE.fields_by_name['union_source'])
_ROOTTREE.fields_by_name['union_source'].containing_oneof = _ROOTTREE.oneofs_by_name['source']
_ROOTTREE.oneofs_by_name['source'].fields.append(
  _ROOTTREE.fields_by_name['filter_source'])
_ROOTTREE.fields_by_name['filter_source'].containing_oneof = _ROOTTREE.oneofs_by_name['source']
DESCRIPTOR.message_types_by_name['TriplePattern'] = _TRIPLEPATTERN
DESCRIPTOR.message_types_by_name['SavedScanIterator'] = _SAVEDSCANITERATOR
DESCRIPTOR.message_types_by_name['SavedProjectionIterator'] = _SAVEDPROJECTIONITERATOR
DESCRIPTOR.message_types_by_name['SavedIndexJoinIterator'] = _SAVEDINDEXJOINITERATOR
DESCRIPTOR.message_types_by_name['SavedBagUnionIterator'] = _SAVEDBAGUNIONITERATOR
DESCRIPTOR.message_types_by_name['SavedFilterIterator'] = _SAVEDFILTERITERATOR
DESCRIPTOR.message_types_by_name['RootTree'] = _ROOTTREE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TriplePattern = _reflection.GeneratedProtocolMessageType('TriplePattern', (_message.Message,), dict(
  DESCRIPTOR = _TRIPLEPATTERN,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.TriplePattern)
  ))
_sym_db.RegisterMessage(TriplePattern)

SavedScanIterator = _reflection.GeneratedProtocolMessageType('SavedScanIterator', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDSCANITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedScanIterator)
  ))
_sym_db.RegisterMessage(SavedScanIterator)

SavedProjectionIterator = _reflection.GeneratedProtocolMessageType('SavedProjectionIterator', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDPROJECTIONITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedProjectionIterator)
  ))
_sym_db.RegisterMessage(SavedProjectionIterator)

SavedIndexJoinIterator = _reflection.GeneratedProtocolMessageType('SavedIndexJoinIterator', (_message.Message,), dict(

  MucEntry = _reflection.GeneratedProtocolMessageType('MucEntry', (_message.Message,), dict(
    DESCRIPTOR = _SAVEDINDEXJOINITERATOR_MUCENTRY,
    __module__ = 'iterators_pb2'
    # @@protoc_insertion_point(class_scope:iterators.SavedIndexJoinIterator.MucEntry)
    ))
  ,
  DESCRIPTOR = _SAVEDINDEXJOINITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedIndexJoinIterator)
  ))
_sym_db.RegisterMessage(SavedIndexJoinIterator)
_sym_db.RegisterMessage(SavedIndexJoinIterator.MucEntry)

SavedBagUnionIterator = _reflection.GeneratedProtocolMessageType('SavedBagUnionIterator', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDBAGUNIONITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedBagUnionIterator)
  ))
_sym_db.RegisterMessage(SavedBagUnionIterator)

SavedFilterIterator = _reflection.GeneratedProtocolMessageType('SavedFilterIterator', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDFILTERITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedFilterIterator)
  ))
_sym_db.RegisterMessage(SavedFilterIterator)

RootTree = _reflection.GeneratedProtocolMessageType('RootTree', (_message.Message,), dict(
  DESCRIPTOR = _ROOTTREE,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.RootTree)
  ))
_sym_db.RegisterMessage(RootTree)


_SAVEDINDEXJOINITERATOR_MUCENTRY.has_options = True
_SAVEDINDEXJOINITERATOR_MUCENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
