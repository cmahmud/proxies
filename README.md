# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 267
- HTTP: 308 alive / 35 gold
- HTTPS: 222 alive / 5 gold
- SOCKS4: 224 alive / 120 gold
- SOCKS5: 239 alive / 107 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11057
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
