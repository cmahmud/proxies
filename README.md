# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 363
- HTTP: 385 alive / 96 gold
- HTTPS: 264 alive / 22 gold
- SOCKS4: 179 alive / 113 gold
- SOCKS5: 225 alive / 132 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28814
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
