# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 396
- HTTP: 310 alive / 83 gold
- HTTPS: 180 alive / 21 gold
- SOCKS4: 232 alive / 147 gold
- SOCKS5: 263 alive / 145 gold

## Historical pool

- Discovered: 158238
- Ever alive: 29983
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
