# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 276
- HTTP: 453 alive / 30 gold
- HTTPS: 162 alive / 5 gold
- SOCKS4: 232 alive / 132 gold
- SOCKS5: 214 alive / 109 gold

## Historical pool

- Discovered: 99074
- Ever alive: 11376
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
