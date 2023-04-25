import inspect
import typing
from collections import deque
from copy import deepcopy
from pathlib import Path

import tortoise.fields.base
import tortoise.fields.data
import tortoise.fields.relational
import tortoise.models
from pysh import sh
from tortoise import fields


class AlternativeEllipsis:
    def __repr__(self):
        return "..."


def get_fields(p: typing.Callable[[str], None]):
    mfields = []
    for field_name in sorted(list(set(fields.__all__))):
        field_val = getattr(fields, field_name)
        if callable(field_val) and field_val.__module__ == "tortoise.fields.data":
            if inspect.isclass(field_val) and issubclass(field_val, tortoise.fields.base.Field):
                mfields.append((field_name, typing.get_args(field_val.__orig_bases__[0])[0], field_val))
            elif "Field" in field_name:
                mfields.append((field_name, inspect.signature(field_val).return_annotation, field_val))
            continue
        if hasattr(field_val, "__module__") and "tortoise" in field_val.__module__:
            p(f"from {field_val.__module__} import {field_name}")
        elif field_name in tortoise.fields.data.__all__:
            p(f"from tortoise.fields.data import {field_name}")
        elif field_name in tortoise.fields.relational.__dict__:
            p(f"from tortoise.fields.relational import {field_name}")
        else:
            p(f"from tortoise.fields.base import {field_name}")
    return mfields


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
    return s, nullable_params, non_nullable_params


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


def get_function_def(
    name: str,
    signature: inspect.Signature,
    params: typing.Sequence[inspect.Parameter],
    return_type: typing.Any,
    doc: str = "",
) -> str:
    signature = signature.replace(parameters=params, return_annotation=return_type)
    secondline = f'''\n    """{doc}"""''' if doc else " ..."
    return f"@overload\ndef {name}{signature}:{secondline}".replace("~", "")


def get_foreign_key_def(foreign_key_func: typing.Callable) -> str:
    return f"\ndef {foreign_key_func.__name__}{inspect.signature(foreign_key_func).replace(return_annotation=typing.Any)}: ..."


def main():
    DEFAULT_PARAMS = dict(inspect.signature(tortoise.fields.base.Field.__init__).parameters.items())
    del DEFAULT_PARAMS["self"]

    deq = deque()
    p = deq.append
    mfields = get_fields(p)
    p("__all__ = " + str(list(fields.__all__)))

    for n, f, v in mfields:
        s, nullable_params, non_nullable_params = get_signature(v, DEFAULT_PARAMS)
        if isinstance(f, typing.TypeVar):
            deq.appendleft(f"from tortoise.fields.data import {str(f).lstrip('~')}")

        p(get_function_def(n, s, list(non_nullable_params.values()), tortoise.fields.base.Field[f], v.__doc__))
        p(
            get_function_def(
                n,
                s,
                list(nullable_params.values()),
                tortoise.fields.base.Field[typing.Optional[f]],
            )
        )

    deq.appendleft(
        """
import typing
import uuid
import decimal
import datetime
import tortoise.fields.base
from typing import Any, Callable, List, Literal, Optional, Union, overload, Type

import tortoise.validators
from tortoise.models import Model
"""
    )

    ROOT = Path(__file__).parent.parent
    ROOT.joinpath("tortoise-stubs/fields/__init__.pyi").write_text("\n".join(deq).replace("NoneType", "None"))
    sh("make format", cwd=ROOT)


if __name__ == "__main__":
    main()
