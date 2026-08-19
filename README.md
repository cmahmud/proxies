# SyndProxy private pool

## Current pool

- Alive now: 1230
- Gold now: 406
- HTTP: 437 alive / 104 gold
- HTTPS: 286 alive / 25 gold
- SOCKS4: 213 alive / 130 gold
- SOCKS5: 294 alive / 147 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22576
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
