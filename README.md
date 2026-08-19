# SyndProxy private pool

## Current pool

- Alive now: 1343
- Gold now: 381
- HTTP: 468 alive / 87 gold
- HTTPS: 354 alive / 16 gold
- SOCKS4: 227 alive / 146 gold
- SOCKS5: 294 alive / 132 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21797
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
