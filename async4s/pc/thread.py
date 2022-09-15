#!/usr/bin/env python

"""
Producer-Consumer模型
"""

from __future__ import annotations

from queue import Queue
import abc
import threading


class PC(metaclass=abc.ABCMeta):
    def __init__(self, buffer_size=1024):
        self.buffer = Queue(buffer_size)

    @abc.abstractmethod
    def produce(self):
        pass

    @abc.abstractmethod
    def consume(self):
        pass

    def start(self):
        self.producer = threading.Thread(target=self.produce, name=f"{self.__class__.__name__}.produce", daemon=True)
        self.consumer = threading.Thread(target=self.consume, name=f"{self.__class__.__name__}.consume", daemon=True)
        self.producer.start()
        self.consumer.start()

    def join(self):
        self.producer.join()
        self.consumer.join()
