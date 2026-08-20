# SyndProxy private pool

## Current pool

- Alive now: 1803
- Gold now: 706
- HTTP: 677 alive / 238 gold
- HTTPS: 553 alive / 146 gold
- SOCKS4: 240 alive / 158 gold
- SOCKS5: 333 alive / 164 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24378
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
