# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 379
- HTTP: 401 alive / 101 gold
- HTTPS: 268 alive / 31 gold
- SOCKS4: 213 alive / 110 gold
- SOCKS5: 263 alive / 137 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28322
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
