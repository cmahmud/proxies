# SyndProxy private pool

## Current pool

- Alive now: 716
- Gold now: 384
- HTTP: 193 alive / 72 gold
- HTTPS: 115 alive / 14 gold
- SOCKS4: 193 alive / 139 gold
- SOCKS5: 215 alive / 159 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25806
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
