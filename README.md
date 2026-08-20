# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 377
- HTTP: 324 alive / 90 gold
- HTTPS: 230 alive / 25 gold
- SOCKS4: 221 alive / 129 gold
- SOCKS5: 245 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25068
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
