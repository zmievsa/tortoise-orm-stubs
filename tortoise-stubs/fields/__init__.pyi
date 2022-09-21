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
def BigIntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> int: ...
@overload
def BigIntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[int]: ...
def BigIntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def BinaryField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> bytes: ...
@overload
def BinaryField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[bytes]: ...
def BinaryField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def BooleanField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> bool: ...
@overload
def BooleanField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[bool]: ...
def BooleanField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def CharField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> str: ...
@overload
def CharField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[str]: ...
def CharField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def DateField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> datetime.date: ...
@overload
def DateField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[datetime.date]: ...
def DateField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def DatetimeField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> datetime.datetime: ...
@overload
def DatetimeField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[datetime.datetime]: ...
def DatetimeField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def DecimalField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> decimal.Decimal: ...
@overload
def DecimalField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[decimal.Decimal]: ...
def DecimalField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def FloatField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> float: ...
@overload
def FloatField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[float]: ...
def FloatField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def IntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> int: ...
@overload
def IntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[int]: ...
def IntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def JSONField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Union[dict, list]: ...
@overload
def JSONField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Union[dict, list, None]: ...
def JSONField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def SmallIntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> int: ...
@overload
def SmallIntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[int]: ...
def SmallIntField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def TextField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> str: ...
@overload
def TextField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[str]: ...
def TextField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def TimeDeltaField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> datetime.timedelta: ...
@overload
def TimeDeltaField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[datetime.timedelta]: ...
def TimeDeltaField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def TimeField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> datetime.time: ...
@overload
def TimeField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[datetime.time]: ...
def TimeField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
@overload
def UUIDField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[False] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> uuid.UUID: ...
@overload
def UUIDField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: Literal[True] = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
) -> Optional[uuid.UUID]: ...
def UUIDField(
    source_field: Optional[str] = None,
    generated: bool = False,
    pk: bool = False,
    null: bool = False,
    default: Any = None,
    unique: bool = False,
    index: bool = False,
    description: Optional[str] = None,
    model: "Optional[Model]" = None,
    validators: Optional[List[Union[tortoise.validators.Validator, Callable]]] = None,
    **kwargs: Any
): ...
def ForeignKeyField(
    model_name: str,
    related_name: Union[str, None, Literal[False]] = None,
    on_delete: str = "CASCADE",
    db_constraint: bool = True,
    **kwargs: Any
) -> Any: ...
