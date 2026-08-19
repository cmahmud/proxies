# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 484
- HTTP: 434 alive / 148 gold
- HTTPS: 295 alive / 75 gold
- SOCKS4: 225 alive / 123 gold
- SOCKS5: 253 alive / 138 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17278
- Ever gold: 645

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
