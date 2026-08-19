# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 403
- HTTP: 277 alive / 78 gold
- HTTPS: 232 alive / 12 gold
- SOCKS4: 258 alive / 153 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20552
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
