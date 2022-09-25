# types-tortoise

Type stubs that make tortoise-orm a lot easier to work with when using type checkers.

Specifically,

* ForeignKeyField can be typehinted without an extra type ignore
* OneToOneField can be typehinted without an extra type ignore
* Data fields' types are now automatically typehinted as the primitive types they describe, not Field subclasses
* Data fields' types automatically reflect the value of null argument (i.e. become optional if you set null=True)
