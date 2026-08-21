# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 412
- HTTP: 312 alive / 86 gold
- HTTPS: 235 alive / 21 gold
- SOCKS4: 205 alive / 151 gold
- SOCKS5: 252 alive / 154 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29934
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
