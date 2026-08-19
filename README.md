# SyndProxy private pool

## Current pool

- Alive now: 1292
- Gold now: 424
- HTTP: 434 alive / 91 gold
- HTTPS: 336 alive / 23 gold
- SOCKS4: 225 alive / 150 gold
- SOCKS5: 297 alive / 160 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22381
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
