# SyndProxy private pool

## Current pool

- Alive now: 1784
- Gold now: 684
- HTTP: 677 alive / 235 gold
- HTTPS: 537 alive / 121 gold
- SOCKS4: 250 alive / 158 gold
- SOCKS5: 320 alive / 170 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24362
- Ever gold: 996

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
