# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 275
- HTTP: 271 alive / 52 gold
- HTTPS: 192 alive / 11 gold
- SOCKS4: 215 alive / 110 gold
- SOCKS5: 220 alive / 102 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14447
- Ever gold: 463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
