# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 381
- HTTP: 323 alive / 94 gold
- HTTPS: 232 alive / 25 gold
- SOCKS4: 222 alive / 129 gold
- SOCKS5: 244 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25068
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
