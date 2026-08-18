# SyndProxy private pool

## Current pool

- Alive now: 560
- Gold now: 215
- HTTP: 140 alive / 27 gold
- HTTPS: 71 alive / 8 gold
- SOCKS4: 168 alive / 109 gold
- SOCKS5: 181 alive / 71 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8360
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
