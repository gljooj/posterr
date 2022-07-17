import abc
from abc import ABC


from src.infra.database.database_config import DataBaseConfig


class AbstractRepository(ABC, DataBaseConfig):
    def __int__(self):
        super().__class__()

    @abc.abstractmethod
    def get_by_filter(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_filter_paginate(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def insert_new(self, data):
        raise NotImplementedError

