# SyndProxy private pool

## Current pool

- Alive now: 1295
- Gold now: 216
- HTTP: 552 alive / 34 gold
- HTTPS: 235 alive / 9 gold
- SOCKS4: 285 alive / 101 gold
- SOCKS5: 223 alive / 72 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6405
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
