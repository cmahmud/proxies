# SyndProxy private pool

## Current pool

- Alive now: 1341
- Gold now: 215
- HTTP: 550 alive / 33 gold
- HTTPS: 278 alive / 9 gold
- SOCKS4: 290 alive / 101 gold
- SOCKS5: 223 alive / 72 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
