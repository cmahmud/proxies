# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 281
- HTTP: 288 alive / 37 gold
- HTTPS: 175 alive / 10 gold
- SOCKS4: 215 alive / 140 gold
- SOCKS5: 159 alive / 94 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13934
- Ever gold: 434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
