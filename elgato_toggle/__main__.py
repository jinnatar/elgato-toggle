import asyncio
from typing import Optional

from elgato import Elgato, State, Info

async def main():
    """Toggle lights."""
    domain = 'dyn.nocturnal.fi'
    state = await toggle(f'keylight-left.{domain}')
    await set_state(f'keylight-right.{domain}', on=state)

async def set_state(hostname: str, on: bool):
    """Set on state for a single light."""

    async with Elgato(hostname) as elgato:
        state: State = await elgato.state()
        await elgato.light(on=on)

async def toggle(hostname: str) -> bool:
    """Toggle a single light."""

    async with Elgato(hostname) as elgato:
        state: State = await elgato.state()
        await elgato.light(on=(not state.on))
        return (not state.on)

def run():
    asyncio.run(main())

if __name__ == "__main__":
    run()
