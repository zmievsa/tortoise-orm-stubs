import datetime
import decimal
import uuid
from typing import Any, Callable, List, Literal, Optional, Union, overload

import tortoise.fields
import tortoise.validators
from tortoise.fields.base import (
    CASCADE,
    NO_ACTION,
    RESTRICT,
    SET_DEFAULT,
    SET_NULL,
    Field,
)
from tortoise.fields.data import (
    BigIntField,
    BinaryField,
    BooleanField,
    CharEnumField,
    CharField,
    DateField,
    DatetimeField,
    DecimalField,
    FloatField,
    IntEnumField,
    IntField,
    JSONField,
    SmallIntField,
    TextField,
    TimeDeltaField,
    TimeField,
    UUIDField,
)
from tortoise.fields.relational import (
    BackwardFKRelation,
    BackwardOneToOneRelation,
    ForeignKeyField,
    ForeignKeyNullableRelation,
    ForeignKeyRelation,
    ManyToManyField,
    ManyToManyRelation,
    OneToOneField,
    OneToOneNullableRelation,
    OneToOneRelation,
    ReverseRelation,
)
from tortoise.models import Model

__all__ = [
    "CASCADE",
    "RESTRICT",
    "SET_DEFAULT",
    "SET_NULL",
    "NO_ACTION",
    "Field",
    "BigIntField",
    "BinaryField",
    "BooleanField",
    "CharEnumField",
    "CharField",
    "DateField",
    "DatetimeField",
    "TimeField",
    "DecimalField",
    "FloatField",
    "IntEnumField",
    "IntField",
    "JSONField",
    "SmallIntField",
    "SmallIntField",
    "TextField",
    "TimeDeltaField",
    "UUIDField",
    "BackwardFKRelation",
    "BackwardOneToOneRelation",
    "ForeignKeyField",
    "ForeignKeyNullableRelation",
    "ForeignKeyRelation",
    "ManyToManyField",
    "ManyToManyRelation",
    "OneToOneField",
    "OneToOneNullableRelation",
    "OneToOneRelation",
    "ReverseRelation",
]

@overload
def BigIntField(pk: bool = False, null: Literal[False] = False, **kwargs: Any) -> int: ...
@overload
def BigIntField(pk: bool = False, null: Literal[True] = False, **kwargs: Any) -> Union[int, None]: ...
def BigIntField(pk: bool = False, null: bool = False, **kwargs: Any):
    """
    Big integer field. (64-bit signed)

    ``pk`` (bool):
        True if field is Primary Key.
    """

@overload
def BinaryField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> bytes: ...
@overload
def BinaryField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> Union[bytes, None]: ...
def BinaryField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
):
    """
    Binary field.

    This is for storing ``bytes`` objects.
    Note that filter or queryset-update operations are not supported.
    """

@overload
def BooleanField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> bool: ...
@overload
def BooleanField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> Union[bool, None]: ...
def BooleanField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
):
    """
    Boolean field.
    """

@overload
def CharField(max_length: int = Ellipsis, null: Literal[False] = False, **kwargs: Any) -> str: ...
@overload
def CharField(max_length: int = Ellipsis, null: Literal[True] = False, **kwargs: Any) -> Union[str, None]: ...
def CharField(max_length: int = Ellipsis, null: bool = False, **kwargs: Any):
    """
    Character field.

    You must provide the following:

    ``max_length`` (int):
        Maximum length of the field in characters.
    """

@overload
def DateField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> datetime.date: ...
@overload
def DateField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> Union[datetime.date, None]: ...
def DateField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
):
    """
    Date field.
    """

@overload
def DatetimeField(
    auto_now: bool = False, auto_now_add: bool = False, null: Literal[False] = False, **kwargs: Any
) -> datetime.datetime: ...
@overload
def DatetimeField(
    auto_now: bool = False, auto_now_add: bool = False, null: Literal[True] = False, **kwargs: Any
) -> Union[datetime.datetime, None]: ...
def DatetimeField(auto_now: bool = False, auto_now_add: bool = False, null: bool = False, **kwargs: Any):
    """
    Datetime field.

    ``auto_now`` and ``auto_now_add`` is exclusive.
    You can opt to set neither or only ONE of them.

    ``auto_now`` (bool):
        Always set to ``datetime.utcnow()`` on save.
    ``auto_now_add`` (bool):
        Set to ``datetime.utcnow()`` on first save only.
    """

@overload
def DecimalField(
    max_digits: int = Ellipsis, decimal_places: int = Ellipsis, null: Literal[False] = False, **kwargs: Any
) -> decimal.Decimal: ...
@overload
def DecimalField(
    max_digits: int = Ellipsis, decimal_places: int = Ellipsis, null: Literal[True] = False, **kwargs: Any
) -> Union[decimal.Decimal, None]: ...
def DecimalField(max_digits: int = Ellipsis, decimal_places: int = Ellipsis, null: bool = False, **kwargs: Any):
    """
    Accurate decimal field.

    You must provide the following:

    ``max_digits`` (int):
        Max digits of significance of the decimal field.
    ``decimal_places`` (int):
        How many of those significant digits is after the decimal point.
    """

@overload
def FloatField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> float: ...
@overload
def FloatField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> Union[float, None]: ...
def FloatField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
):
    """
    Float (double) field.
    """

@overload
def IntField(pk: bool = False, null: Literal[False] = False, **kwargs: Any) -> int: ...
@overload
def IntField(pk: bool = False, null: Literal[True] = False, **kwargs: Any) -> Union[int, None]: ...
def IntField(pk: bool = False, null: bool = False, **kwargs: Any):
    """
    Integer field. (32-bit signed)

    ``pk`` (bool):
        True if field is Primary Key.
    """

@overload
def JSONField(
    encoder: Callable[[Any], str] = Ellipsis,
    decoder: Callable[[Union[str, bytes]], Any] = Ellipsis,
    null: Literal[False] = False,
    **kwargs: Any
) -> Union[dict, list]: ...
@overload
def JSONField(
    encoder: Callable[[Any], str] = Ellipsis,
    decoder: Callable[[Union[str, bytes]], Any] = Ellipsis,
    null: Literal[True] = False,
    **kwargs: Any
) -> Union[dict, list, None]: ...
def JSONField(
    encoder: Callable[[Any], str] = Ellipsis,
    decoder: Callable[[Union[str, bytes]], Any] = Ellipsis,
    null: bool = False,
    **kwargs: Any
):
    """
    JSON field.

    This field can store dictionaries or lists of any JSON-compliant structure.

    You can specify your own custom JSON encoder/decoder, leaving at the default should work well.
    If you have ``python-rapidjson`` installed, we default to using that,
    else the default ``json`` module will be used.

    ``encoder``:
        The custom JSON encoder.
    ``decoder``:
        The custom JSON decoder.

    """

@overload
def SmallIntField(pk: bool = False, null: Literal[False] = False, **kwargs: Any) -> int: ...
@overload
def SmallIntField(pk: bool = False, null: Literal[True] = False, **kwargs: Any) -> Union[int, None]: ...
def SmallIntField(pk: bool = False, null: bool = False, **kwargs: Any):
    """
    Small integer field. (16-bit signed)

    ``pk`` (bool):
        True if field is Primary Key.
    """

@overload
def TextField(
    pk: bool = False, unique: bool = False, index: bool = False, null: Literal[False] = False, **kwargs: Any
) -> str: ...
@overload
def TextField(
    pk: bool = False, unique: bool = False, index: bool = False, null: Literal[True] = False, **kwargs: Any
) -> Union[str, None]: ...
def TextField(pk: bool = False, unique: bool = False, index: bool = False, null: bool = False, **kwargs: Any):
    """
    Large Text field.
    """

@overload
def TimeDeltaField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> datetime.timedelta: ...
@overload
def TimeDeltaField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
) -> Union[datetime.timedelta, None]: ...
def TimeDeltaField(
    source_field: Union[str, None] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Union[str, None] = None,
    model: "Optional[Model]" = None,
    validators: Union[List[Union[tortoise.validators.Validator, Callable]], None] = None,
    **kwargs: Any
):
    """
    A field for storing time differences.
    """

@overload
def TimeField(
    auto_now: bool = False, auto_now_add: bool = False, null: Literal[False] = False, **kwargs: Any
) -> datetime.time: ...
@overload
def TimeField(
    auto_now: bool = False, auto_now_add: bool = False, null: Literal[True] = False, **kwargs: Any
) -> Union[datetime.time, None]: ...
def TimeField(auto_now: bool = False, auto_now_add: bool = False, null: bool = False, **kwargs: Any):
    """
    Time field.
    """

@overload
def UUIDField(null: Literal[False] = False, **kwargs: Any) -> uuid.UUID: ...
@overload
def UUIDField(null: Literal[True] = False, **kwargs: Any) -> Union[uuid.UUID, None]: ...
def UUIDField(null: bool = False, **kwargs: Any):
    """
    UUID Field

    This field can store uuid value.

    If used as a primary key, it will auto-generate a UUID4 by default.
    """

def ForeignKeyField(
    model_name: str,
    related_name: Union[str, None, Literal[False]] = None,
    on_delete: str = "CASCADE",
    db_constraint: bool = True,
    **kwargs: Any
) -> Any: ...
