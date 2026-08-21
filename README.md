# SyndProxy private pool

## Current pool

- Alive now: 1114
- Gold now: 421
- HTTP: 372 alive / 105 gold
- HTTPS: 305 alive / 26 gold
- SOCKS4: 210 alive / 157 gold
- SOCKS5: 227 alive / 133 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28459
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
