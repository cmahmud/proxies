# SyndProxy private pool

## Current pool

- Alive now: 1476
- Gold now: 423
- HTTP: 569 alive / 115 gold
- HTTPS: 345 alive / 22 gold
- SOCKS4: 247 alive / 133 gold
- SOCKS5: 315 alive / 153 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22677
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
