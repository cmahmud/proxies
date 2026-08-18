# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 269
- HTTP: 308 alive / 46 gold
- HTTPS: 202 alive / 11 gold
- SOCKS4: 211 alive / 110 gold
- SOCKS5: 220 alive / 102 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14447
- Ever gold: 461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
