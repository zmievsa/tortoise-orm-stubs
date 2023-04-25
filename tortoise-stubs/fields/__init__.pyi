import datetime
import decimal
import typing
import uuid
from typing import Any, Callable, List, Literal, Optional, Type, Union, overload

import tortoise.fields.base
import tortoise.validators
from tortoise.fields.base import NO_ACTION, SET_DEFAULT, Field
from tortoise.fields.data import CharEnumType, IntEnumType
from tortoise.fields.relational import (
    CASCADE,
    RESTRICT,
    SET_NULL,
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
def BigIntField(pk: bool = False, *, null: Literal[False] = False, **kwargs: Any) -> tortoise.fields.base.Field[int]:
    """
    Big integer field. (64-bit signed)

    ``pk`` (bool):
        True if field is Primary Key.
    """

@overload
def BigIntField(
    pk: bool = False, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[int]]: ...
@overload
def BinaryField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[bytes]:
    """
    Binary field.

    This is for storing ``bytes`` objects.
    Note that filter or queryset-update operations are not supported.
    """

@overload
def BinaryField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[True],
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[typing.Optional[bytes]]: ...
@overload
def BooleanField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[bool]:
    """
    Boolean field.
    """

@overload
def BooleanField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[True],
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[typing.Optional[bool]]: ...
@overload
def CharEnumField(
    enum_type: Type[CharEnumType],
    description: Optional[str] = None,
    max_length: int = 0,
    *,
    null: Literal[False] = False,
    **kwargs: Any,
) -> tortoise.fields.base.Field[CharEnumType]:
    """
    Char Enum Field

    A field representing a character enumeration.

    **Warning**: If ``max_length`` is not specified or equals to zero, the size of represented
    char fields is automatically detected. So if later you update the enum, you need to update your
    table schema as well.

    **Note**: Valid str value of ``enum_type`` is acceptable.

    ``enum_type``:
        The enum class
    ``description``:
        The description of the field. It is set automatically if not specified to a multiline list
        of "name: value" pairs.
    ``max_length``:
        The length of the created CharField. If it is zero it is automatically detected from
        enum_type.

    """

@overload
def CharEnumField(
    enum_type: Type[CharEnumType],
    description: Optional[str] = None,
    max_length: int = 0,
    *,
    null: Literal[True],
    **kwargs: Any,
) -> tortoise.fields.base.Field[typing.Optional[CharEnumType]]: ...
@overload
def CharField(max_length: int, *, null: Literal[False] = False, **kwargs: Any) -> tortoise.fields.base.Field[str]:
    """
    Character field.

    You must provide the following:

    ``max_length`` (int):
        Maximum length of the field in characters.
    """

@overload
def CharField(
    max_length: int, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[str]]: ...
@overload
def DateField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[datetime.date]:
    """
    Date field.
    """

@overload
def DateField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[True],
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[typing.Optional[datetime.date]]: ...
@overload
def DatetimeField(
    auto_now: bool = False, auto_now_add: bool = False, *, null: Literal[False] = False, **kwargs: Any
) -> tortoise.fields.base.Field[datetime.datetime]:
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
def DatetimeField(
    auto_now: bool = False, auto_now_add: bool = False, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[datetime.datetime]]: ...
@overload
def DecimalField(
    max_digits: int, decimal_places: int, *, null: Literal[False] = False, **kwargs: Any
) -> tortoise.fields.base.Field[decimal.Decimal]:
    """
    Accurate decimal field.

    You must provide the following:

    ``max_digits`` (int):
        Max digits of significance of the decimal field.
    ``decimal_places`` (int):
        How many of those significant digits is after the decimal point.
    """

@overload
def DecimalField(
    max_digits: int, decimal_places: int, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[decimal.Decimal]]: ...
@overload
def FloatField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[float]:
    """
    Float (double) field.
    """

@overload
def FloatField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[True],
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[typing.Optional[float]]: ...
@overload
def IntEnumField(
    enum_type: Type[IntEnumType], description: Optional[str] = None, *, null: Literal[False] = False, **kwargs: Any
) -> tortoise.fields.base.Field[IntEnumType]:
    """
    Enum Field

    A field representing an integer enumeration.

    The description of the field is set automatically if not specified to a multiline list of
    "name: value" pairs.

    **Note**: Valid int value of ``enum_type`` is acceptable.

    ``enum_type``:
        The enum class
    ``description``:
        The description of the field. It is set automatically if not specified to a multiline list
        of "name: value" pairs.

    """

@overload
def IntEnumField(
    enum_type: Type[IntEnumType], description: Optional[str] = None, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[IntEnumType]]: ...
@overload
def IntField(pk: bool = False, *, null: Literal[False] = False, **kwargs: Any) -> tortoise.fields.base.Field[int]:
    """
    Integer field. (32-bit signed)

    ``pk`` (bool):
        True if field is Primary Key.
    """

@overload
def IntField(
    pk: bool = False, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[int]]: ...
@overload
def JSONField(
    encoder: Callable[[Any], str] = ...,
    decoder: Callable[[Union[str, bytes]], Any] = ...,
    *,
    null: Literal[False] = False,
    **kwargs: Any,
) -> tortoise.fields.base.Field[typing.Union[dict, list]]:
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
def JSONField(
    encoder: Callable[[Any], str] = ...,
    decoder: Callable[[Union[str, bytes]], Any] = ...,
    *,
    null: Literal[True],
    **kwargs: Any,
) -> tortoise.fields.base.Field[typing.Union[dict, list, None]]: ...
@overload
def SmallIntField(pk: bool = False, *, null: Literal[False] = False, **kwargs: Any) -> tortoise.fields.base.Field[int]:
    """
    Small integer field. (16-bit signed)

    ``pk`` (bool):
        True if field is Primary Key.
    """

@overload
def SmallIntField(
    pk: bool = False, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[int]]: ...
@overload
def TextField(
    pk: bool = False, unique: bool = False, index: bool = False, *, null: Literal[False] = False, **kwargs: Any
) -> tortoise.fields.base.Field[str]:
    """
    Large Text field.
    """

@overload
def TextField(
    pk: bool = False, unique: bool = False, index: bool = False, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[str]]: ...
@overload
def TimeDeltaField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[datetime.timedelta]:
    """
    A field for storing time differences.
    """

@overload
def TimeDeltaField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    *,
    null: Literal[True],
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any,
) -> tortoise.fields.base.Field[typing.Optional[datetime.timedelta]]: ...
@overload
def TimeField(
    auto_now: bool = False, auto_now_add: bool = False, *, null: Literal[False] = False, **kwargs: Any
) -> tortoise.fields.base.Field[datetime.time]:
    """
    Time field.
    """

@overload
def TimeField(
    auto_now: bool = False, auto_now_add: bool = False, *, null: Literal[True], **kwargs: Any
) -> tortoise.fields.base.Field[typing.Optional[datetime.time]]: ...
@overload
def UUIDField(*, null: Literal[False] = False, **kwargs: Any) -> tortoise.fields.base.Field[uuid.UUID]:
    """
    UUID Field

    This field can store uuid value.

    If used as a primary key, it will auto-generate a UUID4 by default.
    """

@overload
def UUIDField(*, null: Literal[True], **kwargs: Any) -> tortoise.fields.base.Field[typing.Optional[uuid.UUID]]: ...
