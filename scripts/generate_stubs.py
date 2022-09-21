import inspect
import typing
from collections import deque
from copy import deepcopy
from pathlib import Path

import tortoise.fields.base
from tortoise import fields
from tortoise.fields.relational import ForeignKeyField

mfields = []
for field in sorted(list(set(fields.__all__))):
    field_val = getattr(fields, field)
    if (
        inspect.isclass(field_val)
        and issubclass(field_val, tortoise.fields.base.Field)
        and field_val.__module__ == "tortoise.fields.data"
    ):
        mfields.append((field, typing.get_args(field_val.__orig_bases__[0])[0]))

s = inspect.signature(tortoise.fields.base.Field.__init__)
params = dict(s.parameters.items())
del params["self"]
nullable_params = deepcopy(params)
nullable_params["null"] = nullable_params["null"].replace(annotation=typing.Literal[True])
non_nullable_params = deepcopy(params)
non_nullable_params["null"] = non_nullable_params["null"].replace(annotation=typing.Literal[False])

deq = deque()
p = deq.append
p(
    """
import datetime
import decimal
import uuid
from typing import Any, Callable, List, Literal, Optional, Union, overload

import tortoise
import tortoise.fields
import tortoise.validators
from tortoise.models import Model
from tortoise.fields import *
"""
)

for n, f in mfields:
    p(f"@overload\ndef {n}{s.replace(parameters=non_nullable_params.values(), return_annotation=f)}: ...")
    p(f"@overload\ndef {n}{s.replace(parameters=nullable_params.values(), return_annotation=typing.Optional[f])}: ...")
    p(f"def {n}{s.replace(parameters=params.values(), return_annotation=inspect._empty)}: ...")

p(f"\ndef ForeignKeyField{inspect.signature(ForeignKeyField).replace(return_annotation=typing.Any)}: ...")

Path(__file__).parent.parent.joinpath("tortoise-stubs/fields/__init__.pyi").write_text(
    "\n".join(deq).replace("NoneType", "None")
)
