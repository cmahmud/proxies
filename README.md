# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 265
- HTTP: 355 alive / 35 gold
- HTTPS: 177 alive / 6 gold
- SOCKS4: 224 alive / 119 gold
- SOCKS5: 241 alive / 105 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11004
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
