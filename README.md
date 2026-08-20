# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 418
- HTTP: 352 alive / 102 gold
- HTTPS: 238 alive / 24 gold
- SOCKS4: 193 alive / 128 gold
- SOCKS5: 313 alive / 164 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24876
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
