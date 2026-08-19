# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 403
- HTTP: 324 alive / 81 gold
- HTTPS: 192 alive / 14 gold
- SOCKS4: 261 alive / 150 gold
- SOCKS5: 231 alive / 158 gold

## Historical pool

- Discovered: 129331
- Ever alive: 20497
- Ever gold: 867

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
