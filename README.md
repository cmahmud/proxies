# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 407
- HTTP: 284 alive / 95 gold
- HTTPS: 243 alive / 30 gold
- SOCKS4: 206 alive / 150 gold
- SOCKS5: 222 alive / 132 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30964
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
