# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 296
- HTTP: 371 alive / 60 gold
- HTTPS: 284 alive / 19 gold
- SOCKS4: 208 alive / 114 gold
- SOCKS5: 207 alive / 103 gold

## Historical pool

- Discovered: 109985
- Ever alive: 15588
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
