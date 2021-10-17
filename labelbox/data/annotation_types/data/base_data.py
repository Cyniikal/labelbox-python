from abc import ABC, abstractmethod
from typing import Optional

from pydantic import BaseModel


class BaseData(BaseModel, ABC):
    """
    Base class for objects representing data.
    This class shouldn't directly be used
    """
    external_id: Optional[str] = None
    uid: Optional[str] = None

    @classmethod
    @abstractmethod
    def from_data_row(cls, data_row):
        pass
