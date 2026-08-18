# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 257
- HTTP: 279 alive / 28 gold
- HTTPS: 167 alive / 9 gold
- SOCKS4: 227 alive / 118 gold
- SOCKS5: 236 alive / 102 gold

## Historical pool

- Discovered: 95227
- Ever alive: 10176
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
