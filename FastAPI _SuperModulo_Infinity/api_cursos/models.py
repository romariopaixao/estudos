from typing import Optional
from pydantic import BaseModel
import random

class Curso(BaseModel):
    id: Optional[int] = random.randint(4,100)
    titulo: str
    aulas: int
    horas: int