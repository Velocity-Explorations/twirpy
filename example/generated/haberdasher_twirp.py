# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: haberdasher.proto

from google.protobuf import symbol_database as _symbol_database

from twirp.base import Endpoint
from twirp.server import TwirpServer
from twirp.client import TwirpClient
from twirp.async_client import AsyncTwirpClient

try:
    from twirp.async_client import AsyncTwirpClient

    _async_available = True
except ModuleNotFoundError as e:
    print(e)
    _async_available = False

_sym_db = _symbol_database.Default()


class HaberdasherServer(TwirpServer):

    def __init__(self, *args, service, server_path_prefix="/twirp"):
        super().__init__(service=service)
        self._prefix = f"{server_path_prefix}/twitch.twirp.example.Haberdasher"
        self._endpoints = {
            "MakeHat": Endpoint(
                service_name="Haberdasher",
                name="MakeHat",
                function=getattr(service, "MakeHat"),
                input=_sym_db.GetSymbol("twitch.twirp.example.Size"),
                output=_sym_db.GetSymbol("twitch.twirp.example.Hat"),
            ),
        }


class HaberdasherClient(TwirpClient):

    def MakeHat(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
        return self._make_request(
            url=f"{server_path_prefix}/twitch.twirp.example.Haberdasher/MakeHat",
            ctx=ctx,
            request=request,
            response_obj=_sym_db.GetSymbol("twitch.twirp.example.Hat"),
            **kwargs,
        )


if _async_available:

    class AsyncHaberdasherClient(AsyncTwirpClient):

        async def MakeHat(
            self, *, ctx, request, server_path_prefix="/twirp", session=None, **kwargs
        ):
            return await self._make_request(
                url=f"{server_path_prefix}/twitch.twirp.example.Haberdasher/MakeHat",
                ctx=ctx,
                request=request,
                response_obj=_sym_db.GetSymbol("twitch.twirp.example.Hat"),
                session=session,
                **kwargs,
            )
