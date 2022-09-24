import inspect
import typing
from collections import deque
from copy import deepcopy
from pathlib import Path

import tortoise.fields.base
from tortoise import fields
from tortoise.fields.relational import ForeignKeyField


class AlternativeEllipsis:
    def __repr__(self):
        return "..."


deq = deque()
p = deq.append
p(
    """
import datetime
import decimal
import uuid
from typing import Any, Callable, List, Literal, Optional, Union, overload, Type

import tortoise.validators
from tortoise.models import Model
"""
)


mfields = []
for field_name in sorted(list(set(fields.__all__))):
    field_val = getattr(fields, field_name)
    if callable(field_val) and field_val.__module__ == "tortoise.fields.data":
        if inspect.isclass(field_val) and issubclass(field_val, tortoise.fields.base.Field):
            mfields.append((field_name, typing.get_args(field_val.__orig_bases__[0])[0], field_val))
        elif "Field" in field_name:
            mfields.append((field_name, inspect.signature(field_val).return_annotation, field_val))
        continue
    p(f"from tortoise.fields import {field_name}")


def get_signature(cls_or_func, default_params: typing.Dict[str, inspect.Parameter]):
    if inspect.isclass(cls_or_func):
        s = inspect.signature(cls_or_func.__init__)
    else:
        s = inspect.signature(cls_or_func)
    params = dict(s.parameters.items())
    params.pop("self", None)
    if "null" not in params:
        nullparam = default_params["null"]
        params_lst = list(params.items())
        params_lst = params_lst[0:-1] + [("null", nullparam)] + [params_lst[-1]]
        params = {k: v for k, v in params_lst}

    params = build_new_params(params)

    nullable_params = deepcopy(params)
    nullable_params["null"] = nullable_params["null"].replace(annotation=typing.Literal[True], default=inspect._empty)
    non_nullable_params = deepcopy(params)
    non_nullable_params["null"] = non_nullable_params["null"].replace(annotation=typing.Literal[False])
    return s, params, nullable_params, non_nullable_params


def build_new_params(params: typing.Dict[str, inspect.Parameter]):
    null_found = False
    for k, v in params.items():
        if v.kind in {inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL}:
            continue
        if callable(v.default) and v.default is not inspect._empty:
            params[k] = v.replace(default=AlternativeEllipsis())
        if null_found:
            pass
        elif k == "null":
            null_found = True
        else:
            continue

        params[k] = v.replace(kind=inspect.Parameter.KEYWORD_ONLY)
    return params


DEFAULT_PARAMS = dict(inspect.signature(tortoise.fields.base.Field.__init__).parameters.items())
del DEFAULT_PARAMS["self"]


p("__all__ = " + str(fields.__all__))

for n, f, v in mfields:
    s, params, nullable_params, non_nullable_params = get_signature(v, DEFAULT_PARAMS)
    if isinstance(f, typing.TypeVar):
        deq.appendleft(f"from tortoise.fields.data import {str(f).lstrip('~')}")
    p(
        f'@overload\ndef {n}{s.replace(parameters=non_nullable_params.values(), return_annotation=f)}:\n    """{v.__doc__ or ...}"""'.replace(
            "~", ""  # Dangerous? Yes. But what the hell else would I do with those typevars
        )
    )
    p(
        f'@overload\ndef {n}{s.replace(parameters=nullable_params.values(), return_annotation=typing.Optional[f])}:\n    """{v.__doc__ or ...}"""'.replace(
            "~", ""  # Dangerous? Yes. But what the hell else would I do with those typevars
        )
    )
    # p(f"def {n}{s.replace(parameters=params.values(), return_annotation=inspect._empty)}: ...")

p(f"\ndef ForeignKeyField{inspect.signature(ForeignKeyField).replace(return_annotation=typing.Any)}: ...")


Path(__file__).parent.parent.joinpath("tortoise-stubs/fields/__init__.pyi").write_text(
    "\n".join(deq).replace("NoneType", "None")
)
