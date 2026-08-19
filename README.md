# SyndProxy private pool

## Current pool

- Alive now: 1610
- Gold now: 436
- HTTP: 581 alive / 98 gold
- HTTPS: 411 alive / 24 gold
- SOCKS4: 281 alive / 148 gold
- SOCKS5: 337 alive / 166 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22468
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
