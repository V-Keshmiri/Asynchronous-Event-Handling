"""
Author: Vahid Keshmiri
Email: V.Keshmiry@Gmail.com

This module demonstrates asynchronous event handling using Python's asyncio library. 
The code showcases how to handle multiple events concurrently, improving responsiveness and performance.
"""

import asyncio

async def handle_event(event_name: str):
    """
    Asynchronously handles an event.

    Parameters:
    event_name (str): The name of the event to handle.

    Returns:
    None
    """
    print(f"Handling event: {event_name}")
    await asyncio.sleep(1)
    print(f"Finished handling event: {event_name}")

async def main():
    """
    Main function to handle multiple events concurrently.

    Returns:
    None
    """
    events = ["event_1", "event_2", "event_3"]
    await asyncio.gather(*(handle_event(event) for event in events))

if __name__ == "__main__":
    asyncio.run(main())
