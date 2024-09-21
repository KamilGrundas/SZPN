import time
import asyncio
from typing import Optional, Callable


class Timer:
    def __init__(self):
        self.value: Optional[float] = 0
        self.running = False
        self.on_change_callback: Optional[Callable[[float], None]] = None

    def get_time(self):
        if self.value is not None:
            return round(self.value, 2)
        return None

    def get_formatted_time(self):
        return "{:.2f}".format(self.value)

    async def start(self):
        self.running = True
        start_time = time.time()
        while self.running:
            await asyncio.sleep(0.02)
            current_time = time.time()
            self.value += current_time - start_time
            start_time = current_time
            if self.on_change_callback:
                self.on_change_callback(self.value)

    def reset(self):
        self.running = False
        self.value = 0
        if self.on_change_callback:
            self.on_change_callback(self.value)

    def on_change(self, callback: Callable[[float], None]):
        """Assign a callback function to be called when the time changes."""
        self.on_change_callback = callback