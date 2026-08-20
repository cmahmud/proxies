# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 367
- HTTP: 180 alive / 70 gold
- HTTPS: 136 alive / 19 gold
- SOCKS4: 189 alive / 118 gold
- SOCKS5: 232 alive / 160 gold

## Historical pool

- Discovered: 148331
- Ever alive: 26063
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
