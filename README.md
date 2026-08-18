# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 258
- HTTP: 415 alive / 31 gold
- HTTPS: 167 alive / 4 gold
- SOCKS4: 227 alive / 117 gold
- SOCKS5: 227 alive / 106 gold

## Historical pool

- Discovered: 95405
- Ever alive: 11000
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
