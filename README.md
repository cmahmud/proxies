# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 356
- HTTP: 372 alive / 70 gold
- HTTPS: 227 alive / 12 gold
- SOCKS4: 213 alive / 128 gold
- SOCKS5: 253 alive / 146 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20364
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
