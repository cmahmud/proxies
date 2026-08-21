# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 407
- HTTP: 423 alive / 106 gold
- HTTPS: 285 alive / 26 gold
- SOCKS4: 226 alive / 150 gold
- SOCKS5: 227 alive / 125 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28552
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
