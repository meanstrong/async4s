#!/usr/bin/env python

"""
Producer-Consumer模型
"""

from __future__ import annotations

import asyncio
import abc


class PC(metaclass=abc.ABCMeta):
    def __init__(self, buffer_size=1024):
        self.buffer = asyncio.Queue(buffer_size)

    @abc.abstractmethod
    async def produce(self):
        pass

    @abc.abstractmethod
    async def consume(self):
        pass

    async def start(self):
        producer = asyncio.ensure_future(self.produce())
        consumer = asyncio.ensure_future(self.consume())
        return await asyncio.gather(producer, consumer)
