# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 338
- HTTP: 363 alive / 65 gold
- HTTPS: 212 alive / 11 gold
- SOCKS4: 243 alive / 142 gold
- SOCKS5: 215 alive / 120 gold

## Historical pool

- Discovered: 129271
- Ever alive: 20251
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
