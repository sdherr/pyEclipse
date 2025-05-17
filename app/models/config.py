class Config:
    number_of_players: int = 6
    # Rise of the Ancients
    rota_discoveries: bool = True
    rota_developments: bool = True
    rota_rare_technologies: bool = True
    rota_special_reputation: bool = True
    rota_sectors: bool = True
    rota_warp_portal: bool = True
    rota_ancient_homeworlds: bool = True
    rota_hive_sectors: bool = True
    # Shadow of the Rift
    sotr_discoveries: bool = True
    sotr_developments: bool = True
    sotr_rare_technologies: bool = True
    sotr_evolution: bool = True
    sotr_distortions: bool = True
    sotr_sectors: bool = True
    sotr_deep_warp: bool = True
    # Nebula mini-expansion
    nebula_discoveries: bool = True
    nebula_sectors: bool = True


config = Config()
