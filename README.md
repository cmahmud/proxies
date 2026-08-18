# SyndProxy private pool

## Current pool

- Alive now: 730
- Gold now: 247
- HTTP: 215 alive / 25 gold
- HTTPS: 115 alive / 2 gold
- SOCKS4: 194 alive / 114 gold
- SOCKS5: 206 alive / 106 gold

## Historical pool

- Discovered: 99103
- Ever alive: 11508
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
