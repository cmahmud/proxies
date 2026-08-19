# SyndProxy private pool

## Current pool

- Alive now: 1432
- Gold now: 437
- HTTP: 483 alive / 97 gold
- HTTPS: 362 alive / 25 gold
- SOCKS4: 263 alive / 148 gold
- SOCKS5: 324 alive / 167 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22466
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
