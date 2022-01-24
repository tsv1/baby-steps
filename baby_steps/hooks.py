from typing import TYPE_CHECKING, Any, Callable, List, Type, Union

__all__ = ("add_hook", "del_hook", "HookType",)

if TYPE_CHECKING:  # pragma: nocover
    from ._step import Step
    StepType = Type[Step]
else:
    StepType = Any

NameType = Union[str, None]
HookType = Callable[[StepType, NameType], Any]

_hooks: List[HookType] = []


def add_hook(fn: HookType) -> None:
    _hooks.append(fn)


def del_hook(fn: HookType) -> None:
    _hooks.remove(fn)
