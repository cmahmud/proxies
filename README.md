# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 356
- HTTP: 280 alive / 72 gold
- HTTPS: 206 alive / 13 gold
- SOCKS4: 211 alive / 124 gold
- SOCKS5: 227 alive / 147 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20292
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
