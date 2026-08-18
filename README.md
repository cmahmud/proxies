# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 267
- HTTP: 292 alive / 34 gold
- HTTPS: 226 alive / 5 gold
- SOCKS4: 226 alive / 122 gold
- SOCKS5: 249 alive / 106 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11057
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
