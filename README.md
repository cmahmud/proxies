# SyndProxy private pool

## Current pool

- Alive now: 1138
- Gold now: 283
- HTTP: 464 alive / 30 gold
- HTTPS: 244 alive / 7 gold
- SOCKS4: 213 alive / 126 gold
- SOCKS5: 217 alive / 120 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13107
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
