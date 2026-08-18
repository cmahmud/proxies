# SyndProxy private pool

## Current pool

- Alive now: 595
- Gold now: 205
- HTTP: 154 alive / 26 gold
- HTTPS: 86 alive / 7 gold
- SOCKS4: 178 alive / 102 gold
- SOCKS5: 177 alive / 70 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8360
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
