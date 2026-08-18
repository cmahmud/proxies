# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 209
- HTTP: 523 alive / 34 gold
- HTTPS: 230 alive / 10 gold
- SOCKS4: 233 alive / 97 gold
- SOCKS5: 209 alive / 68 gold

## Historical pool

- Discovered: 85839
- Ever alive: 5721
- Ever gold: 287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
