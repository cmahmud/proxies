# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 282
- HTTP: 293 alive / 37 gold
- HTTPS: 170 alive / 10 gold
- SOCKS4: 216 alive / 140 gold
- SOCKS5: 158 alive / 95 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13936
- Ever gold: 434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
