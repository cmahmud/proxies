# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 266
- HTTP: 327 alive / 35 gold
- HTTPS: 233 alive / 6 gold
- SOCKS4: 232 alive / 120 gold
- SOCKS5: 233 alive / 105 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11054
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
