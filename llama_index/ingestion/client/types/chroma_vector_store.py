# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class ChromaVectorStore(pydantic.BaseModel):
    """
    Chroma vector store.

    In this vector store, embeddings are stored within a ChromaDB collection.

    During query time, the index uses ChromaDB to query for the top
    k most similar nodes.

    Args:
        chroma_collection (chromadb.api.models.Collection.Collection):
            ChromaDB collection instance
    """

    stores_text: typing.Optional[bool]
    is_embedding_query: typing.Optional[bool]
    flat_metadata: typing.Optional[bool]
    collection_name: typing.Optional[str]
    host: typing.Optional[str]
    port: typing.Optional[str]
    ssl: bool
    headers: typing.Optional[typing.Dict[str, str]]
    collection_kwargs: typing.Optional[typing.Dict[str, typing.Any]]
    class_name: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
