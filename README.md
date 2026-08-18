# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 266
- HTTP: 336 alive / 35 gold
- HTTPS: 248 alive / 6 gold
- SOCKS4: 246 alive / 120 gold
- SOCKS5: 242 alive / 105 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11054
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
