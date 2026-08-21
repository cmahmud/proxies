# SyndProxy private pool

## Current pool

- Alive now: 1119
- Gold now: 438
- HTTP: 381 alive / 107 gold
- HTTPS: 285 alive / 35 gold
- SOCKS4: 216 alive / 136 gold
- SOCKS5: 237 alive / 160 gold

## Historical pool

- Discovered: 152762
- Ever alive: 28384
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
