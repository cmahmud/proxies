# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 363
- HTTP: 251 alive / 89 gold
- HTTPS: 156 alive / 30 gold
- SOCKS4: 187 alive / 114 gold
- SOCKS5: 224 alive / 130 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32576
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
