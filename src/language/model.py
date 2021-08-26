from dataclasses import *
from typing import *

@dataclass
class DiagramElement:
    type: str
    alias: str
    calls: List[str]

@dataclass
class Relations:
    relations: List[Tuple[str, str]]

@dataclass
class Diagram:
    elements: List[DiagramElement]
    relations: Relations