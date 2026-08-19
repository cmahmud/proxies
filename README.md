# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 419
- HTTP: 314 alive / 89 gold
- HTTPS: 239 alive / 24 gold
- SOCKS4: 233 alive / 146 gold
- SOCKS5: 280 alive / 160 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22340
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
