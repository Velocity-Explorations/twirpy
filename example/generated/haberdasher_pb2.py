# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: haberdasher.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'haberdasher.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11haberdasher.proto\x12\x14twitch.twirp.example\">\n\x03Hat\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12\x11\n\x04name\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\x16\n\x04Size\x12\x0e\n\x06inches\x18\x01 \x01(\x05\x32O\n\x0bHaberdasher\x12@\n\x07MakeHat\x12\x1a.twitch.twirp.example.Size\x1a\x19.twitch.twirp.example.HatB\tZ\x07\x65xampleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'haberdasher_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\007example'
  _globals['_HAT']._serialized_start=43
  _globals['_HAT']._serialized_end=105
  _globals['_SIZE']._serialized_start=107
  _globals['_SIZE']._serialized_end=129
  _globals['_HABERDASHER']._serialized_start=131
  _globals['_HABERDASHER']._serialized_end=210
# @@protoc_insertion_point(module_scope)
