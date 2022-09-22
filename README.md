# tortoise-stubs

Type stubs that make tortoise a bit easier to work with when using type checkers.

For example,

* ForeignKeyField can be typehinted without an extra type ignore
* Data fields' types are now typehinted as the primitive types they describe, not Field subclasses
* Data fields' types become optional for your typechecker with null=True argument
