# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 285
- HTTP: 303 alive / 65 gold
- HTTPS: 232 alive / 18 gold
- SOCKS4: 205 alive / 102 gold
- SOCKS5: 199 alive / 100 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15394
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
