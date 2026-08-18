# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 262
- HTTP: 469 alive / 30 gold
- HTTPS: 182 alive / 4 gold
- SOCKS4: 226 alive / 121 gold
- SOCKS5: 236 alive / 107 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11001
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
