# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 285
- HTTP: 351 alive / 30 gold
- HTTPS: 188 alive / 6 gold
- SOCKS4: 253 alive / 125 gold
- SOCKS5: 246 alive / 124 gold

## Historical pool

- Discovered: 102840
- Ever alive: 13131
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
