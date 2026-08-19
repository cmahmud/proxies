# SyndProxy private pool

## Current pool

- Alive now: 1273
- Gold now: 386
- HTTP: 423 alive / 91 gold
- HTTPS: 279 alive / 20 gold
- SOCKS4: 260 alive / 138 gold
- SOCKS5: 311 alive / 137 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21490
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
