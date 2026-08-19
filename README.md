# SyndProxy private pool

## Current pool

- Alive now: 1629
- Gold now: 434
- HTTP: 598 alive / 98 gold
- HTTPS: 405 alive / 24 gold
- SOCKS4: 287 alive / 145 gold
- SOCKS5: 339 alive / 167 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22474
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
