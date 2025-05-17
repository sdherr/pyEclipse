from sector import Sector


class Table:
    map: dict[int, dict[int, Sector | None]]  # 2-d dict using our q and r Axial coordinates
    placedSectors: list[Sector]
    deepWarpNexus: Sector
