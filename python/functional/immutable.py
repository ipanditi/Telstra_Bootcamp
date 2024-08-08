from dataclasses import dataclass
@dataclass(frozen=True)
class Immutable:
    x:int
    y:int
i = Immutable(1,2)
i.x=10