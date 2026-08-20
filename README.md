# SyndProxy private pool

## Current pool

- Alive now: 1896
- Gold now: 700
- HTTP: 722 alive / 234 gold
- HTTPS: 603 alive / 146 gold
- SOCKS4: 240 alive / 155 gold
- SOCKS5: 331 alive / 165 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24427
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
