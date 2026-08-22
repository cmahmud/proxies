# SyndProxy private pool

## Current pool

- Alive now: 805
- Gold now: 357
- HTTP: 248 alive / 87 gold
- HTTPS: 133 alive / 29 gold
- SOCKS4: 190 alive / 105 gold
- SOCKS5: 234 alive / 136 gold

## Historical pool

- Discovered: 167356
- Ever alive: 32557
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
